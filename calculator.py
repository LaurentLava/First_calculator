##################################################
## First attempt to do a calculator with the Tkinter
## module.
##################################################
## Free of use and copy
##################################################
## Author: Laurent Lava
## Credits: [https://www.geeksforgeeks.org/python-simple-gui-calculator-using-tkinter/]
## Version: 0.0.1
## Mmaintainer: Laurent Lava
## Email: laurentlava04[at]gmail.com
## Status: can be improved :)
##################################################


###############
## Libraries ##
###############


from tkinter import *	


###############
## Variables ##
###############


TITLE = "Custom calculator"
WIDTH = 280
HEIGHT = 411
GEOMETRY = str(WIDTH) + "x" + str(HEIGHT)
LIGHT_BLACK = "#262525"
BLACK = "#000000"
SILVER = "#A5A2A2"
ORANGE = "#FBA92A"
WHITE = "#000000"
expression = ""


###############
## Functions ##
###############

def initialize_gui(gui):
	"""
	This functions initializes all the buttons and fields
	we need for our calculator
	"""
	global to_display 

	to_display = StringVar() # used to show text

	# Computation of button width and height:
	button_width = 28 #int(WIDTH / 4)
	button_height = 4 #int(float(HEIGHT) / 6)

	# Set Label for output
	outputbox = Label(gui, textvariable=to_display , fg="white",
					bg = LIGHT_BLACK, anchor="e",
					height = button_height,
					width = button_width + 2)
	outputbox.config(font=(24))
	outputbox.grid(row=0, columnspan = 4) 

	to_display.set("")

	# Declare buttons
	# Clear button
	clear = Button(gui, text = "AC", fg = BLACK, bg = SILVER,
		command = clear_expression, height = button_height,
		width = button_width + 2)
	clear.grid(row = 2, columnspan = 4)

	button_width = int(button_width / 4)
	# 7 8 9
	number7 = Button(gui, text = '7', fg = BLACK, bg = SILVER,
		command = lambda: press(7), height = button_height,
		width = button_width)
	number7.grid(row = 3, column = 0)

	number8 = Button(gui, text = '8', fg = BLACK, bg = SILVER,
		command = lambda: press(8), height = button_height,
		width = button_width)
	number8.grid(row = 3, column = 1)

	number9 = Button(gui, text = '9', fg = BLACK, bg = SILVER,
		command = lambda: press(9), height = button_height,
		width = button_width)
	number9.grid(row = 3, column = 2)

	# 4 5 6
	number4 = Button(gui, text = '4', fg = BLACK, bg = SILVER,
		command = lambda: press(4), height = button_height,
		width = button_width)
	number4.grid(row = 4, column = 0)

	number5 = Button(gui, text = '5', fg = BLACK, bg = SILVER,
		command = lambda: press(5), height = button_height,
		width = button_width)
	number5.grid(row = 4, column = 1)

	number6 = Button(gui, text = '6', fg = BLACK, bg = SILVER,
		command = lambda: press(6), height = button_height,
		width = button_width)
	number6.grid(row = 4, column = 2)

	# 1 2 3
	number1 = Button(gui, text = '1', fg = BLACK, bg = SILVER,
		command = lambda: press(1), height = button_height,
		width = button_width)
	number1.grid(row = 5, column = 0)

	number2 = Button(gui, text = '2', fg = BLACK, bg = SILVER,
		command = lambda: press(2), height = button_height,
		width = button_width)
	number2.grid(row = 5, column = 1)

	number3 = Button(gui, text = '3', fg = BLACK, bg = SILVER,
		command = lambda: press(3), height = button_height,
		width = button_width)
	number3.grid(row = 5, column = 2)

	# Operations
	# + - * / = 0
	plus = Button(gui, text= "+", fg = WHITE, background = ORANGE,
		command = lambda: press('+'), height = button_height,
		width = button_width)
	plus.grid(row = 3, column = 3)

	minus = Button(gui, text= "-", fg = WHITE, bg = ORANGE,
		command = lambda: press('-'), height = button_height,
		width = button_width)
	minus.grid(row = 4, column = 3)

	times = Button(gui, text= "x", fg = WHITE, bg = ORANGE,
		command = lambda: press("*"), height = button_height,
		width = button_width)
	times.grid(row = 5, column = 3)

	divide = Button(gui, text = "/", fg = WHITE, bg = ORANGE,
		command = lambda: press('/'), height = button_height,
		width = button_width)
	divide.grid(row = 6, column = 3)

	equal = Button(gui, text = "=", fg = WHITE, bg = ORANGE,
		command = compute_expression, height = button_height,
		width = button_width)
	equal.grid(row = 6, column = 2)

	zero = Button(gui, text = "0", fg = BLACK, bg = SILVER,
		command = lambda: press('0'), height = button_height,
		width = button_width)
	zero.grid(row = 6, column = 0)

	decimal = Button(gui, text = ".", fg = BLACK, bg = SILVER,
		command = lambda: press('.'), height = button_height,
		width = button_width)
	decimal.grid(row = 6, column = 1)



def press(number):
	"""
	This function defines what happens when a user type a number
	or an opertation
	"""
	global to_display
	global expression
	expression += str(number) 

	to_display.set(expression)

def compute_expression():
	"""
	This function evaluates the expression entered by the user
	"""
	global to_display
	global expression

	try:
		total = str(eval(expression))
		expression = total
		to_display.set(total)

	except:
		expression = ""
		to_display.set("ERROR")


def clear_expression():
	"""
	This function clears the current expression and reset
	anything in memory
	"""

	global to_display
	global expression

	expression = ""
	to_display.set("")
	


def main():
	"""
	Main function
	"""
	# First create the GUI windows
	gui = Tk()

	# Set background color
	gui.configure(background = LIGHT_BLACK)

	# Set title 
	gui.title(TITLE)

	# Set geometry of window
	gui.geometry(GEOMETRY)

	# Fill windows with buttons and output field
	initialize_gui(gui)

	# Start gui
	gui.mainloop()
	

###############
## Main func ##
###############

if __name__ == "__main__":

	main()







