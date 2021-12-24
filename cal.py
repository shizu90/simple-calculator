from tkinter import *
import math
import cx_Freeze

operator = ""

#FUNCTIONS

def button_click(n):
    global operator
    operator = operator + str(n)
    input.set(operator)

def result():
    global operator
    equal = str(eval(operator))
    input.set(equal) 
    operator = ""

def sqrt_numbers():
    global operator
    operator = float(eval(operator)) 
    sqrt = math.sqrt(int(operator))
    input.set(sqrt)
    operator = str(sqrt)

def sqrd_number():
    global operator
    operator = float(eval(operator)) 
    sqrd = int(operator) * int(operator)
    input.set(sqrd)
    operator = str(sqrd)

def clear():
    global operator
    operator = ""
    input.set(operator)

#INTERFACE

interface = Tk()
interface.title("Calculator")
input = StringVar()

interface.geometry = ("300x275")

interface.configure(background="#FFFFFF")


text = Entry(interface, font=('arial', 20), textvariable = input, bd = 1, bg="white", justify='right').grid(columnspan=4, row= 0)

mult = Button(interface, text = "*", font = ('arial', 20), width=5, bg = '#F0F0F0', bd = 1, command=lambda:button_click("*"))
mult.grid(column=0, row=1)

div = Button(interface, text="/", font = ('arial', 20), width=5, bg = '#F0F0F0', bd = 1, command=lambda:button_click("/"))
div.grid(column=1, row=1)

rem = Button(interface, text="%", font=('arial', 20), width=5, bg = '#F0F0F0', bd = 1, command=lambda:button_click("%"))
rem.grid(column=2, row=1)

sqrt = Button(interface, text="²√x", font=('arial', 20), width=5, bg = '#F0F0F0', bd = 1, command=lambda:sqrt_numbers())
sqrt.grid(column=3, row=1)

sqrd = Button(interface, text="x²", font=('arial', 20), width=5, bg ='#F0F0F0', bd = 1, command=lambda:sqrd_number())
sqrd.grid(column=3, row=2)

add = Button(interface, text="+", font=('arial', 20), width=5, bg = "#F0F0F0", bd = 1, command=lambda:button_click("+"))
add.grid(column=3, row=3)

sub = Button(interface, text="-", font=('arial', 20), width=5, bg = "#F0F0F0", bd = 1, command=lambda:button_click("-"))
sub.grid(column=3, row=4)

res = Button(interface, text="=", font=('arial', 20), width=5, bg = "#9F9FFF", bd = 1, command=lambda:result())
res.grid(column=3, row=5)

cls = Button(interface, text="C", font=('arial', 20), width=5, bg = "#F0F0F0", bd = 1, command=lambda:clear())
cls.grid(column=2, row=5)

blank = Button(interface, text="", font=('arial', 20), width=5, bg = "#F0F0F0", bd = 1) #FUTURE FUNCTION
blank.grid(column=0, row=5)

number_7 = Button(interface, text="7", font=('arial', 20), width=5, bg = "#FFFFFF", bd = 1, command=lambda:button_click(7))
number_7.grid(column = 0, row = 2)

number_8 = Button(interface, text="8", font=('arial', 20), width=5, bg = "#FFFFFF", bd = 1, command=lambda:button_click(8))
number_8.grid(column = 1, row = 2)

number_9 = Button(interface, text="9", font=('arial', 20), width=5, bg = "#FFFFFF", bd = 1, command=lambda:button_click(9))
number_9.grid(column = 2, row = 2)

number_4 = Button(interface, text="4", font=('arial', 20), width=5, bg = "#FFFFFF", bd = 1, command=lambda:button_click(4))
number_4.grid(column = 0, row = 3)

number_5 = Button(interface, text="5", font=('arial', 20), width=5, bg = "#FFFFFF", bd = 1, command=lambda:button_click(5))
number_5.grid(column = 1, row = 3)

number_6 = Button(interface, text="6", font=('arial', 20), width=5, bg = "#FFFFFF", bd = 1, command=lambda:button_click(6))
number_6.grid(column = 2, row = 3)

number_1 = Button(interface, text="1", font=('arial', 20), width=5, bg = "#FFFFFF", bd = 1, command=lambda:button_click(1))
number_1.grid(column = 0, row = 4)

number_2 = Button(interface, text="2", font=('arial', 20), width=5, bg = "#FFFFFF", bd = 1, command=lambda:button_click(2))
number_2.grid(column = 1, row = 4)

number_3 = Button(interface, text = "3", font=('arial', 20), width=5, bg = "#FFFFFF", bd = 1, command=lambda:button_click(3))
number_3.grid(column = 2, row = 4)

number_0 = Button(interface, text = "0", font=('arial', 20), width=5, bg = "#FFFFFF", bd = 1, command=lambda:button_click(0))
number_0.grid(column = 1, row = 5)

interface.mainloop()



