import sqlite3


CREATE_BEANS_TABLE = 'CREATE TABLE IF NOT EXISTS beans (id INTEGER PRIMARY KEY, name TEXT, method TEXT, Rating Integer);'
INSERT_BEAN = 'INSERT INTO beans (name,method,rating) VALUES (?, ?, ?);'
GET_ALL_BEANS = 'SELECT * FROM beans'
GET_BEANS_BY_NAME = 'SELECT * FROM beans WHERE name = ?'
GET_BEST_PREPARATION_FOR_BEAN = 'SELECT * FROM beans WHERE name = ? ORDER BY rating DESC LIMIT 1'
GET_WORST_PREPARATION_FOR_BEAN = 'SELECT * FROM beans WHERE name = ? ORDER BY rating ASC LIMIT 1'
GET_COLUMN_NAMES = 'PRAGMA table_info(beans);'
GET_ALL_PREPARATION_METHODS = 'SELECT method FROM beans GROUP BY method'


def connect():
    return sqlite3.connect('data.db')


def create_tables(connection):
    with connection:
        connection.execute(CREATE_BEANS_TABLE)


def add_bean(connection, name, method, rating):
    with connection:
        connection.execute(INSERT_BEAN, (name, method, rating))


def get_all_beans(connection):
    with connection:
        return connection.execute(GET_ALL_BEANS).fetchall()


def get_beans_by_name(connection, name):
    with connection:
        return connection.execute(GET_BEANS_BY_NAME, (name,)).fetchall()


def get_best_preparation_for_bean(connection, name):
    with connection:
        return connection.execute(GET_BEST_PREPARATION_FOR_BEAN, (name,)).fetchone()


def get_worst_preparation_for_bean(connection, name):
    with connection:
        return connection.execute(GET_BEST_PREPARATION_FOR_BEAN, (name,)).fetchone()


def get_column_names(connection):
    with connection:
        column_info = connection.execute(GET_COLUMN_NAMES).fetchall()
        columns = [entity[1] for entity in column_info]
        del columns[0]
        return columns

def get_all_preparation_methods(connection):
    with connection:
        return connection.execute(GET_ALL_PREPARATION_METHODS).fetchall()
