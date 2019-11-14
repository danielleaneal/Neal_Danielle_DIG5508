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
# site, and could not get the "a" key to yield any sort of output. I figured out that I had to define the 
#function with two arguments.
    
    
def setup():
    size(200,200)
    print("test")
    noStroke()
    
            

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
    
myDog1 = Dog(color(255, 0, 0), random(0,200),random(0,200), 2)
myDog2 = Dog(color(250, 255, 255), random(0,200),random(0,200), 4)
myDog3 = Dog(color(250, 0, 255), random(0,200),random(0,200), 1)
myDog4 = Dog(color(0, 250, 255), random(0,200),random(0,200), 1)
myDog2 = Dog(color (random(255)), random(0,200),random(0,200), 3)

def draw(): 
    background(255)
    myCar1.drive()
    myCar1.display()
    myCar2.drive()
    myCar2.display()
    if ((keyPressed) and (key == ' ')):
        myCar2.setcolor(color(random(255)))
    myDog1.drive()
    myDog1.display()
    myDog2.drive()
    myDog2.display()
    myDog3.drive()
    myDog3.display()
    myDog4.drive()
    myDog4.display()
    pass

def mousePressed():
    rect(mouseX, mouseY, 33, 33)
    
    

# I changed the def display (self) function to make the dogs larger, because in my function,
# the dogs are Great Danes. I also changed the background color to be forest green,
# because the dogs are in a park (which is green). From here, I tried to mess with the speed of the animals,
# and caused some of the dogs to run faster than the others. I also spaced them out a little
# bit to give them room to run in the park. They move each frame.


#3-4
