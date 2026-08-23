# basic clicker template, but in PYTHON
import tkinter as tk
score = 0

root = tk.Tk()

root.title("Basic Clicker Template")
root.minsize(290, 100)
root.maxsize(290, 100)
def on_click():
    global score
    score = score + 1
    scoretxt.config(text=score)

scoretxt = tk.Label(root, text=score)
scoretxt.pack(padx=5, pady=5)

button = tk.Button(
    root,
    text="Click Me!",
    command=on_click,
)
button.pack(padx=5, pady=5)

root.mainloop()
