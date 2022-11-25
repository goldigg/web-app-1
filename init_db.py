import os
import psycopg2

conn = psycopg2.connect(
        host=os.environ["DB_HOST"],
        database=os.environ["DB_NAME"],
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'])

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS users;')
cur.execute('CREATE TABLE users (id serial PRIMARY KEY,'
                                 'first_name varchar (150) NOT NULL,'
                                 'last_name varchar (50) NOT NULL,'
                                 'age integer NOT NULL,'
                                 'description text,'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )

# Insert data into the table

cur.execute('INSERT INTO users (first_name, last_name, age, description)'
            'VALUES (%s, %s, %s, %s)',
            ('Alan',
             'Goldmann',
             15,
             'Older bother')
            )


cur.execute('INSERT INTO users (first_name, last_name, age, description)'
            'VALUES (%s, %s, %s, %s)',
            ('Grzegorz',
             'Goldmann',
             16,
             'It\'s me!')
            )

conn.commit()

cur.close()
conn.close()
