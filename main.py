# importing required libraries
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
import os
import sys


class MainWindow(QMainWindow):

	
	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)


		
		self.browser = QWebEngineView()
		
		self.browser.setUrl(QUrl("https://www.zerohedge.com/"))

		
		self.browser.urlChanged.connect(self.update_urlbar)

		
		self.browser.loadFinished.connect(self.update_title)

		
		self.setCentralWidget(self.browser)

		
		self.status = QStatusBar()

		
		self.setStatusBar(self.status)

		
		navtb = QToolBar("Navigation")

		
		self.addToolBar(navtb)

		
		back_btn = QAction("Back", self)

		
		back_btn.setStatusTip("Back to previous page")

		
		back_btn.triggered.connect(self.browser.back)

		
		navtb.addAction(back_btn)

		
		next_btn = QAction("Forward", self)
		next_btn.setStatusTip("Forward to next page")

		
		next_btn.triggered.connect(self.browser.forward)
		navtb.addAction(next_btn)

		# similarly for reload action
		reload_btn = QAction("Reload", self)
		reload_btn.setStatusTip("Reload page")

		# adding action to the reload button
		# making browser to reload
		reload_btn.triggered.connect(self.browser.reload)
		navtb.addAction(reload_btn)

		# similarly for home action
		home_btn = QAction("Home", self)
		home_btn.setStatusTip("Go home")
		home_btn.triggered.connect(self.navigate_home)
		navtb.addAction(home_btn)

		# adding a separator in the tool bar
		navtb.addSeparator()

		# creating a line edit for the url
		self.urlbar = QLineEdit()

		# adding action when return key is pressed
		self.urlbar.returnPressed.connect(self.navigate_to_url)

		# adding this to the tool bar
		navtb.addWidget(self.urlbar)

		# adding stop action to the tool bar
		stop_btn = QAction("Stop", self)
		stop_btn.setStatusTip("Stop loading current page")

		# adding action to the stop button
		# making browser to stop
		stop_btn.triggered.connect(self.browser.stop)
		navtb.addAction(stop_btn)

		# showing all the components
		self.show()


	# method for updating the title of the window
	def update_title(self):
		title = self.browser.page().title()
		self.setWindowTitle("% s - Zero Browser" % title)


	# method called by the home action
	def navigate_home(self):

		# open the google
		self.browser.setUrl(QUrl("https://www.zerohedge.com/"))

	# method called by the line edit when return key is pressed
	def navigate_to_url(self):

		# getting url and converting it to QUrl object
		q = QUrl(self.urlbar.text())

		# if url is scheme is blank
		if q.scheme() == "":
			# set url scheme to html
			q.setScheme("http")

		# set the url to the browser
		self.browser.setUrl(q)

	# method for updating url
	# this method is called by the QWebEngineView object
	def update_urlbar(self, q):

		# setting text to the url bar
		self.urlbar.setText(q.toString())

		# setting cursor position of the url bar
		self.urlbar.setCursorPosition(0)


# creating a pyQt5 application
app = QApplication(sys.argv)

# setting name to the application
app.setApplicationName("Geek Browser")

# creating a main window object
window = MainWindow()

# loop
app.exec_()
