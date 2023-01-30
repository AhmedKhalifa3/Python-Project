from lib2to3.pgen2.token import DOT
import math
from pyexpat import model
from tkinter import *
from turtle import bgcolor

import matplotlib.pyplot as plt
import numpy as np
from setuptools import Command

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# building a GUI window called root, setting its title and background color.
root = Tk()
root.title('CASIO LITE')
root.configure(background="black")


# All Script Function
# second degree equation functions

def plot2():
    global xs2
    # x_squared2_value is the coefficient of X^2
    x_squared2_value = x_squared2.get()
    xs2 = float(x_squared2_value)

    global f2
    # x_first2_value is the coefficient of X
    x_first2_value = x_first2.get()
    f2 = float(x_first2_value)

    global xc2
    # x_constant2_value is the constant value
    xconstant2_value = xconstant2.get()
    xc2 = float(xconstant2_value)

    x = np.linspace(-2, 2, 100)
    y = xs2 * (x ** 2) + x * f2 + xc2
    fig = plt.figure(figsize=(10, 5))

    # Create the plot
    plt.plot(x, y)

    # Show the plot
    plt.show()


# solving second degree equation using the coffiecients from the function above
def solver2():
    roots_of_equation.delete(0, END)
    d = (math.pow(f2, 2) - 4 * xs2 * xc2)
    if xs2 == 0:
        roots_of_equation.insert(0, 'The equation is not quadratic')
    elif d < 0:
        roots_of_equation.insert(0, "There is no answer")
    elif d == 0:
        x = (-f2 + d) / (2 * xs2)
        roots_of_equation.insert(0, "There is one answer: {}".format(x))
    elif d < 0:
        roots_of_equation.insert('The roots are imaginary numbers')
    else:
        x1 = (-f2 + (math.sqrt(d))) / (2 * xs2)
        x2 = (-f2 - (math.sqrt(d))) / (2 * xs2)
        roots_of_equation.insert(0, "There are two answers: {} and {}".format(x1, x2))


# first degree equation
def plot1():
    global f1
    # x_first1_value is the coefficient of X
    x_first1_value = x_first1.get()
    f1 = float(x_first1_value)

    global xc1
    # x_constant1_value is the constant value
    xconstant1_value = xconstant1.get()
    xc1 = float(xconstant1_value)

    x = np.linspace(-25, 25, 100)
    y = f1 * x  + xc1
    fig = plt.figure(figsize=(10, 5))

    # Create the plot
    plt.plot(x, y)

    # Show the plot
    plt.show()


# solving first degree equation using the coefficients from the function above
def solver1():
    roots_of_equation.delete(0, END)
    rooot = -xc1 / f1
    roots_of_equation.insert(0, 'x = {}'.format(rooot))


# first degree differential equation solver
def defrentiate():
    k = float(input('Enter the constant value: '))

    def model(y, t):
        dydt = -k * y
        return dydt

    # initial condition
    y0 = float(input('Enter the initial value: '))

    # time points
    t = np.linspace(0, 20)

    # solve ODE
    y = odeint(model, y0, t)

    # plot results
    plt.plot(t, y)
    plt.xlabel('time')
    plt.ylabel('y(t)')
    plt.show()


# ----------------------------------------------------------------------------------------------------------------
# button click function get the inserted number in the entry and combine it with the existing number in the main entry
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))



# clear function deletes what is inside the ENtry from start to end
def clear():
    e.delete(0, END)


# dot function insert a dot
def dot():
    e.insert(END, '.')
    float(e.get(0, END))


# add function to add to numbers
def add():
    first_number = e.get()
    global F_num
    global math
    math = 'addition'
    F_num = float(first_number)
    e.delete(0, END)


# subtract function to subtract to numbers
def substract():
    first_number = e.get()
    global F_num
    global math
    math = 'subtraction'
    F_num = float(first_number)
    e.delete(0, END)


# multiply function to multiply to numbers
def multiply():
    first_number = e.get()
    global F_num
    global math
    math = 'multiply'
    F_num = float(first_number)
    e.delete(0, END)


# divide function to divide to numbers
def divide():
    first_number = e.get()
    global F_num
    global math
    math = 'devide'
    F_num = float(first_number)
    e.delete(0, END)


# remain function get the remainder of deviding number on number
def remain():
    first_number = e.get()
    global F_num
    global math
    math = 'remainder'
    F_num = float(first_number)
    e.delete(0, END)


# sqrt function to get the square root of a number
def sqrt():
    first_number = e.get()
    to_be_sqrt = float(first_number)
    e.delete(0, END)
    e.insert(0, to_be_sqrt ** 0.5)
    e.get()


# squared function get the square of a number
def squared():
    first_number = e.get()
    to_be_squared = float(first_number)
    e.delete(0, END)
    e.insert(0, to_be_squared ** 2)
    e.get()


# tripled function to get a the number raised to the power of 3
def tripled():
    first_number = e.get()
    to_be_trippled = float(first_number)
    e.delete(0, END)
    e.insert(0, to_be_trippled ** 3)
    e.get()


# power function to get the power of a specific number
def power():
    first_number = e.get()
    global F_num
    global math
    math = 'power'
    F_num = float(first_number)
    e.delete(0, END)


# log function to get the log of a number
def log():
    first_number = e.get()
    to_be_logged = float(first_number)
    e.delete(0, END)
    e.insert(0, math.log(to_be_logged))
    e.get()


# factorial function to get the factorial of a number
def factorial():
    first_number = e.get()
    to_be_factorized = float(first_number)
    e.delete(0, END)
    e.insert(0, math.factorial(to_be_factorized))
    e.get()


# exponential_log function to get the exponetial log of a number
def exponential_log():
    first_number = e.get()
    to_be_lenned = float(first_number)
    e.delete(0, END)
    e.insert(0, math.log(to_be_lenned, math.e))
    e.get()


# sin function to add to get the sin of a number
def sin():
    first_number = e.get()
    to_be_sined = float(first_number)
    e.delete(0, END)
    e.insert(0, math.sin(math.radians(to_be_sined)))
    e.get()


# cos function to get the cos of a number
def cos():
    first_number = e.get()
    to_be_cosined = float(first_number)
    e.delete(0, END)
    e.insert(0, math.cos(math.radians(to_be_cosined)))
    e.get()


# tan function to get the tan of a number
def tan():
    first_number = e.get()
    to_be_tanned = float(first_number)
    e.delete(0, END)
    e.insert(0, math.tan(math.radians(to_be_tanned)))
    e.get()


# cot function to get the cot of a number
def cot():
    first_number = e.get()
    to_be_cottaned = float(first_number)
    e.delete(0, END)
    e.insert(0, 1 / (math.tan(math.radians(to_be_cottaned))))
    e.get()


# sec function get the sec of a number
def sec():
    first_number = e.get()
    to_be_secced = float(first_number)
    e.delete(0, END)
    e.insert(0, 1 / (math.cos(math.radians(to_be_secced))))
    e.get()


# csc function get the csc of a number
def csc():
    first_number = e.get()
    to_be_csced = float(first_number)
    e.delete(0, END)
    e.insert(0, 1 / (math.sin(math.radians(to_be_csced))))
    e.get()


# rad2degree function converts rad to degree
def rad2degree():
    first_number = e.get()
    to_be_converted2rad = float(first_number)
    e.delete(0, END)
    e.insert(0, (math.radians(to_be_converted2rad)))
    e.get()


# degree2rad function converts degree to rad
def degree2rad():
    first_number = e.get()
    to_be_converted2degree = float(first_number)
    e.delete(0, END)
    e.insert(0, (math.degrees(to_be_converted2degree)))
    e.get()


# equal function do a specific functionn according to the pressed button
def equal():
    second_num = float(e.get())
    e.delete(0, END)
    if math == 'addition':
        e.insert(0, F_num + second_num)
    elif math == 'subtraction':
        e.insert(0, F_num - second_num)
    elif math == 'multiply':
        e.insert(0, F_num * second_num)
    elif math == 'divide':
        e.insert(0, F_num / second_num)
    elif math == 'remainder':
        e.insert(0, F_num % second_num)
    elif math == 'power':
        e.insert(0, F_num ** second_num)


# -------------------------------------------------------------------------------------------------------

# All script Labels

# adding the label of Enter First degree Equation variables
plot_label = Label(root, text='Enter First degree Equation variables', bg="#303030", fg='white',
                   font="Georgia 13 italic ")
plot_label.grid(row=0, column=7, ipadx=10, ipady=10, sticky="nsew")

# adding the label of Enter Second degree Equation variables
plot_label2 = Label(root, text='Enter Second degree Equation variables', bg="#303030", fg='white',
                    font="Georgia 13 italic ")
plot_label2.grid(row=0, column=10, ipadx=10, ipady=10, sticky="nsew")

# adding the label of Solving the Equation
Solver_label = Label(root, text='Solving the Equation', bg="#303030", fg='white', font="Georgia 15 italic ")
Solver_label.grid(row=3, column=7, ipadx=10, ipady=10, sticky="nsew")

# -------------------------------------------------------------------------------------------------------

# All Script Entry box

# building the main entry box in the screen and specifying its location on the screen
e = Entry(root, relief=RIDGE, bd=10, font=("Arial", 15), bg="black", fg='white')
e.grid(row=0, column=0, columnspan=4, ipadx=10, ipady=10, sticky="nsew")

# building the entry boxes for solving first degree equation and specifying its location on the screen
x_first1 = Entry(root, relief=RIDGE, bd=10, font=("Arial", 15), bg="black", fg='white')
x_first1.grid(row=1, column=7, columnspan=1, sticky="nsew")

xconstant1 = Entry(root, relief=RIDGE, bd=10, font=("Arial", 15), bg="black", fg='white')
xconstant1.grid(row=2, column=7, columnspan=1, sticky="nsew")

# building the entry boxes for solving first degree equation and specifying its location on the screen
x_squared2 = Entry(root, relief=RIDGE, bd=10, font=("Arial", 15), bg="black", fg='white')
x_squared2.grid(row=1, column=10, columnspan=1, sticky="nsew")

x_first2 = Entry(root, relief=RIDGE, bd=7, font=("Arial", 15), bg="black", fg='white')
x_first2.grid(row=2, column=10, columnspan=1, sticky="nsew")

xconstant2 = Entry(root, relief=RIDGE, bg="black", fg='white', bd=7, font=("Arial", 15))
xconstant2.grid(row=3, column=10, columnspan=1, sticky="nsew")

# building the entry boxes for displaying the solution of the equations and specifying its location on the screen
roots_of_equation = Entry(root, relief=RIDGE, bd=7, font=("Arial", 15), bg="black", fg='white')
roots_of_equation.grid(row=4, column=7, columnspan=3, rowspan=2, sticky="nsew")

# ----------------------------------------------------------------------------------------------------------


# creating buttons
button1 = Button(text='1', padx=40, pady=19, bg="#303030", fg='white', font=('Arial', 12), activeforeground='white',
                 activebackground='grey', command=lambda: button_click(1))
button2 = Button(text='2', padx=40, pady=19, bg="#303030", fg='white', font=('Arial', 12), activeforeground='white',
                 activebackground='grey', command=lambda: button_click(2))
button3 = Button(text='3', padx=40, pady=19, bg="#303030", fg='white', font=('Arial', 12), activeforeground='white',
                 activebackground='grey', command=lambda: button_click(3))
button4 = Button(text='4', padx=40, pady=19, bg="#303030", fg='white', font=('Arial', 12), activeforeground='white',
                 activebackground='grey', command=lambda: button_click(4))
button5 = Button(text='5', padx=40, pady=19, bg="#303030", fg='white', font=('Arial', 12), activeforeground='white',
                 activebackground='grey', command=lambda: button_click(5))
button6 = Button(text='6', padx=40, pady=19, bg="#303030", fg='white', font=('Arial', 12), activeforeground='white',
                 activebackground='grey', command=lambda: button_click(6))
button7 = Button(text='7', padx=40, pady=19, bg="#303030", fg='white', font=('Arial', 12), activeforeground='white',
                 activebackground='grey', command=lambda: button_click(7))
button8 = Button(text='8', padx=40, pady=19, bg="#303030", fg='white', font=('Arial', 12), activeforeground='white',
                 activebackground='grey', command=lambda: button_click(8))
button9 = Button(text='9', padx=40, pady=19, bg="#303030", fg='white', font=('Arial', 12), activeforeground='white',
                 activebackground='grey', command=lambda: button_click(9))
button0 = Button(text='0', padx=40, pady=19, bg="#303030", fg='white', font=('Arial', 12), activeforeground='white',
                 activebackground='grey', command=lambda: button_click(0))
button_dot = Button(text='.', padx=40, pady=19, bg="#303030", fg='white', font=('Arial', 12),
                    activeforeground='white', activebackground='grey', command = lambda: button_click('.'))

button_reminder = Button(text='%', padx=40, pady=19, bg="#303030", fg='white', font=('Arial', 12),
                         activeforeground='white', command=remain)
button_clear = Button(text='AC', padx=40, pady=19, bg="#303030", fg='white', font=('Arial', 12),
                      activeforeground='white', command=clear)
button_differential = Button(text='Solve 1st degree differential', padx=26, pady=19, bg="#FF9912", fg='black',
                             font="Georgia 15 italic ", activeforeground='white', activebackground='grey',
                             command=defrentiate)

button_Minus = Button(font=10, text='-', padx=40, pady=19, bg="#FF9912", command=substract)
button_Add = Button(font=10, text='+', padx=40, pady=19, bg="#FF9912", command=add)
button_equal = Button(font=10, text='=', padx=40, pady=19, bg="#FF9912", command=equal)
button_multiply = Button(font=10, text='×', padx=40, pady=19, bg="#FF9912", command=multiply)
button_division = Button(font=10, text='÷', padx=41, pady=19, bg="#FF9912", command=divide)

button_squared = Button(text='x²', padx=40, pady=19, bg="#303030", fg='white', font=('Arial', 12),
                        activeforeground='white', activebackground='grey', command=squared)
button_tripled = Button(text='(x^3)', padx=40, pady=19, bg="#303030", fg='white', font=('Arial', 12),
                        activeforeground='white', activebackground='grey', command=tripled)
button_sqrt = Button(text='√', padx=40, pady=19, bg="#303030", fg='white', font=('Arial', 12),
                     activeforeground='white', activebackground='grey', command=sqrt)
button_power = Button(text='aⁿ', padx=40, pady=19, bg="#303030", fg='white', font=('Arial', 12),
                      activeforeground='white', activebackground='grey', command=power)
button_log = Button(text='log', padx=40, pady=19, bg="#303030", fg='white', font=('Arial', 12),
                    activeforeground='white', activebackground='grey', command=log)
button_ln = Button(text='ln', padx=40, pady=19, bg="#303030", fg='white', font=('Arial', 12),
                   activeforeground='white', activebackground='grey', command=exponential_log)
button_factorial = Button(text='!', padx=40, pady=19, bg="#303030", fg='white', font=('Arial', 12),
                          activeforeground='white', activebackground='grey', command=factorial)
button_sin = Button(text='sin', padx=40, pady=19, bg="#303030", fg='white', font=('Arial', 12),
                    activeforeground='white', activebackground='grey', command=sin)
button_cos = Button(text='cos', padx=40, pady=19, bg="#303030", fg='white', font=('Arial', 12),
                    activeforeground='white', activebackground='grey', command=cos)
button_tan = Button(text='tan', padx=40, pady=19, bg="#303030", fg='white', font=('Arial', 12),
                    activeforeground='white', activebackground='grey', command=tan)
button_cot = Button(text='cot', padx=40, pady=19, bg="#303030", fg='white', font=('Arial', 12),
                    activeforeground='white', activebackground='grey', command=cot)
button_sec = Button(text='sec', padx=40, pady=19, bg="#303030", fg='white', font=('Arial', 12),
                    activeforeground='white', activebackground='grey', command=sec)
button_csc = Button(text='csc', padx=40, pady=19, bg="#303030", fg='white', font=('Arial', 12),
                    activeforeground='white', activebackground='grey', command=csc)
button_degree2rad = Button(text='π°', padx=40, pady=19, bg="#303030", fg='white', font=('Arial', 12),
                           activeforeground='white', activebackground='grey', command=rad2degree)
button_rad2degree = Button(text='(°)', padx=40, pady=19, bg="#303030", fg='white', font=('Arial', 12),
                           activeforeground='white', activebackground='grey', command=degree2rad)

# plot buttons to graph the equations

# plot1 button to graph the first degree equation
button_plot1 = Button(text='Graph 1st Deg eq', padx=40, pady=20, bg="#303030", fg='white',
                      font="Georgia 15 italic ", activeforeground='white', command=lambda: [plot1(), solver1()])
# plot1 button to graph the second degree equation
button_plot2 = Button(text='Graph 2nd Deg eq', padx=40, pady=20, bg="#303030", fg='white',
                      font="Georgia 15 italic ", activeforeground='white', command=lambda: [plot2(), solver2()])

# specifying buttons locations on the screan
button7.grid(row=2, column=0, sticky="nsew")
button8.grid(row=2, column=1, sticky="nsew")
button9.grid(row=2, column=2, sticky="nsew")

button4.grid(row=3, column=0, sticky="nsew")
button5.grid(row=3, column=1, sticky="nsew")
button6.grid(row=3, column=2, sticky="nsew")

button1.grid(row=4, column=0, sticky="nsew")
button2.grid(row=4, column=1, sticky="nsew")
button3.grid(row=4, column=2, sticky="nsew")

button0.grid(row=5, column=0, columnspan=2, sticky="nsew")
button_dot.grid(row=5, column=2, sticky="nsew")

button_Add.grid(row=4, column=3, sticky="nsew")
button_Minus.grid(row=3, column=3, sticky="nsew")
button_clear.grid(row=1, column=0, columnspan=2, sticky="nsew")
button_differential.grid(row=0, column=4, columnspan=3, sticky="nsew")
button_equal.grid(row=5, column=3, sticky="nsew")

button_multiply.grid(row=2, column=3, sticky="nsew")
button_division.grid(row=1, column=3, sticky="nsew")
button_reminder.grid(row=1, column=2, sticky="nsew")

button_sin.grid(row=5, column=4, sticky="nsew")
button_cos.grid(row=5, column=5, sticky="nsew")
button_tan.grid(row=5, column=6, sticky="nsew")

button_cot.grid(row=4, column=4, sticky="nsew")
button_sec.grid(row=4, column=5, sticky="nsew")
button_csc.grid(row=4, column=6, sticky="nsew")

button_log.grid(row=3, column=4, sticky="nsew")
button_ln.grid(row=3, column=5, sticky="nsew")
button_factorial.grid(row=3, column=6, sticky="nsew")

button_sqrt.grid(row=2, column=4, sticky="nsew")
button_squared.grid(row=2, column=5, sticky="nsew")
button_tripled.grid(row=1, column=6, sticky="nsew")
button_power.grid(row=2, column=6, sticky="nsew")

button_rad2degree.grid(row=1, column=4, sticky="nsew")
button_degree2rad.grid(row=1, column=5, sticky="nsew")

button_plot1.grid(row=4, column=10, sticky="nsew")
button_plot2.grid(row=5, column=10, sticky="nsew")


def window():
    root.mainloop()
