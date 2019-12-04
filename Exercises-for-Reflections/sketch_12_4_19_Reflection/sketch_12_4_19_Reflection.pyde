#Reflection for 12.4.19

lines_of_the_poem = ['Love is not hate',
                     'Love smells like roses',
                     'Love is ','Love is colorless,because it is blind',
                     'Love feels like a connection and bond that brings happiness',
                     'Love is white because marriage dresses',
                     'Love is the sound of stirring mac and cheese',
                     'Love is that feeling you get when you embrace someone when it is cold outside',
                     'Love is that feeling you get whenever you think about your significant other or see them',
                     'Love is whatever color you desire',
                     'Love feels like',
                     'Love is generally red, a healthy heart is technically pink, but love to me is a bold, bright color',
                     'Love feels like looking into those beautiful eyes of yours',
                     'I\'ve never been in love before, but I can imagine it would feel similar to how a young kids feels when they meet their first crush. Nothing else matters in that moment.',
                     'Love sounds like a consistent, yet racing heartbeat',
                     'Love is someone that\'s fun and happy and goes with the flow',
                     'Love is the sound of waves hitting the shore',
                     'Love is the scent of Starbucks, because I used to go there to study with my ex like every other day',
                     'If I knew what love was I wouldn\'t be using this app',
                     'Love is the sunrise',
                     'Love is being able to talk about anything',
                     'Love is',
                     'Love is',
                     'Love is a homecooked meal']

class Poem(object):
    def __init__(self,poem,xpos, ypos, yspeed):
        self.poem=poem
        self.xpos = xpos
        self.ypos = ypos
        self.yspeed = yspeed
        self.listLen = len(self.poem)
        self.ran = int(random(0,self.listLen))
        
        
        
    def display(self):
        textSize(28)
        fill(0)   
        print(self.ran)            
        text(self.poem[self.ran], self.xpos, self.ypos, 800,300)
        self.ypos = self.ypos + self.yspeed;
        if self.ypos > height:
            self.ypos = 0
            
    def anotherrandomline(self, poem, xpos, ypos, yspeed):
        self.poem=poem
        self.xpos = xpos
        self.ypos = ypos
        self.yspeed = yspeed
        self.listLen = len(self.poem)
        self.ran = int(random(0,self.listLen));
     
      
        
def setup():
    size (1000,1000)
    frameRate(60)
    
myPoem1 = Poem(lines_of_the_poem, 5,0,2.5)
myPoem2 = Poem(lines_of_the_poem, 5,200,2.5)
myPoem3 = Poem(lines_of_the_poem, 5,385,2.5)
    
def draw():
    background(244,194,194)
    myPoem1.display()
    myPoem2.display()
    myPoem3.display()
    if (keyPressed and (key==' ')):
        myPoem1.anotherrandomline(lines_of_the_poem, 5,0,2.5)        
        myPoem2.anotherrandomline(lines_of_the_poem, 5,200,2.5)
        myPoem3.anotherrandomline(lines_of_the_poem, 5,385,2.5)    
