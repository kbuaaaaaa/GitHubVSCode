import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class Simple_drawing_window(QWidget):
    def __init__(self):
       QWidget.__init__(self, None)
       self.setWindowTitle("Simple Drawing")
       self.rabbit = QPixmap("images/rabbit.png")
        
    def paintEvent(self,e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(0,127,0))
        p.drawPolygon([QPoint(40,100),QPoint(180,110),QPoint(166,100),QPoint(170,105)])
        p.setPen(QColor(278,100,0))
        p.setBrush(QColor(255,27,0))
        p.drawPie(50,150,100,100,0,180*16)
        p.drawPolygon([QPoint(50,250),QPoint(150,206),QPoint(180,400),])
        p.drawPixmap(QRect(200,100,320,320),self.rabbit)
        p.end()
        
class Simple_drawing_window2(QWidget):
    def __init__(self):
       QWidget.__init__(self, None)
       self.setWindowTitle("Simple Drawing")
       self.rabbit = QPixmap("images/rabbit.png")
        
    def paintEvent(self,e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(255,0,0))
        p.drawPolygon([QPoint(70,10),QPoint(120,110),QPoint(30,100),QPoint(100,50)])
        p.setPen(QColor(255,0,0))
        p.setBrush(QColor(255,0,0))
        p.drawPie(50,150,100,100,0,180*16)
        p.drawPolygon([QPoint(50,20),QPoint(550,200),QPoint(170,400),])
        p.drawPixmap(QRect(200,100,320,320),self.rabbit)
        p.end()

def main():
    app = QApplication(sys.argv)
    w = Simple_drawing_window()
    w.show()
    w2 = Simple_drawing_window2()
    w2.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())
