-- CREATE TABLE

CREATE TABLE IF NOT EXISTS Users(
    -- NAME         TYPE            CONSTRAINTS
       id           INTEGER         PRIMARY KEY     AUTOINCREMENT,

       name         TEXT                                         ,
       money        REAL                                         , -- 4.7
       file         BLOB                                         ,
       --           NULL

       --           --              NOT NULL
       --           --              DEFAULT 'TEST'
       --           --              UNIQUE
       --           --              CHECK ( age >= 10 )
);

CREATE TABLE IF NOT EXISTS Dogs(
    id          INTEGER         PRIMARY KEY     AUTOINCREMENT,
    name        TEXT            NOT NULL,
    breed       TEXT            NOT NULL    DEFAULT 'unknown',
    dob         INTEGER         ,
    owner_id    INTEGER     REFERENCES Owners(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Owners(
    id INTEGER         PRIMARY KEY     AUTOINCREMENT,
    name TEXT   NOT NULL
)

-- INSERT
INSERT INTO Owners ( name )
  VALUES ( 'Test1' ), ( 'Test2' ), ( 'Test3' );



-- UPDATE

UPDATE Dogs
   SET name = 'Bobik';

UPDATE Dogs
   SET name = 'Bobik'
 WHERE id = 5;


-- DELETE
DELETE FROM Dogs;

DELETE FROM Dogs WHERE name='Test';
