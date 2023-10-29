from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

# Thiết lập kết nối MySQL
db = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password='',
    database='dbtest'
)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(data):
    sender, message = data['sender'], data['message']

    # Lưu tin nhắn vào cơ sở dữ liệu
    cursor = db.cursor()
    insert_query = "INSERT INTO messages (sender, message) VALUES (%s, %s)"
    cursor.execute(insert_query, (sender, message))
    db.commit()
    cursor.close()

    emit('message', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
