class Temp:
	def __init__(self):
		self.selectedTemp = 52
		self.selectedRange = 4
		self.currentTemp = 75
		self.power = False

	def setDesiredTemp(self, newTemp):
		self.desiredTemp = newTemp

	def setRange(self, newRange):
		self.tempRange = newRange

	def setPower(self, newPower):
		self.power = newPower