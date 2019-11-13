# Danielle Neal Lab 3

#3-2

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
    def setcolor(self, newcolor):
        self.c = newcolor
    
    def drive(self):
        self.xpos = self.xpos + self.xspeed;
        if self.xpos > width:
            self.xpos = 0

myCar1 = Car(color(255, 0, 0), 0, 100, 2)
myCar2 = Car(color(250, 255, 255), 0, 10, 1)

# When I first tried to add "keypressed" to the function, I got an error that stated 
# "keyPressed is not defined." I'm going to research how to define keyPressed, as I thought that 
# defining that I wanted the keyPressed to be the spacebar would be sufficient. I changed "keyPressed" to
# "keyCode" and somehow got rid of this error, but the function is still not working when I run the code
# and press the space bar. I also tried this with the letter "a" key, as shown on the processing tutorial 
# site, and could not get the "a" key to yield any sort of output.
    
    
def setup():
    size(200,200)
    print("test")
    
    
def draw(): 
    background(255)
    myCar1.drive()
    myCar1.display()
    myCar2.drive()
    myCar2.display()
    if ((keyPressed) and (key == ' ')):
        myCar2.setcolor(color(random(255)))
