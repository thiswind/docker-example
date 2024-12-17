from flask import Flask, request, jsonify
import mysql.connector
import os

app = Flask(__name__)

# 获取环境变量
db_host = os.getenv('DB_HOST', 'localhost')
db_user = os.getenv('DB_USER', 'your_username')
db_password = os.getenv('DB_PASSWORD', 'your_password')
db_name = os.getenv('DB_NAME', 'your_database')

def get_db_connection():
    return mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(users)

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    name = data['name']
    email = data['email']

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = 'INSERT INTO users (name, email) VALUES (%s, %s)'
    values = (name, email)
    cursor.execute(query, values)
    conn.commit()
    user_id = cursor.lastrowid
    cursor.close()
    conn.close()

    return jsonify({'id': user_id}), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')