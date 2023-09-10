import tkinter as tk
import nltk
from nltk.chat.util import Chat, reflections

root = tk.Tk()
root.title("Chatbot")

pairs = [
    [
        r"hello|hi|hey",
        ["Hello", "Hey there","Hi"]
    ],
    [
        r"how are you ?",
        ["I am fine, thank you! How can I help you?"]
    ],
    [
        r"what (.*) you ?",
        ["I am a chatbot.", "I am a chatbot. What about you?"]
    ]
]


default_pairs = [
    r"(.*)",
    ["Sorry. I didn't get it."]
]

pairs.append(default_pairs)


# def send():
#     send = "You -> "+e.get()
#     txt.insert(tk.END, "\n"+send)
#     user = e.get().lower()
#     if user == "hello":
#         txt.insert(tk.END, "\n" + "Bot -> Hi")
#     elif user == "hi":
#         txt.insert(tk.END, "\n" + "Bot -> Hello")
#     elif user == "how are you":
#         txt.insert(tk.END, "\n" + "Bot -> Fine. And you?")
#     elif user == "fine" or user == "i am fine":
#         txt.insert(tk.END, "\n" + "Bot -> Nice to hear that. How can I help you?")
#     else:
#         txt.insert(tk.END, "\n" + "Bot -> Sorry. I didn't get it.")
#     e.delete(0, tk.END)
    
def send():
    input = e.get().lower()
    chat_reply = chatbot.respond(input)
    print(input ,chat_reply)
    txt.insert(tk.END, "\n" + "You -> " + input)
    txt.insert(tk.END, "\n" + "Bot -> " + chat_reply)
    e.delete(0, tk.END)
    
chatbot = Chat(pairs, reflections)
txt = tk.Text(root)
txt.grid(row=0, column=0, columnspan=2)
e = tk.Entry(root, width=100)
e.grid(row=1, column=0)
send = tk.Button(root, text="Send", command=send).grid(row=1, column=1)
root.mainloop()