from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QTextEdit
import sys
import threading  # Import threading module
from backend import chatbot  # Import the Chatbot class correctly
from PyQt6.QtCore import QMetaObject, Qt

class ChatboxWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.chatbot = chatbot()  # Correctly initialize the Chatbot class
        
        self.setMinimumSize(700, 500)
        
        # Adding the chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 380, 420)
        self.chat_area.setReadOnly(True)
        
        # Adding the input field widget
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 440, 380, 40)
        
        # Adding the button widget
        self.button = QPushButton('Send', self)
        self.button.setGeometry(400, 440, 80, 40)
        self.button.clicked.connect(self.send_message)
        self.show()
    
    def send_message(self):
        user_input = self.input_field.text().strip()
        if user_input:
            self.chat_area.append(f"<p style='color:#333333'>Me: {user_input}</p>")
            self.input_field.clear()
            
            # Start a new thread to handle bot response
            thread = threading.Thread(target=self.get_bot_response, args=(user_input,))
            thread.start()  # Correct method to start the thread
    
    def get_bot_response(self, user_input):
        # Get the bot response from chatbot instance
        response = self.chatbot.get_responce(user_input)
        
        # Use thread-safe method to update the chat area
        QMetaObject.invokeMethod(self.chat_area, "append", Qt.QueuedConnection, 
                                 QMetaObject.createArgument(str, f"<p style='color:#333333'>Bot: {response}</p>"))

# Application execution
app = QApplication(sys.argv)
window = ChatboxWindow()
sys.exit(app.exec())
