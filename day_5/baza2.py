# baza danych - system przechowywania danych
# silnik - mechanizm przechowywania, zarządzzania i dostępu do danych
# bazy relacyjne, nierelacyjne
# sql, nosql
# ms sqlserver, oracle, mysql, mariadb, postgress, terradata, sqlite

import sqlite3

try:
    conn = sqlite3.connect("baza_danych.db")
    c = conn.cursor()
    print("Baza danych została podłączona")

    query  = """
    CREATE TABLE IF NOT EXISTS developers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    salary REAL NOT NULL);
            """

    c.execute(query)
    conn.commit()

    # insert = "INSERT INTO developers (id,name,email,salary) VALUES (1,'Radek','raj@raj.pl', 1000);"
    # c.execute(insert)
    # conn.commit()

    select = "SELECT * FROM developers;"
    for row in c.execute(select):
        print(row) # (1, 'Radek', 'raj@raj.pl', 1000.0)

    update = """
    UPDATE developers SET salary=11000 WHERE id=1;
             """
    c.execute(update)
    conn.commit()

except sqlite3.Error as e:
    print("Bład podłaczenia bazy danych:", e)
finally:
    if conn:
        conn.close()
        print("Podłaczenie zostało zamknięte")
# Baza danych została podłączona
# Podłaczenie zostało zamknięte

# powerquery, powerbi, pgadmin, dbeaver, TablePlus, sqldeveloper
