import sqlite3


# connection = sqlite3.connect("test.db")
# connection.execute("""
#     CREATE TABLE IF NOT EXISTS Owners(
#        id INTEGER         PRIMARY KEY     AUTOINCREMENT,
#        name TEXT   NOT NULL
#     );
# """)
# connection.close()

# connection = sqlite3.connect("test.db")
# cursor = connection.execute(
#     "INSERT INTO Owners (name) VALUES (?)",
#     ('Test1',)
# )
# print(cursor.lastrowid)
# connection.commit()
# print(cursor.lastrowid)
# connection.close()

# with sqlite3.connect("test.db") as connection:
#     cursor = connection.execute(
#         "INSERT INTO Owners (name) VALUES (?)",
#         ('Test2',)
#     )
#     print(cursor.lastrowid)


# with sqlite3.connect("test.db") as connection:
#     cursor = connection.execute(
#         "UPDATE Owners SET name='UPDATED Test1' WHERE id=?",
#         (1,)
#     )
#     print(cursor.rowcount)

# with sqlite3.connect("test.db") as connection:
#     cursor = connection.execute(
#         "DELETE FROM Owners WHERE id=?",
#         (2,)
#     )
#     print(cursor.rowcount)
