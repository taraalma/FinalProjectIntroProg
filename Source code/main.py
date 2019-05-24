from tkinter import *
import random
import time
from thermostat import *

oddNon = 0

tk = Tk()
tk.title("Monitor")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas = Canvas(tk, width = 500, height = 500, bd = 0, highlightthickness = 0, background = '#FFFFFF')
canvas.pack()
tk.update()

class Gradient:
	
	IsObjectHidden = 0
	
	def __init__(self, canvas, xStartval, yStartval, xFinVal, yFinVal, x):
		
		self.xStartingValue  = xStartval
		self.yStartingValue  = yStartval
		self.xFinalValue 	 = xFinVal
		self.yFinalValue 	 = yFinVal
		self.GradientColor	 = x
		
		self.draw(canvas)
		
	def draw(self, canvas):
		global arrayColores
		
		gradientObjectColor = str(arrayColores[32 - self.GradientColor])
		self.canvas = canvas
		if (self.IsObjectHidden == 0):
			self.id = canvas.create_rectangle(self.xStartingValue, self.yStartingValue, self.xFinalValue, self.yFinalValue, width=5 , fill=gradientObjectColor,outline=gradientObjectColor)
		else:
			self.id = canvas.create_rectangle(self.xStartingValue, self.yStartingValue, self.xFinalValue, self.yFinalValue, width=5 , fill='#FFFFFF',outline='#FFFFFF')

xWidth = 40

Gradient0 = Gradient (canvas,0,0,xWidth,4,31)
Gradient1 = Gradient (canvas,0,4,xWidth,8,30)
Gradient2 = Gradient (canvas,0,8,xWidth,12,29)
Gradient3 = Gradient (canvas,0,12,xWidth,16,28)
Gradient4 = Gradient (canvas,0,16,xWidth,20,27)
Gradient5 = Gradient (canvas,0,20,xWidth,24,26)
Gradient6 = Gradient (canvas,0,24,xWidth,28,25)
Gradient7 = Gradient (canvas,0,28,xWidth,32,24)
Gradient8 = Gradient (canvas,0,32,xWidth,36,23)
Gradient9 = Gradient (canvas,0,36,xWidth,40,22)
Gradient10 = Gradient (canvas,0,40,xWidth,44,21)
Gradient11 = Gradient (canvas,0,44,xWidth,48,20)
Gradient12 = Gradient (canvas,0,48,xWidth,52,19)
Gradient13 = Gradient (canvas,0,52,xWidth,56,18)
Gradient14 = Gradient (canvas,0,56,xWidth,60,17)
Gradient15 = Gradient (canvas,0,60,xWidth,64,16)
Gradient16 = Gradient (canvas,0,64,xWidth,68,15)
Gradient17 = Gradient (canvas,0,68,xWidth,72,14)
Gradient18 = Gradient (canvas,0,72,xWidth,76,13)
Gradient19 = Gradient (canvas,0,76,xWidth,80,12)
Gradient20 = Gradient (canvas,0,80,xWidth,84,11)
Gradient21 = Gradient (canvas,0,84,xWidth,88,10)
Gradient22 = Gradient (canvas,0,88,xWidth,92,9)
Gradient23 = Gradient (canvas,0,92,xWidth,96,8)
Gradient24 = Gradient (canvas,0,96,xWidth,100,7)
Gradient25 = Gradient (canvas,0,100,xWidth,104,6)
Gradient26 = Gradient (canvas,0,104,xWidth,108,5)
Gradient27 = Gradient (canvas,0,108,xWidth,112,4)
Gradient28 = Gradient (canvas,0,112,xWidth,116,3)
Gradient29 = Gradient (canvas,0,116,xWidth,120,2)
Gradient30 = Gradient (canvas,0,120,xWidth,124,1)
Gradient31 = Gradient (canvas,0,124,xWidth,128,0)



while 1:
	global oddNon
	
	if (oddNon == 0):
		tk.update_idletasks()
		tk.update()
		time.sleep(1)
		oddNon = 1
	if ( oddNon == 1):
		tk.update_idletasks()
		tk.update()
		time.sleep(1)
		oddNon = 0


