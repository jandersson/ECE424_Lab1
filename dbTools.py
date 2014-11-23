__author__ = "Jonas Andersson"

import sqlite3

database_name = 'medical.sqlite'
make_table_users_if_not_exists = 'CREATE TABLE IF NOT EXISTS users (name VARCHAR(80), password VARCHAR(80))'
make_table_measurements_if_not_exists = 'CREATE TABLE IF NOT EXISTS measurements' \
                                        ' (patient_name VARCHAR(80), blood_pressure VARCHAR(80),' \
                                        'height VARCHAR(80), weight VARCHAR(80))'


def login():
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    return conn, cursor


def make_tables():
    conn, cursor = login()
    cursor.execute(make_table_users_if_not_exists)
    cursor.execute(make_table_measurements_if_not_exists)
    #Check if test user is present in database. If it is not, create it
    cursor.execute('SELECT * FROM users WHERE name = (?) AND password = (?)', ('test', '1234'))
    result = cursor.fetchone()
    if result:
        print('Test user is present in users table')
    else:
        cursor.execute('INSERT INTO users (name, password) VALUES (?, ?)', ('test', '1234'))
    conn.commit()
    cursor.close()
    conn.close()


def get_login(login_info):
    """
    Takes a dictionary, login info, which contains the username and password supplied by the user
    :param login_info:
    :return:
    """
    conn, cursor = login()
    cursor.execute('SELECT * FROM users WHERE name =:name and password =:password', {'name': login_info['username'],
                                                                                     'password': login_info['password']})
    result = cursor.fetchone()
    print('login result: ' + str(result))
    return result


def insert_measurements(measurements):
    conn, cursor = login()
    cursor.execute("""INSERT INTO measurements (patient_name, blood_pressure, height, weight) VALUES (?,?,?,?)""",
                   (measurements['username'],
                   measurements['blood pressure'],
                   measurements['height'],
                   measurements['weight']))
    conn.commit()
    conn.close()


def get_latest_measurement(patient_name):
    conn, cursor = login()
    cursor.execute("SELECT * FROM measurements WHERE patient_name = (?) ORDER BY rowid DESC", (patient_name,))
    result = cursor.fetchone()
    print('Latest measurement: ' + str(result))
    measurement = None
    if result:
        measurement = {'username': result[0],
                       'blood pressure': result[1],
                       'height': result[2],
                       'weight': result[3]}
    return measurement