from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)

    if text == "=":
        try:
            result = str(eval(scvalue.get()))
            scvalue.set(result)
        except Exception as e:
            scvalue.set("Error")
    elif text == "C":
        scvalue.set("")
    else:
        scvalue.set(scvalue.get() + text)

# main window
root = Tk()
root.title("Calculator")
root.geometry("400x600")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 30 bold", justify=RIGHT)
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

# button layout
buttons = [
    ["9", "8", "7", "+"],
    ["6", "5", "4", "-"],
    ["3", "2", "1", "*"],
    ["0", "C", "=", "/"],
    ["%"]
]

for row in buttons:
    f = Frame(root, bg="grey")
    for btn in row:
        b = Button(f, text=btn, padx=20, pady=20, font="lucida 20 bold")
        b.pack(side=LEFT, padx=10, pady=10)
        b.bind("<Button-1>", click)
    f.pack()

root.mainloop()
