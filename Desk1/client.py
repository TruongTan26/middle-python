import socket
import tkinter as tk
import threading

def send_message():
    message = entry.get()
    client_socket.sendall(message.encode('utf-8'))

# Khởi tạo socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 5555))

# Giao diện cho Client
client_gui = tk.Tk()
client_gui.title("Client")

chat_box = tk.Text(client_gui)
chat_box.pack()

entry = tk.Entry(client_gui)
entry.pack()

send_button = tk.Button(client_gui, text="Send", command=send_message)
send_button.pack()

# Nhận và hiển thị tin nhắn từ server
def receive():
    while True:
        try:
            data = client_socket.recv(1024)
            if data:
                chat_box.insert(tk.END, data.decode('utf-8') + '\n')
        except:
            break

receive_thread = threading.Thread(target=receive)
receive_thread.start()

def on_closing():
    client_socket.close()
    client_gui.destroy()

client_gui.protocol("WM_DELETE_WINDOW", on_closing)

client_gui.mainloop()