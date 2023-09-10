import tkinter as tk

root = tk.Tk()
root.title("Chatbot")

def send():
    send = "You -> "+e.get()
    txt.insert(tk.END, "\n"+send)
    user = e.get().lower()
    if user == "hello":
        txt.insert(tk.END, "\n" + "Bot -> Hi")
    elif user == "hi":
        txt.insert(tk.END, "\n" + "Bot -> Hello")
    elif user == "how are you":
        txt.insert(tk.END, "\n" + "Bot -> Fine. And you?")
    elif user == "fine" or user == "i am fine":
        txt.insert(tk.END, "\n" + "Bot -> Nice to hear that. How can I help you?")
    else:
        txt.insert(tk.END, "\n" + "Bot -> Sorry. I didn't get it.")
    e.delete(0, tk.END)
    
txt = tk.Text(root)
txt.grid(row=0, column=0, columnspan=2)
e = tk.Entry(root, width=100)
e.grid(row=1, column=0)
send = tk.Button(root, text="Send", command=send).grid(row=1, column=1)
root.mainloop()