import tkinter as tk
from tkinter import scrolledtext
import threading

class ChatClient:
    def __init__(self, root, receive_func, write_func, nickname):
        self.root = root
        self.root.title(f"Chat Client - {nickname}")
        self.receive_func = receive_func
        self.write_func = write_func
        self.nickname = nickname

        self.root.configure(bg='#f0e4ff')

        self.chat_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, bg='#f9f4ff', highlightbackground='#d4b3ff', highlightthickness=2)
        self.chat_area.pack(padx=20, pady=5)
        self.chat_area.config(state=tk.DISABLED)

        self.chat_area.tag_config('self', foreground='#bf94f8')
        self.chat_area.tag_config('received', foreground='#8f3ff9')  

        self.message_entry = tk.Entry(self.root, width=50, bg='#f9f4ff', highlightbackground='#d4b3ff', highlightthickness=2)
        self.message_entry.pack(padx=20, pady=5)
        self.message_entry.bind("<Return>", self.send_message)

        self.send_button = tk.Button(self.root, text="Send", command=self.send_message, bg='#d2b6f7', highlightbackground='#d4b3ff', highlightthickness=2)
        self.send_button.pack(padx=20, pady=5)

        self.receive_thread = threading.Thread(target=self.receive)
        self.receive_thread.daemon = True
        self.receive_thread.start()

    def receive(self):
        self.receive_func(self.display_message)

    def display_message(self, message, tag=None):
        self.chat_area.config(state=tk.NORMAL)
        if tag is None:
            tag = 'received'  
        self.chat_area.insert(tk.END, message + '\n', tag)
        self.chat_area.config(state=tk.DISABLED)
        self.chat_area.yview(tk.END)

    def send_message(self, event=None):
        message = self.message_entry.get()
        self.write_func(message)
        self.display_message(f"{self.nickname}: {message}", 'self')
        self.message_entry.delete(0, tk.END)

if __name__ == "__main__":
    import client
    root = tk.Tk()
    chat_client = ChatClient(root, client.receive, client.write, client.nickname)
    root.mainloop()