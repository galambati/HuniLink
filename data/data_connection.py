import os
import psycopg2
import psycopg2.extras


def get_connection_data():
    user_name = os.environ.get('PSQL_USER_NAME')
    password = os.environ.get('PSQL_PASSWORD')
    host = os.environ.get('PSQL_HOST')
    database = os.environ.get('PSQL_DATABASE')

    final_variable = user_name and password and host and database

    if final_variable:
        return f"postgresql://{user_name}:{password}@{host}/{database}"
    else:
        raise KeyError('Some necessary data is missing!')


def open_db():
    try:
        connection_string = get_connection_data()
        connection = psycopg2.connect(connection_string)
        connection.autocommit = True
    except psycopg2.DatabaseError as exception:
        print('Database connection error occurred!')
        raise exception
    return connection


def connection_handler(function):
    def wrapper(*args, **kwargs):
        connection = open_db()
        dict_cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        return_value = function(dict_cursor, *args, **kwargs)
        dict_cursor.close()
        connection.close()
        return return_value
    return wrapper
