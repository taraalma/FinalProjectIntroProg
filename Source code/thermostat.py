# array for each color of the gradient
gradientList = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

# colors for each gradient.
arrayColores = ['#E50000','#DD0008','#D60010','#CE0018','#C70020','#C00029','#B80031','#B10039','#A90041','#A2004A','#9B0052','#93005A','#8C0062','#84006A','#7D0073','#76007B','#6E0083','#67008B','#600094','#58009C','#5100A4','#4900AC','#4200B4','#3B00BD','#3300C5','#2C00CD','#2400D5','#1D00DE','#1600E6','#0E00EE','#0700F6','#0000FF','#FFFFFF']

COLUMN_0 = 0
COLUMN_1 = 1
COLUMN_2 = 2
COLUMN_3 = 3
COLUMN_4 = 4
COLUMN_5 = 5
COLUMN_6 = 6
COLUMN_7 = 7
COLUMN_8 = 8
COLUMN_9 = 9

ROW_0 = 0
ROW_1 = 1
ROW_2 = 2
ROW_3 = 3
ROW_4 = 4
ROW_5 = 5
ROW_6 = 6
ROW_7 = 7
ROW_8 = 8
ROW_9 = 9

# Gradient class for objects with different color.
class Gradient:
	
	IsObjectHidden = 0
	
	def __init__(self, canvas, xStartval, yStartval, xFinVal, yFinVal, x):
		
		self.xStartingValue  = xStartval
		self.yStartingValue  = yStartval
		self.xFinalValue 	 = xFinVal
		self.yFinalValue 	 = yFinVal
		self.GradientColor	 = x
		self.container		 = None
		self.draw(canvas)
		
	def draw(self, canvas):
		global arrayColores
		
		gradientObjectColor = str(arrayColores[32 - self.GradientColor])
		self.canvas = canvas
		if (self.IsObjectHidden == 0):
			self.id = canvas.create_rectangle(self.xStartingValue, self.yStartingValue, self.xFinalValue, self.yFinalValue, width=5 , fill=gradientObjectColor,outline=gradientObjectColor)
		else:
			self.id = canvas.create_rectangle(self.xStartingValue, self.yStartingValue, self.xFinalValue, self.yFinalValue, width=5 , fill='#F0F0F0',outline='#F0F0F0')
	def __del__(self):
		pass