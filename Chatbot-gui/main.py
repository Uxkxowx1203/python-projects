from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLineEdit, QPushButton,QApplication
import sys
import openai
from backend1 import ChatBot
import threading

class ChatBotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.chatbot=ChatBot()
        self.setMinimumSize(700,500)
        self.setWindowTitle("ChatBot")
    
        #chat area widget
        self.chat_area=QTextEdit(self)
        
        self.chat_area.setGeometry(10,10,480,320)
        self.chat_area.setReadOnly(True)
        #input text widget
        self.input_area=QLineEdit(self)
        self.input_area.setGeometry(10,340,480,40)
        self.input_area.returnPressed.connect(self.send_message)
        #add button widget
        self.button=QPushButton("send",self)
        
        self.button.setGeometry(500,340,100,40)
        self.button.clicked.connect(self.send_message)

        self.show()
    def send_message(self):
        user_input=self.input_area.text().strip()
    
        self.chat_area.append(f"<p style='color:#E9E9E9'>Me: {user_input}</p>")
        self.input_area.clear()
        #thread=threading.Thread(target=self.get_bot_response,args=(user_input, ))
        #thread.start()
    #def get_bot_response(self,user_input):
        response=self.chatbot.get_response(user_input)
        self.chat_area.append(f"<p style='color:#333333; background-color: #E9E9E9'>Bot: {response}</p>")



app= QApplication(sys.argv)
main_window=ChatBotWindow()
sys.exit(app.exec())
