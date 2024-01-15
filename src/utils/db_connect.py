import psycopg2

def create_connection(dbName):
  DB_NAME = dbName
  DB_USER = 'postgres'
  DB_PASSWORD = 'password'
  DB_HOST = 'localhost'
  DB_PORT = '5432'

  try:
    connection = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    return connection
  
  except psycopg2.Error as e:
    print("Error connecting to PostgreSQL:", e)
    return None
