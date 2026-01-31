import psycopg2
from psycopg2 import sql

class DatabaseManager:
    def __init__(self,dbname, user, password, host='localhost', port='5432'):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None

    def connect(self):
        """Connect to the PostgreSQL database server"""
        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            print('Connection to database successful')
        except Exception as e:
            print(f'Could not connect to database: {e}')

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print('Database connection closed')

    def execute_query(self, query, params=None):
        """Execute a single query"""
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            self.connection.commit()

    def fetch_all(self, query, params=None):
        """Fetch all results from a query"""
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()  

    def fetch_one(self, query, params=None):
        """Fetch a single result from a query"""
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchone()  

# Example usage:
# db_manager = DatabaseManager('your_db', 'your_user', 'your_password')
# db_manager.connect()
# db_manager.execute_query('CREATE TABLE IF NOT EXISTS test (id SERIAL PRIMARY KEY, name VARCHAR(50));')
# db_manager.close_connection()