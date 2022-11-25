import os
import psycopg2
from flask import Flask, render_template, jsonify

app = Flask(__name__)


def get_db_connection():
    conn = psycopg2.connect(host=os.environ['DB_HOST'],
                            database=os.environ['DB_NAME'],
                            user=os.environ['DB_USERNAME'],
                            password=os.environ['DB_PASSWORD'])
    return conn

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM public.users;')
    users = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', users=users)


incomes = [
    { 'description': 'salary', 'amount': 5000 }
]
@app.route('/info')
def get_incomes():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT id FROM public.users;')
    # users = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(cur.rowcount)
