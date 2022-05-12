from data import data_connection


@data_connection.connection_handler
def insert_user_data(cursor, name, email, password, uni, course, starting_date):
    query = """
            INSERT INTO users (name, email, password, university, course, starting_date)
            VALUES (%(name)s, %(email)s, %(password)s, %(uni)s, %(course)s, %(starting_date)s)
            """
    cursor.execute(query, {'name': name, 'email': email, 'password': password, 'uni': uni, 'course': course,
          'starting_date': starting_date})


@data_connection.connection_handler
def get_unis(cursor):
    query = '''
        SELECT DISTINCT university
        FROM users
    '''
    cursor.execute(query)
    return cursor.fetchall()


@data_connection.connection_handler
def get_user_data(cursor, email, password):
    query = '''
        SELECT name
        FROM users
        WHERE email LIKE %(email)s AND password LIKE %(password)s
    '''
    cursor.execute(query, {'email': email, 'password': password})
    return cursor.fetchall()
