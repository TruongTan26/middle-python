import tkinter as tk
from db import connect_db, create_cursor

# Tạo con trỏ cho kết nối
mydb = connect_db()
mycursor = create_cursor(mydb)

# Các hàm khác ở đây không thay đổi
def send_message():
    user_input = input_entry.get()
    output_text.insert(tk.END, "You: " + user_input + "\n")
    
    # Thực hiện truy vấn để kiểm tra tin nhắn của người dùng và lấy phản hồi từ cơ sở dữ liệu
    mycursor.execute("SELECT bot_response FROM bot_chat WHERE user_input = %s", (user_input,))
    result = mycursor.fetchone()
    
    if result:
        bot_response = result[0]
        output_text.insert(tk.END, "Bot: Typing...\n")
        root.after(2000, lambda: show_response(bot_response))
    else:
        output_text.insert(tk.END, "\nBot: Phản hồi mặc định\n")
    
    input_entry.delete(0, tk.END)
    output_text.see(tk.END)  # Cuộn xuống dòng tin nhắn mới nhất

def show_response(response):
    output_text.insert(tk.END, "Bot: " + response + "\n")
    output_text.see(tk.END)  

def on_enter(event=None):
    send_message()

root = tk.Tk()
root.title("Chat Bot")

output_text = tk.Text(root, height=20, width=50)
output_text.pack()

scrollbar = tk.Scrollbar(root, command=output_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
output_text.config(yscrollcommand=scrollbar.set)
# cho phép scroll ngược lại tin nhắn

input_frame = tk.Frame(root)
input_frame.pack(side=tk.BOTTOM)

input_entry = tk.Entry(input_frame, width=40)
input_entry.pack(side=tk.LEFT)

send_button = tk.Button(input_frame, text="Gửi", command=send_message)
send_button.pack(side=tk.LEFT)

input_entry.bind("<Return>", lambda event: send_message())

root.mainloop()
