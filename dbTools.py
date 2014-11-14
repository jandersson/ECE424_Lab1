__author__ = "Jonas Andersson"

import sqlite3

make_table_users_if_not_exists = 'CREATE TABLE IF NOT EXISTS users (name VARCHAR(80), password VARCHAR(80))'
make_table_measurements_if_not_exists = ''

def login():
    conn = sqlite3.connect('dbaseSQL')
    cursor = conn.cursor()
    return conn, cursor

def make_tables(cursor):
    cursor.execute(make_table_users_if_not_exists)