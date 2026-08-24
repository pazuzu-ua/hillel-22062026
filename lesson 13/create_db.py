"""Create and populate lesson13.db for practising SELECT queries.

Schema (continues the Owners/Dogs domain from lesson 12):

    Owners  1 --- N  Dogs  1 --- N  Visits

Run:  python "lesson 13/create_db.py"
The script is idempotent: it drops the tables and recreates them from scratch.
"""

import random
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).with_name("lesson13.db")

SCHEMA = """
DROP TABLE IF EXISTS Visits;
DROP TABLE IF EXISTS Dogs;
DROP TABLE IF EXISTS Owners;

CREATE TABLE Owners(
    id          INTEGER     PRIMARY KEY AUTOINCREMENT,
    name        TEXT        NOT NULL,
    city        TEXT        NOT NULL DEFAULT 'unknown',
    email       TEXT        UNIQUE,
    balance     REAL        NOT NULL DEFAULT 0
);

CREATE TABLE Dogs(
    id          INTEGER     PRIMARY KEY AUTOINCREMENT,
    name        TEXT        NOT NULL,
    breed       TEXT        NOT NULL DEFAULT 'unknown',
    birth_year  INTEGER     NOT NULL,
    weight      REAL        NOT NULL CHECK ( weight > 0 ),
    owner_id    INTEGER     REFERENCES Owners(id) ON DELETE CASCADE
);

CREATE TABLE Visits(
    id          INTEGER     PRIMARY KEY AUTOINCREMENT,
    dog_id      INTEGER     NOT NULL REFERENCES Dogs(id) ON DELETE CASCADE,
    visit_date  TEXT        NOT NULL,       -- ISO 'YYYY-MM-DD'
    reason      TEXT        NOT NULL,
    price       REAL        NOT NULL DEFAULT 0
);
"""

OWNERS = [
    # (name, city, email, balance)
    ("Anna Kovalenko", "Kyiv", "anna.k@example.com", 1250.50),
    ("Borys Shevchenko", "Lviv", "borys.s@example.com", 340.00),
    ("Olena Tkachuk", "Kyiv", "olena.t@example.com", 0.00),
    ("Dmytro Bondarenko", "Odesa", "dmytro.b@example.com", 780.25),
    ("Iryna Melnyk", "Kharkiv", "iryna.m@example.com", 95.75),
    ("Petro Lysenko", "Lviv", "petro.l@example.com", 2100.00),
    ("Sofia Marchenko", "Dnipro", "sofia.m@example.com", 15.00),
    ("Taras Hnatiuk", "Kyiv", "taras.h@example.com", 640.10),
    ("Yuliia Savchenko", "Odesa", "yuliia.s@example.com", 0.00),
    ("Viktor Romanenko", "Kharkiv", "viktor.r@example.com", 430.90),
    ("Kateryna Boyko", "Dnipro", "kateryna.b@example.com", 1880.00),
    ("Andrii Zhuk", "Lviv", "andrii.z@example.com", 55.40),
    ("Nataliia Pavlenko", "Kyiv", "nataliia.p@example.com", 720.00),
    ("Oleh Danylchenko", "Poltava", "oleh.d@example.com", 310.30),
    ("Maryna Kravets", "Poltava", "maryna.k@example.com", 0.00),
]

DOGS = [
    # (name, breed, birth_year, weight, owner_index)  -- owner_index is 1-based
    ("Bobik", "mixed", 2018, 12.4, 1),
    ("Rex", "German Shepherd", 2016, 34.0, 1),
    ("Luna", "Labrador", 2020, 28.5, 1),
    ("Sirko", "mixed", 2015, 18.2, 2),
    ("Bella", "Beagle", 2021, 11.0, 2),
    ("Max", "Golden Retriever", 2017, 31.8, 3),
    ("Zhuchka", "mixed", 2019, 9.6, 3),
    ("Charlie", "Poodle", 2022, 7.3, 4),
    ("Daisy", "Corgi", 2020, 13.1, 4),
    ("Rocky", "Rottweiler", 2014, 48.0, 4),
    ("Milo", "Dachshund", 2021, 8.4, 5),
    ("Lola", "Chihuahua", 2019, 3.2, 5),
    ("Bruno", "Boxer", 2018, 29.7, 6),
    ("Nika", "Husky", 2016, 24.9, 6),
    ("Tuzik", "mixed", 2013, 15.5, 6),
    ("Molly", "Cocker Spaniel", 2022, 12.0, 7),
    ("Archie", "Border Collie", 2020, 19.4, 7),
    ("Simba", "Akita", 2017, 38.2, 8),
    ("Kaif", "mixed", 2023, 6.1, 8),
    ("Pushok", "Pomeranian", 2021, 3.9, 9),
    ("Graf", "Doberman", 2015, 40.3, 9),
    ("Sharik", "mixed", 2012, 21.0, 10),
    ("Vesta", "Samoyed", 2019, 22.6, 10),
    ("Ronnie", "Bulldog", 2018, 25.1, 10),
    ("Chip", "Jack Russell", 2022, 7.8, 11),
    ("Dana", "Great Dane", 2016, 62.5, 11),
    ("Baksik", "mixed", 2020, 14.3, 11),
    ("Zeus", "Malamute", 2014, 42.0, 12),
    ("Mira", "Shiba Inu", 2021, 10.2, 12),
    ("Toby", "Spaniel", 2019, 16.7, 13),
    ("Sonya", "Pug", 2020, 8.0, 13),
    ("Rudy", "Irish Setter", 2017, 27.4, 13),
    ("Bim", "mixed", 2011, 17.9, 14),
    ("Kesha", "Yorkshire Terrier", 2023, 3.5, 14),
    ("Nord", "Alabai", 2015, 68.0, 14),
    ("Lucky", "mixed", 2022, 11.6, 15),
    ("Ayza", "Shepherd", 2018, 33.3, 15),
    ("Fima", "French Bulldog", 2021, 12.8, 15),
    # strays: no owner, good for LEFT JOIN / IS NULL practice
    ("Grey", "Weimaraner", 2019, 30.0, None),
    ("Malysh", "unknown", 2023, 5.0, None),
]

REASONS = [
    "vaccination",
    "checkup",
    "surgery",
    "dental cleaning",
    "injury treatment",
    "deworming",
    "allergy",
    "grooming",
]

PRICE_BY_REASON = {
    "vaccination": (300, 600),
    "checkup": (150, 400),
    "surgery": (2000, 6000),
    "dental cleaning": (700, 1500),
    "injury treatment": (500, 2500),
    "deworming": (100, 250),
    "allergy": (250, 900),
    "grooming": (200, 700),
}


def generate_visits(dog_count, count=70, seed=13):
    """Build a deterministic list of visit rows."""
    rng = random.Random(seed)
    visits = []
    for _ in range(count):
        dog_id = rng.randint(1, dog_count)
        year = rng.randint(2023, 2025)
        month = rng.randint(1, 12)
        day = rng.randint(1, 28)
        reason = rng.choice(REASONS)
        low, high = PRICE_BY_REASON[reason]
        price = round(rng.uniform(low, high), 2)
        visits.append((dog_id, f"{year}-{month:02d}-{day:02d}", reason, price))
    return visits


def main():
    with sqlite3.connect(DB_PATH) as connection:
        connection.execute("PRAGMA foreign_keys = ON")
        connection.executescript(SCHEMA)

        connection.executemany(
            "INSERT INTO Owners (name, city, email, balance)"
            " VALUES (?, ?, ?, ?)",
            OWNERS,
        )
        connection.executemany(
            "INSERT INTO Dogs (name, breed, birth_year, weight, owner_id)"
            " VALUES (?, ?, ?, ?, ?)",
            DOGS,
        )
        connection.executemany(
            "INSERT INTO Visits (dog_id, visit_date, reason, price)"
            " VALUES (?, ?, ?, ?)",
            generate_visits(len(DOGS)),
        )

    with sqlite3.connect(DB_PATH) as connection:
        for table in ("Owners", "Dogs", "Visits"):
            cursor = connection.execute(f"SELECT COUNT(*) FROM {table}")
            (rows,) = cursor.fetchone()
            print(f"{table:<8} {rows} rows")
    print(f"database ready: {DB_PATH}")


if __name__ == "__main__":
    main()
