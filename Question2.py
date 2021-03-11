from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import sys
 
 
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
 
 
        title = "Paint Application"
        top = 400
        left = 400
        width = 800
        height = 600
 
        icon = "icons/pain.png"
 
        self.setWindowTitle(title)
        self.setGeometry(top, left, width, height)
        self.setWindowIcon(QIcon(icon))
 
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)
 
        self.drawing = False
        self.brushSize = 4
        self.brushColor = Qt.black
        self.lastPoint = QPoint()
 
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("File")

        button = QPushButton('Clear', self)
        button.move(300,500)
        button.clicked.connect(self.clear)
        self.label = QLabel("Drag the mouse to draw", self)
        self.label.move(300,470)
        self.label.resize(200,20)
 
    
 
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()
            #print(self.lastPoint)
 
 
