__author__ = "Jonas Andersson"

import sqlite3

make_table_users_if_not_exists = 'CREATE TABLE IF NOT EXISTS users (name VARCHAR(80), password VARCHAR(80))'
make_table_measurements_if_not_exists = 'CREATE TABLE IF NOT EXISTS measurements' \
                                        ' (name VARCHAR(80), blood_pressure VARCHAR(80),' \
                                        'height VARCHAR(80), weight VARCHAR(80))'

def login():
    conn = sqlite3.connect('dbaseSQL.db')
    cursor = conn.cursor()
    return conn, cursor

def make_tables():
    conn, cursor = login()
    cursor.execute(make_table_users_if_not_exists)
    cursor.execute(make_table_measurements_if_not_exists)
    conn.commit()
    cursor.close()
    conn.close()