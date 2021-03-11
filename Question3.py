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

class Pole(object):

    def __init__(self,name="",xpos=0,ypos=0,thick=10,length=100):
        self.pname = name
        self.stack = []
        self.toppos = 0
        self.pxpos = xpos
        self.pypos = ypos
        self.pthick = thick
        self.plength = length

    def showpole(self):
        turtle.lt(90)
        turtle.penup()
        turtle.goto(self.pxpos,self.pypos)
        turtle.pendown()
        turtle.rt(90)
        for x in range(2):
            turtle.fd(self.pthick/2)
            turtle.lt(90)
            turtle.fd(self.plength)
            turtle.lt(90)
            turtle.fd(self.pthick/2)

    def pushdisk(self,disk):
        disk.newpos(self.pxpos,self.toppos)
        disk.showdisk()
        self.stack.append(disk)
        self.toppos += disk.dheight
        self.toppos += 1


    def popdisk(self):
        d = self.stack.pop()
        d.cleardisk()
        self.toppos -= 1
        self.toppos -= d.dheight
        return d
       
class Hanoi(object):

    def __init__(self,n=3,start="A",workspace="B",destination="C"):
        self.startp = Pole(start,0,0)
        self.workspacep = Pole(workspace,150,0)
        self.destinationp = Pole(destination,300,0)
        self.startp.showpole()
        self.workspacep.showpole()
        self.destinationp.showpole()
        for i in range(n):
            self.startp.pushdisk(Disk("d"+str(i),0,i*150,20,(n-i)*30))

    def move_disk(self,start,destination):
        disk = start.popdisk()
        destination.pushdisk(disk)

    def move_tower(self,n,s,d,w):
        if n == 1:
            self.move_disk(s,d)
        else:
            self.move_tower(n-1,s,w,d)
            self.move_disk(s,d)
            self.move_tower(n-1,w,d,s)

    def solve(self):
        self.move_tower(3,self.startp,self.destinationp,self.workspacep)


h = Hanoi()
h.solve()


