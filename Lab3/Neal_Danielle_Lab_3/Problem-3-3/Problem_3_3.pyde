# Danielle Neal Lab 3

#3-3

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
  
# I changed the def display (self) function to make the dogs larger, because in my function,
# the dogs are Great Danes. I also changed the background color to be forest green,
# because the dogs are in a park (which is green). From here, I tried to mess with the speed of the animals,
# and caused some of the dogs to run faster than the others. I also spaced them out a little
# bit to give them room to run in the park. They move each frame.
