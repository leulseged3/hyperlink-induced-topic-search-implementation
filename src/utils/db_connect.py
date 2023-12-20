import psycopg2

def create_connection():
  DB_NAME = 'ewupcyuy'
  DB_USER = 'ewupcyuy'
  DB_PASSWORD = 'AcIwKA4-9kJww5JfWGucnj3ime1caG1l'
  DB_HOST = 'horton.db.elephantsql.com'
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
