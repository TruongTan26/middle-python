import socket
import threading
import tkinter as tk
from tkinter import ttk

# Khởi tạo socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 5555))
server_socket.listen(5)

# Danh sách các client và các tab tương ứng
clients = []
client_tabs = {}
unread_messages = {}

# Giao diện cho Server
server_gui = tk.Tk()
server_gui.title("Server")

tabs = ttk.Notebook(server_gui)
tabs.pack(fill=tk.BOTH, expand=True)

# Gửi tin nhắn tới một client cụ thể
def send_message_to_client(client_socket, message):
    try:
        client_socket.sendall(message.encode('utf-8'))
    except:
        pass

# Xử lý kết nối từ client
def handle_client(client_socket, client_address):
    global clients, client_tabs, unread_messages

    client_name = f"Bàn {len(clients) + 1}"
    client_tab = tk.Frame(tabs)
    client_tabs[client_socket] = client_tab
    unread_messages[client_socket] = 0

    # Hiển thị tab của client
    tabs.add(client_tab, text=client_name)

    clients.append(client_socket)

    # Tạo giao diện nhập tin nhắn và nút gửi
    entry = tk.Entry(client_tab)
    entry.pack()

    send_button = tk.Button(client_tab, text="Send", command=lambda: send_message_to_client(client_socket, entry.get()))
    send_button.pack()

    chat_text = tk.Text(client_tab)
    chat_text.pack(fill=tk.BOTH, expand=True)

    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break

            # Hiển thị tin nhắn trên tab của client
            chat_text.insert(tk.END, f'Khách hàng: {data.decode("utf-8")} \n')
            unread_messages[client_socket] += 1

            # Cập nhật số tin nhắn chưa đọc trên tab
            tabs.tab(client_tab, text=f"{client_name} ({unread_messages[client_socket]})")

            # # Gửi tin nhắn tới các client khác
            # for client in clients:
            #     if client == client_socket: # if client != client_socket:
            #         send_message_to_client(client, f'{data.decode("utf-8")}_rfs')
        except:
            break
        

    client_socket.close()

def on_closing():
    server_socket.close()
    server_gui.destroy()
# Chấp nhận kết nối từ các client
def accept_connections():
    while True:
        client, addr = server_socket.accept()
        print(f"Connected with {addr}")
        
        # Tạo một luồng mới để xử lý kết nối với client
        client_thread = threading.Thread(target=handle_client, args=(client, addr))
        client_thread.start()

accept_thread = threading.Thread(target=accept_connections)
accept_thread.start()
server_gui.protocol("WM_DELETE_WINDOW", on_closing)
server_gui.mainloop()
