import sqlite3

from constants.database_queries import (CHECK_IF_ROW_EXISTS,
                                        CREATE_BEANS_TABLE, GET_ALL_BEANS,
                                        GET_ALL_PREPARATION_METHODS,
                                        GET_BEANS_BY_NAME,
                                        GET_BEST_PREPARATION_FOR_BEAN,
                                        GET_COLUMN_NAMES, INSERT_BEAN)
from constants.globals import db_path, export_csv_path


def connect():
    return sqlite3.connect(db_path)


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
        return columns


def get_all_preparation_methods(connection):
    with connection:
        return connection.execute(GET_ALL_PREPARATION_METHODS).fetchall()


def write_csv_header(connection):
    with open(export_csv_path, 'w+') as file:
        file.write(','.join(get_column_names(connection)) + '\n')
    file.close()


def export_database_to_csv(connection):
    with connection:
        all_data = connection.execute(GET_ALL_BEANS).fetchall()
        write_csv_header(connection)
        with open(export_csv_path, 'a') as file:
            for row in all_data:
                file.write(','.join(str(value) for value in row) + '\n')
        file.close()


def check_if_row_exists(connection, name, method, rating):
    with connection:
        return connection.execute(CHECK_IF_ROW_EXISTS,
                                  (name, method, rating)).fetchone()


def import_database_from_csv(connection):
    new_additions = 0
    with connection:
        with open('data.csv', 'r') as file:
            lines = file.readlines()
            del lines[0]
            for line in lines:
                line = line.strip().split(',')
                if (check_if_row_exists(connection, line[1], line[2], line[3]) == None):
                    add_bean(connection, line[1], line[2], line[3])
                    new_additions += 1
        file.close()
    write_csv_header(connection)
    return new_additions
