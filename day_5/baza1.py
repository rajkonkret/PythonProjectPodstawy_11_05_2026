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
except sqlite3.Error as e:
    print("Bład podłaczenia bazy danych:", e)
finally:
    if conn:
        conn.close()
        print("Podłaczenie zostało zamknięte")
