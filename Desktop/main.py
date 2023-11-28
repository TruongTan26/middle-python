
from server import *
import threading
from application import Application
import time
import sys

def runGUI():
    app = Application()
    app.geometry("500x500")
    app.title("App1")
    app.resizable(False, False)
    app.mainloop()

def runChatServer(kill):
    ChatServer(kill)

def KillThread(t1):
    chatServer = threading.Thread(target=lambda: runChatServer(False))
    chatServer.start()
    while t1.is_alive():
        time.sleep(1)
        if t1.is_alive() == False:
            chatServer = threading.Thread(target=lambda: runChatServer(True))
            chatServer.start()
            chatServer.join(0)
            print("Dit me may in ra di lam on")
    

stop_thread = threading.Event()

GUI = threading.Thread(target=runGUI)
GUI.start()

checkThread = threading.Thread(target=lambda: KillThread(GUI))
checkThread.start()

checkThread.join(0)
sys.exit()
