#Danielle Neal Lab 3

#3-4

class Dog(object):
# The Constructor is defined with arguments.
    def __init__(self, c, xpos, ypos, xspeed):
        self.c = c
        self.xpos = xpos
        self.ypos = ypos
        self.xspeed = xspeed
        
    def display(self):
        stroke(0)
        fill(self.c)
        rectMode(CENTER)
        rect(self.xpos, self.ypos, 30, 20);
    
    def drive(self):
        self.xpos = self.xpos + self.xspeed;
        if self.xpos > width:
            self.xpos = 0
    
myDog1 = Dog(color(255, 0, 0), 0, 45, 2)
myDog2 = Dog(color(250, 255, 255), 60, 10, 4)
myDog3 = Dog(color(250, 0, 255), 80, 10, 1)
myDog4 = Dog(color(0, 250, 255), 150, 30, 1)
myDog2 = Dog(color (random(255)), 0, 60, 3)

    

    
def setup():
    size(300,200)

    
def draw(): 
  background(0,128,0)
  myDog1.drive()
  myDog1.display()
  myDog2.drive()
  myDog2.display()
  myDog3.drive()
  myDog3.display()
  myDog4.drive()
  myDog4.display()

  
class DRAWING(object):
    c=color(250)
    
def draw():
    frameRate(5)
    printIn(pmousex - mousexX)
  
def setup():
    size(100, 100)
    strokeWeight(2)


def draw():
    line(mouseX, mouseY, pmouseX, pmouseY)
    
    
# This allows me to "draw" lines with my mouse, but the dogs in the frame disappeared.
# I also don't know how to make the drawing not a one line drawing. However, when I tried
# to name the class "DRAWING," it didn't work anymore. I got an indentation error,
# but when I tried to indent the def draw, and def setup functions, my dog class came back
# when I ran it and the drawing with my mouse line disappeared.
