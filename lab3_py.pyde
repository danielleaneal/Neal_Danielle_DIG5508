

 #3-1. Event

class Car:

    def __init__(self, c, xpos, ypos, xspeed):
        self.c = c
        self.xpos = xpos
        self.ypos = ypos
        self.xspeed = xspeed
        
        
    def display(self):
        stroke(0)
        fill(self.c)
        rectMode(CENTER)
        rect(self.xpos, self.ypos, 20, 10);
    
    def colorchange(self, newcolor):
        self.c = newcolor

    def drive(self):
        self.xpos = self.xpos + self.xspeed;
        if self.xpos > width:
            self.xpos = 0

class pedestrian:

    def __init__(self, c, xpos, ypos, xspeed):
        self.c = c
        self.xpos = xpos
        self.ypos = ypos
        self.xspeed = xspeed
        
    def display(self):
        stroke(0)
        fill(self.c)
        rectMode(CENTER)
        rect(self.xpos, self.ypos, 20, 10);

    def walk(self):
        self.xpos = self.xpos + self.xspeed;
        if self.xpos > width:
            self.xpos = 0
    #For some reason i have a stretch in the forms and they are overlappad.  

  #3-2. Interactivity           
class Click(object):

    def __init__(self, c, xpos, ypos, xspeed):
        self.c = c
        self.xpos = xpos
        self.ypos = ypos
        self.xspeed = xspeed
  #3-3.New Object
    def updatelocation(self, xpos, ypos):
        self.xpos = xpos
        self.ypos =ypos
        
    def display(self):
        stroke(0)
        fill(self.c)
        rectMode(CENTER)
        rect(self.xpos, self.ypos, 20, 10);
myClick1 = Click(color(22 , 22, 22), 0, 0, 10)
def mousePressed ():
    myClick1.updatelocation(mouseX, mouseY)


myCar1 = Car(color(50, 0, 0), 0, 20, 2)
myCar2 = Car(color(0, 150, 150), 0, 10, 1)
mypedestrian1 = pedestrian(color(150, 0, 0), 0, 50, 1)
mypedestrian2 = pedestrian(color(0, 100, 100), 0, 40, 3)

  #For some reason i have a stretch in the forms and they are overlappad.  

def setup():
    size(200,200)
    
def draw():    
    myCar1.drive()
    myCar1.display()
    myCar2.drive()
    myCar2.display()
    
    if ((keyPressed) and (key == ' ')):
        myCar2.colorchange(color(random(255), random(255), random(255)))
   
    mypedestrian1.walk()
    mypedestrian1.display()
    mypedestrian2.walk()
    mypedestrian2.display()
    myClick1.display()
 
     
    
    #  
    
    
