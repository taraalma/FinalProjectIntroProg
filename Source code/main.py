from tkinter import *
import random
import time
from thermostat import *

oddNon = 0
GradientList = []
xWidth = 40

# Start program
tk = Tk()
tk.title("Monitor for sensor stuff")

# Insert frame
frame = Frame(tk)
frame.grid(row=0,column=0, sticky="n")

# Insert canvas for the temperature gradient
canvas = Canvas(tk, width = (xWidth + 0), height = 150, bd = 0, highlightthickness = 0, bg = '#F0F0F0')
canvas.grid(row=0,column=0)

# Insert label for temperature
labelSpace0=Label(frame, text=" ",height=11,width=10).grid(row=1,column=0)

label0=Label( frame, text="      Temp:", anchor= SE,bg='#F0F0F0').grid(row=2,column=0, sticky="W")

tk.update()

# Initialize gradients in a list
# the variable xWidth is used to determine the width of each gradient.

GradientList.append(Gradient(canvas,0,0,xWidth,4,31))
GradientList.append(Gradient(canvas,0,4,xWidth,8,30))
GradientList.append(Gradient(canvas,0,8,xWidth,12,29))
GradientList.append(Gradient(canvas,0,12,xWidth,16,28))
GradientList.append(Gradient(canvas,0,16,xWidth,20,27))
GradientList.append(Gradient(canvas,0,20,xWidth,24,26))
GradientList.append(Gradient(canvas,0,24,xWidth,28,25))
GradientList.append(Gradient(canvas,0,28,xWidth,32,24))
GradientList.append(Gradient(canvas,0,32,xWidth,36,23))
GradientList.append(Gradient(canvas,0,36,xWidth,40,22))
GradientList.append(Gradient(canvas,0,40,xWidth,44,21))
GradientList.append(Gradient(canvas,0,44,xWidth,48,20))
GradientList.append(Gradient(canvas,0,48,xWidth,52,19))
GradientList.append(Gradient(canvas,0,52,xWidth,56,18))
GradientList.append(Gradient(canvas,0,56,xWidth,60,17))
GradientList.append(Gradient(canvas,0,60,xWidth,64,16))
GradientList.append(Gradient(canvas,0,64,xWidth,68,15))
GradientList.append(Gradient(canvas,0,68,xWidth,72,14))
GradientList.append(Gradient(canvas,0,72,xWidth,76,13))
GradientList.append(Gradient(canvas,0,76,xWidth,80,12))
GradientList.append(Gradient(canvas,0,80,xWidth,84,11))
GradientList.append(Gradient(canvas,0,84,xWidth,88,10))
GradientList.append(Gradient(canvas,0,88,xWidth,92,9))
GradientList.append(Gradient(canvas,0,92,xWidth,96,8))
GradientList.append(Gradient(canvas,0,96,xWidth,100,7))
GradientList.append(Gradient(canvas,0,100,xWidth,104,6))
GradientList.append(Gradient(canvas,0,104,xWidth,108,5))
GradientList.append(Gradient(canvas,0,108,xWidth,112,4))
GradientList.append(Gradient(canvas,0,112,xWidth,116,3))
GradientList.append(Gradient(canvas,0,116,xWidth,120,2))
GradientList.append(Gradient(canvas,0,120,xWidth,124,1))
GradientList.append(Gradient(canvas,0,124,xWidth,128,0))

maxAmount = 1

for y in range (0,32):
	GradientList[(31-y)].IsObjectHidden = 1
	GradientList[(31-y)].draw(canvas)
tk.update_idletasks()
tk.update()

while 1:
	
	maxAmount = maxAmount + 1
	
	if ( maxAmount == 32 ):
		maxAmount = 0
		for y in range (0,32):
			GradientList[(31-y)].IsObjectHidden = 1
			GradientList[(31-y)].draw(canvas)
		
		
	for y in range (0,maxAmount):
		GradientList[(31-y)].IsObjectHidden = 0
		GradientList[(31-y)].draw(canvas)
	
	tk.update_idletasks()
	tk.update()
	time.sleep(0.1)
	
