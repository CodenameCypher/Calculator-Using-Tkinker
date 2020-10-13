import tkinter
from tkinter import*
import time

val = ""
A = 0
operator = ""

def button1_isClicked():
    global val
    val = val + "1"
    data.set(val)

def button2_isClicked():
    global val
    val = val + "2"
    data.set(val)

def button3_isClicked():
    global val
    val = val + "3"
    data.set(val)

def button4_isClicked():
    global val
    val = val + "4"
    data.set(val)

def button5_isClicked():
    global val
    val = val + "5"
    data.set(val)

def button6_isClicked():
    global val
    val = val + "6"
    data.set(val)

def button7_isClicked():
    global val
    val = val + "7"
    data.set(val)

def button8_isClicked():
    global val
    val = val + "8"
    data.set(val)

def button9_isClicked():
    global val
    val = val + "9"
    data.set(val)

def button0_isClicked():
    global val
    val = val + "0"
    data.set(val)

def buttonC_isClicked():
    global val
    global A
    global operator
    operator = ""
    A = 0
    val = ""
    data.set(val)

def buttonPlus_isClicked():
    global val
    global A
    global operator
    operator = "+"
    A = int(val)
    val = val + "+"
    data.set(val)

def buttonMinus_isClicked():
    global val
    global A
    global operator
    operator = "-"
    A = int(val)
    val = val + "-"
    data.set(val)

def buttonMultiply_isClicked():
    global val
    global A
    global operator
    operator = "*"
    A = int(val)
    val = val + "x"
    data.set(val)

def buttonDivide_isClicked():
    global val
    global A
    global operator
    operator = "/"
    A = int(val)
    val = val + "/"
    data.set(val)


def buttonEquals_isClicked():
    global val
    global A
    global operator
    val2 = val
    if operator is "+":
        n2 = int(val2.split("+")[1])
        result = A + n2
        val = str(result)
        data.set(result)

    if operator is "-":
        n2 = int(val2.split("-")[1])
        result = A - n2
        val = str(result)
        data.set(result)

    if operator is "*":
        n2 = int(val2.split("x")[1])
        result = A * n2
        val = str(result)
        data.set(result)

    if operator is "/":
        n2 = int(val2.split("/")[1])
        if(n2 is 0) :
            data.set("Can't divide by 0")
        else: 
            result = A / n2
            val = str(result)
            data.set(result)


root = tkinter.Tk()
root.geometry("250x400+300+300")
root.title("Calculator Using Tkinter")


data = StringVar()
textBox = Label(root,text="Enter your text",anchor=SE,font=("times new roman",22), textvariable = data, background = "#ADD8E6", fg = "#000000")
textBox.pack(expand=True,fill="both")

#button rows
buttonRow1 = Frame(root)
buttonRow1.pack(expand = True, fill = "both")

buttonRow2 = Frame(root)
buttonRow2.pack(expand = True, fill = "both")

buttonRow3 = Frame(root)
buttonRow3.pack(expand = True, fill = "both")

buttonRow4 = Frame(root)
buttonRow4.pack(expand = True, fill = "both")


#button row 1 buttons 1 2 3 +
button_1 = Button(buttonRow1,text="1",font=("times new roman",16),relief = GROOVE,bg='#171717',fg='white',border=1,command=button1_isClicked)
button_1.pack(side = LEFT, expand=True, fill="both")
button_2 = Button(buttonRow1,text="2",font=("times new roman",16),relief = GROOVE,bg='#171717',fg='white',border=1,command=button2_isClicked)
button_2.pack(side = LEFT, expand=True, fill="both")
button_3 = Button(buttonRow1,text="3",font=("times new roman",16),relief = GROOVE,bg='#171717',fg='white',border=1,command=button3_isClicked)
button_3.pack(side = LEFT, expand=True, fill="both")
button_plus = Button(buttonRow1,text="+",font=("times new roman",16),relief = GROOVE,bg='#171717',fg='white',border=1,command=buttonPlus_isClicked)
button_plus.pack(side = LEFT, expand=True, fill="both")

#button row 2 buttons 4 5 6 -
button_4 = Button(buttonRow2,text="4",font=("times new roman",16),relief = GROOVE,bg='#171717',fg='white',border=1,command=button4_isClicked)
button_4.pack(side = LEFT, expand=True, fill="both")
button_5 = Button(buttonRow2,text="5",font=("times new roman",16),relief = GROOVE,bg='#171717',fg='white',border=1,command=button5_isClicked)
button_5.pack(side = LEFT, expand=True, fill="both")
button_6 = Button(buttonRow2,text="6",font=("times new roman",16),relief = GROOVE,bg='#171717',fg='white',border=1,command=button6_isClicked)
button_6.pack(side = LEFT, expand=True, fill="both")
button_minus = Button(buttonRow2,text="-",font=("times new roman",16),relief = GROOVE,bg='#171717',fg='white',border=1,command=buttonMinus_isClicked)
button_minus.pack(side = LEFT, expand=True, fill="both")

#button row 3 buttons 7 8 9 x
button_7 = Button(buttonRow3,text="7",font=("times new roman",16),relief = GROOVE,bg='#171717',fg='white',border=1,command=button7_isClicked)
button_7.pack(side = LEFT, expand=True, fill="both")
button_8 = Button(buttonRow3,text="8",font=("times new roman",16),relief = GROOVE,bg='#171717',fg='white',border=1,command=button8_isClicked)
button_8.pack(side = LEFT, expand=True, fill="both")
button_9 = Button(buttonRow3,text="9",font=("times new roman",16),relief = GROOVE,bg='#171717',fg='white',border=1,command=button9_isClicked)
button_9.pack(side = LEFT, expand=True, fill="both")
button_multiply = Button(buttonRow3,text="x",font=("times new roman",16),relief = GROOVE,bg='#171717',fg='white',border=1,command=buttonMultiply_isClicked)
button_multiply.pack(side = LEFT, expand=True, fill="both")

#button row 4 buttons c 0 = /
button_c = Button(buttonRow4,text="C",font=("times new roman",16),relief = GROOVE,bg='red',fg='white',border=2,command=buttonC_isClicked)
button_c.pack(side = LEFT, expand=True, fill="both")
button_0 = Button(buttonRow4,text="0",font=("times new roman",16),relief = GROOVE,bg='#171717',fg='white',border=1,command=button0_isClicked)
button_0.pack(side = LEFT, expand=True, fill="both")
button_equals = Button(buttonRow4,text="=",font=("times new roman",16),relief = GROOVE,bg='orange',fg='white',border=1,command=buttonEquals_isClicked)
button_equals.pack(side = LEFT, expand=True, fill="both")
button_divide = Button(buttonRow4,text="/",font=("times new roman",16),relief = GROOVE,bg='#171717',fg='white',border=1,command=buttonDivide_isClicked)
button_divide.pack(side = LEFT, expand=True, fill="both")


root.mainloop()