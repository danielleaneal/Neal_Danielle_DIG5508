#Danielle Neal Lab 3, working in Processing with a Python Mode.

#3-1

class Car(object):
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
        rect(self.xpos, self.ypos, 20, 10);
    
    def drive(self):
        self.xpos = self.xpos + self.xspeed;
        if self.xpos > width:
            self.xpos = 0
    
myCar1 = Car(color(255, 0, 0), 0, 100, 2)
myCar2 = Car(color(250, 255, 255), 0, 10, 1)
myCar2 = Car(color (random(255)), 0, 10, 1)

#I changed one of the cars to white, then I chose to make it randomly determine one
# part of myCar2's colors. Now myCar2 is a random different shade of grey every time I run 
# the function
    
def setup():
    size(200,200)
    
#Fixed an indentation error here to make the cars run. I see one
#blue and one red car moving from left to right.

def draw(): 
  background(255)
  myCar1.drive()
  myCar1.display()
  myCar2.drive()
  myCar2.display()
