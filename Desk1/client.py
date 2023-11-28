import socket
import tkinter as tk
import threading, sys

# Giao diện cho Client
def chat(table_number):
    def send_message():
        message = entry.get()
        client_socket.sendall(message.encode('utf-8'))
        # client_socket.sendto(message.encode('utf-8'),("127.0.0.1",5555))
        chat_box.insert(tk.END, f'Bàn {table_number}: {message} \n')

    # Khởi tạo socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 5555))

    client_gui = tk.Tk()
    client_gui.title(f'Bàn {table_number}')

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
                    chat_box.insert(tk.END, f'Nhân viên: {data.decode("utf-8")} \n')
            except:
                break

    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    def on_closing():
        client_socket.close()
        client_gui.destroy()

    client_gui.protocol("WM_DELETE_WINDOW", on_closing)

    client_gui.mainloop()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Vui lòng nhập số bàn.")
    else:
        table_number = int(sys.argv[1])
        chat(table_number)