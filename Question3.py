import turtle

class Disk(object):

    def __init__(self,name="",xpos=0,ypos=0,height=20,width=40,color = "Red"):
        self.dname = name
        self.dxpos = xpos
        self.dypos = ypos
        self.dheight = height
        self.dwidth = width
        self.dcolor = color

    def showdisk(self,color = "Red"):
        turtle.fillcolor(color)
        turtle.begin_fill()
        turtle.lt(90)
        turtle.penup()
        turtle.goto(self.dxpos,self.dypos)
        turtle.pendown()
        turtle.rt(90)
        for x in range(2):
            turtle.fd(self.dwidth/2)
            turtle.lt(90)
            turtle.fd(self.dheight)
            turtle.lt(90)
            turtle.fd(self.dwidth/2)
        turtle.end_fill()

    def newpos(self,xpos,ypos):
        self.dxpos = xpos
        self.dypos = ypos
        
    def cleardisk(self):
        turtle.pencolor("WHITE")
        
        self.showdisk("WHITE")
        turtle.pencolor("BLACK")




