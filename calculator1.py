from tkinter import *

expression = ""

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="light green")
    gui.title("Simple Calculator")
    gui.geometry("270x150")
    equation = StringVar()
    expression_field = Entry(gui, textvariable=equation)
    expression_field.grid(columnspan=4, ipadx=70)

    # Buttons for digits and operators
    button1 = Button(gui, text='1', fg='black', bg='red', command=lambda: press(1), height=1, width=7)
    button1.grid(row=2, column=0)
    # ... (similarly for other buttons)

    gui.mainloop()
