#!/usr/bin/env python

#pip install PyQt5

from PyQt5 import QtWidgets, uic, Qt
from calc import *
import sys
import os

class Ui(QtWidgets.QDialog):
	def __init__(self):
		super(Ui, self).__init__()

		# Get relative path to this script, idk if this is the best way to do it though
		dir_path = os.path.dirname(os.path.realpath(__file__))
		uic.loadUi(dir_path + r'\res\calc1.ui', self)
		self.screen = self.findChild(QtWidgets.QLabel, 'screen')
		self.opScreen = self.findChild(QtWidgets.QLabel, 'opScreen')

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

		# OPERATIONS
		self.mAdd.clicked.connect(self.mAddPressed)
		self.mMul.clicked.connect(self.mMulPressed)
		self.mSub.clicked.connect(self.mSubPressed)
		self.mDiv.clicked.connect(self.mDivPressed)
		self.result.clicked.connect(self.resultPressed)
		self.clear.clicked.connect(self.pclearPressed)

		# VARIABLES
		self.display = "0"
		self.cleared = True
		self.decimal = False
		self.first = 0
		self.second = 0
		self.operation = False
		self.screen.setText("0")
		self.opScreen.setText("")

		self.show()

	def nPrint(self, value):
		if self.cleared:
			self.display = value
			self.cleared = False
		else:
			self.display += value
		self.screen.setText(self.display)

	def binaryOperation(self, operation, symbol):
		self.first = float(self.display)
		self.zeroPressed()
		self.operation = operation
		self.opScreen.setText(symbol)

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

	def mAddPressed(self):
		self.binaryOperation(add, "+")
	
	def mMulPressed(self):
		self.binaryOperation(multiply, "*")

	def mSubPressed(self):
		self.binaryOperation(subtract, "-")

	def mDivPressed(self):
		self.binaryOperation(divide, "/")

	def resultPressed(self):
		if self.operation:
			self.second = float(self.display)
			try:
				answer = self.operation(self.first, self.second)
			except ValueError as e:
				self.cleared = True
				self.decimal = False
				self.screen.setText("ERROR: " + str(e))
				return

			if answer.is_integer():
				answer = int(answer)
			self.display = str(answer)
			self.cleared = True
			self.decimal = False
			self.screen.setText(self.display)
			self.opScreen.setText("=")

	def pclearPressed(self):
		self.display = "0"
		self.first = 0
		self.second = False
		self.operation = False
		self.cleared = True
		self.decimal = False
		self.screen.setText(self.display)
		self.opScreen.setText("")

app = QtWidgets.QApplication(sys.argv)
window = Ui()
window.setFixedSize(window.size())
app.exec_()
