from PyQt5.QtWidgets import QAction,QApplication, QDesktopWidget,QMainWindow, qApp, QGridLayout,QLabel, QPushButton,QLineEdit,QTextEdit, QWidget
from PyQt5.QtGui import QIcon, QPixmap
import sys

class Win(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        height = QDesktopWidget().availableGeometry().height()
        width = QDesktopWidget().availableGeometry().width()
        self.resize(width,height)
        self.center()
        self.setWindowTitle('Как-то так')
        self.statusBar().showMessage('Cool!')
        self.SetMenu()
        widget = self.CrtWidget()
        self.setCentralWidget(widget)
        self.show()

    def center(self):
        a = self.frameGeometry()
        b = QDesktopWidget().availableGeometry().center()
        a.moveCenter(b)
        self.move(a.topLeft())

    def SetMenu(self):
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

    def CrtWidget(self):
        widget = QWidget()
        grid = QGridLayout()
        grid.setSpacing(10)

        line = QLabel("DDDDDDDDDDDDDDDDDDDDDDDDDDD")

        grid.addWidget(line)

        widget.setLayout(grid)
        return widget

app = QApplication(sys.argv)
win = Win()
sys.exit(app.exec_())


