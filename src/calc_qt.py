#!/usr/bin/env python

#pip install PyQt5

from PyQt5 import QtWidgets, uic, Qt, QtCore
from calc import *
import sys
import os

class Ui(QtWidgets.QMainWindow):
	def __init__(self):
		super(Ui, self).__init__()

		# Get relative path to this script, idk if this is the best way to do it though
		dir_path = os.path.dirname(os.path.realpath(__file__))
		uic.loadUi(dir_path + r'\res\calc.ui', self)

		# NUMBERS
		self.n1.clicked.connect(self.n1Pressed)
		self.n2.clicked.connect(self.n2Pressed)
		self.n3.clicked.connect(self.n3Pressed)
		self.n4.clicked.connect(self.n4Pressed)
		self.n5.clicked.connect(self.n5Pressed)
		self.n6.clicked.connect(self.n6Pressed)
		self.n7.clicked.connect(self.n7Pressed)
		self.n8.clicked.connect(self.n8Pressed)
		self.n9.clicked.connect(self.n9Pressed)
		self.n0.clicked.connect(self.n0Pressed)

		# MISC
		self.dot.clicked.connect(self.dotPressed)
		self.zero.clicked.connect(self.zeroPressed)
		self.switchSign.clicked.connect(self.switchSignPressed)
		self.deleteLast.clicked.connect(self.deleteLastPressed)

		# OPERATIONS
		self.mAdd.clicked.connect(self.mAddPressed)
		self.mMul.clicked.connect(self.mMulPressed)
		self.mSub.clicked.connect(self.mSubPressed)
		self.mDiv.clicked.connect(self.mDivPressed)
		self.mSquared.clicked.connect(self.mSquaredPressed)
		self.mSqrt.clicked.connect(self.mSqrtPressed)
		self.mFactorial.clicked.connect(self.mFactorialPressed)
		self.mPower.clicked.connect(self.mPowerPressed)
		self.mRoot.clicked.connect(self.mRootPressed)
		self.mPrime.clicked.connect(self.mPrimePressed)
		self.result.clicked.connect(self.resultPressed)
		self.clear.clicked.connect(self.pclearPressed)

		# VARIABLES
		self.display = "0"
		self.prevDisplay = ""
		self.answer = 0
		self.equalsLast = False
		self.cleared = True
		self.decimal = False
		self.unaryLast = False
		self.symbol = ""
		self.first = 0
		self.second = 0
		self.operation = False
		self.screen.setText("0")
		self.prevScreen.setText("")

		self.show()

	def keyPressEvent(self, event):
		if event.key() == QtCore.Qt.Key_1:
			self.n1Pressed()
		elif event.key() == QtCore.Qt.Key_2:
			self.n2Pressed()
		elif event.key() == QtCore.Qt.Key_3:
			self.n3Pressed()
		elif event.key() == QtCore.Qt.Key_4:
			self.n4Pressed()
		elif event.key() == QtCore.Qt.Key_5:
			self.n5Pressed()
		elif event.key() == QtCore.Qt.Key_6:
			self.n6Pressed()
		elif event.key() == QtCore.Qt.Key_7:
			self.n7Pressed()
		elif event.key() == QtCore.Qt.Key_8:
			self.n8Pressed()
		elif event.key() == QtCore.Qt.Key_9:
			self.n9Pressed()
		elif event.key() == QtCore.Qt.Key_0:
			self.n0Pressed()
		elif event.key() == QtCore.Qt.Key_0:
			self.n0Pressed()
		elif event.key() == QtCore.Qt.Key_Plus:
			self.mAddPressed()
		elif event.key() == QtCore.Qt.Key_Minus:
			self.mSubPressed()
		elif event.key() == QtCore.Qt.Key_Asterisk:
			self.mMulPressed()
		elif event.key() == QtCore.Qt.Key_Slash:
			self.mDivPressed()
		elif event.key() == QtCore.Qt.Key_Enter:
			self.resultPressed()
		elif event.key() == QtCore.Qt.Key_Return:
			self.resultPressed()
		elif event.key() == QtCore.Qt.Key_Backspace:
			self.deleteLastPressed()
		elif event.key() == QtCore.Qt.Key_Delete:
			self.pclearPressed()
		elif event.key() == QtCore.Qt.Key_Shift:
			self.switchSignPressed()
		elif event.key() == QtCore.Qt.Key_Period:
			self.dotPressed()
		else:
			super(Ui, self).keyPressEvent(event)
		#event.accept()

	def nPrint(self, value):
		if self.cleared:
			self.display = value
			self.cleared = False
		else:
			self.display += value
		if abs(float(self.display)) > 10 ** 12:
			self.screen.setText("{:e}".format(float(self.display)))
		else:
			self.screen.setText(self.display)

	def binaryOperation(self, operation, symbol):
		self.unaryLast = False
		self.first = float(self.display)
		if self.first.is_integer():
			self.first = int(self.first)
		if abs(self.first) > 10 ** 12:
			self.prevDisplay = "{:e}".format(self.first) + symbol
		else:
			self.prevDisplay = str(self.first) + symbol
		self.symbol = symbol
		self.zeroPressed()
		self.operation = operation
		self.prevScreen.setText(self.prevDisplay)
		self.equalsLast = False

	def unaryOperation(self, operation, symbol, lastUnaryOperation):
		if not self.equalsLast:
			self.resultPressed()

		self.unaryLast = lastUnaryOperation
		self.first = float(self.display)
		if self.first.is_integer():
			self.first = int(self.first)

		if abs(self.first) > 10 ** 12:
			self.prevDisplay = symbol + "(" + "{:e}".format(self.first) + ")"
		else:
			self.prevDisplay = symbol + "(" + str(self.first) + ")"

		self.symbol = symbol
		self.zeroPressed()
		self.operation = operation
		self.prevScreen.setText(self.prevDisplay)

		try:
			self.answer = self.operation(self.first)
		except ValueError as e:
			self.cleared = True
			self.decimal = False
			self.display = "0"
			self.screen.setText("ERROR: " + str(e))
			self.operation = False
			self.unaryLast = False
			self.first = 0
			self.second = 0
			return

		if isinstance(self.answer, float):
			if self.answer.is_integer():
				self.answer = int(self.answer)

		self.prevScreen.setText(self.prevDisplay)
		self.equalsLast = True
		# TODO: define upper limit on answers
		if abs(self.answer) > 10 ** 12:
			self.display = "{:e}".format(self.answer)
		else:
			self.display = str(self.answer)
		self.cleared = True
		self.decimal = False
		self.first = self.answer
		self.screen.setText(self.display)

	def n1Pressed(self):
		self.nPrint("1")
	
	def n2Pressed(self):
		self.nPrint("2")

	def n3Pressed(self):
		self.nPrint("3")

	def n4Pressed(self):
		self.nPrint("4")

	def n5Pressed(self):
		self.nPrint("5")

	def n6Pressed(self):
		self.nPrint("6")

	def n7Pressed(self):
		self.nPrint("7")

	def n8Pressed(self):
		self.nPrint("8")

	def n9Pressed(self):
		self.nPrint("9")

	def n0Pressed(self):
		self.nPrint("0")

	def dotPressed(self):
		if self.cleared:
			self.display = "0"
		if self.decimal == False:
			self.display += "."
			self.decimal = True
			self.cleared = False
			self.screen.setText(self.display)

	def zeroPressed(self):
		self.display = "0"
		self.cleared = True
		self.decimal = False
		self.screen.setText(self.display)

	def switchSignPressed(self):
		if self.display[0] == "-":
			self.display = self.display[1 : : ]
			if abs(float(self.display)) > 10 ** 12:
				self.screen.setText("{:e}".format(float(self.display)))
			else:
				self.screen.setText(self.display)
		else:
			self.display = "-" + self.display
			if abs(float(self.display)) > 10 ** 12:
				self.screen.setText("{:e}".format(float(self.display)))
			else:
				self.screen.setText(self.display)

	def deleteLastPressed(self):
		self.cleared = True
		self.decimal = False
		if len(self.display) == 2:
			if self.display[0] == "-":
				self.display = "0"
			else:
				self.display = self.display[:-1]
			self.screen.setText(self.display)
		elif len(self.display) == 1:
			self.display = "0"
			self.screen.setText(self.display)
		else:
			self.display = self.display[:-1]
			self.screen.setText(self.display)

	def mAddPressed(self):
		self.binaryOperation(add, "+")
	
	def mMulPressed(self):
		self.binaryOperation(multiply, "*")

	def mSubPressed(self):
		self.binaryOperation(subtract, "-")

	def mDivPressed(self):
		self.binaryOperation(divide, "/")

	def mPowerPressed(self):
		self.binaryOperation(to_the_power_of, "^")

	def mRootPressed(self):
		#self.binaryOperation(root, "√")
		self.unaryLast = False
		self.first = float(self.display)
		if self.first.is_integer():
			self.first = int(self.first)
		if abs(self.first > 10 ** 12):
			self.prevDisplay = "√" + "{:e}".format(self.first)
		else:
			self.prevDisplay = "√" + str(self.first)
		self.symbol = "√"
		self.zeroPressed()
		self.operation = root
		self.prevScreen.setText(self.prevDisplay)
		self.equalsLast = False

	def mSquaredPressed(self):
		self.unaryOperation(to_the_power_of, "squared", self.mSquaredPressed)

	def mSqrtPressed(self):
		self.unaryOperation(root, "sqrt", self.mSqrtPressed)

	def mFactorialPressed(self):
		self.unaryOperation(factorial, "fact", self.mFactorialPressed)

	def mPrimePressed(self):
		if not self.equalsLast:
			self.resultPressed()

		self.unaryLast = self.mPrimePressed
		self.first = float(self.display)
		if self.first.is_integer():
			self.first = int(self.first)
		self.prevDisplay = "Prime" + "(" + str(self.first) + ")"
		self.symbol = "Prime"
		self.zeroPressed()
		self.operation = prime
		self.prevScreen.setText(self.prevDisplay)

		try:
			self.answer = self.operation(self.first)
		except ValueError as e:
			self.cleared = True
			self.decimal = False
			self.display = "0"
			self.screen.setText("ERROR: " + str(e))
			self.operation = False
			self.unaryLast = False
			self.first = 0
			self.second = 0
			return

		if self.answer:
			self.answer = 1
		else:
			self.answer = 0

		self.prevScreen.setText(self.prevDisplay)
		self.equalsLast = True
		self.display = str(self.answer)
		self.cleared = True
		self.decimal = False
		self.first = self.answer
		self.screen.setText(self.display)

	def resultPressed(self):
		if self.unaryLast != False:
			self.unaryLast()
			return
		if self.operation:
			if self.equalsLast:
				self.prevDisplay = str(self.answer) + self.symbol
			else:
				self.second = float(self.display)
				if self.second.is_integer():
					self.second = int(self.second)

			try:
				self.answer = self.operation(self.first, self.second)
			except ValueError as e:
				self.cleared = True
				self.decimal = False
				self.display = "0"
				self.screen.setText("ERROR: " + str(e))
				self.operation = False
				self.unaryLast = False
				self.first = 0
				self.second = 0
				return

			if isinstance(self.answer, float):
				if self.answer.is_integer():
					self.answer = int(self.answer)

			if self.operation == root:
				if abs(self.second) > 10 ** 12:
					self.prevDisplay = "{:e}".format(self.second) + self.prevDisplay
				else:
					self.prevDisplay = str(self.second) + self.prevDisplay
			else:
				if abs(self.second) > 10 ** 12:
					self.prevDisplay += "{:e}".format(self.second)
				else:
					self.prevDisplay += str(self.second)

			self.prevScreen.setText(self.prevDisplay)
			self.equalsLast = True
			if abs(self.answer) > 10 ** 12:
				self.display = "{:e}".format(self.answer)
			else:
				self.display = str(self.answer)
			self.cleared = True
			self.decimal = False
			self.first = self.answer
			self.screen.setText(self.display)

	def pclearPressed(self):
		self.prevDisplay = ""
		self.prevScreen.setText(self.prevDisplay)
		self.display = "0"
		self.first = 0
		self.second = False
		self.equalsLast = False
		self.operation = False
		self.cleared = True
		self.unaryLast = False
		self.decimal = False
		self.screen.setText(self.display)

app = QtWidgets.QApplication(sys.argv)
window = Ui()
window.setFixedSize(window.size())
app.exec_()
