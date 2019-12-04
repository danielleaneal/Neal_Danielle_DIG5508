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

        
    


        
        
    



    
    
    
# I added a "frameRate" element to the setup so I could maybe establish a frame rate
# and then the random selection of a phrase happen every time the frame restarts potentially.
# I don't know if this is the right way to go about making the phrase reset to another
# random phrase once it reaches the top again, but I'm going to experiment with this.
# Nothing happened when the frame rate was changed, so I'm gonna research some more
# options for making "something happen every __ seconds." Maybe putting the random
# generation on a timer would be a good option? 



# https://medium.com/greedygame-engineering/an-elegant-way-to-run-periodic-tasks-in-python-61b7c477b679
# Here is an article I found about "periodic actions" in Python, but it isn't specifically 
# about Python in Processing. I'm gonna see if any of these work in my draw line, because that's 
# where I want the periodic actions to be (in the display)


# I tried to get the code to "loop" and change the random element every time the mouse was clicked
# to try and incorporate iteration in this way, but I don't think I'm quite understanding
# how the loop works

# I finally got it to pick a different random line of the poem every time you hit the
# spacebar, which does sort of incorporate iteration, though not in the way I'd originally hoped.
# However, due to time constraints and other assignments that are looming over my head, 
# I will accept this program as having satisfied my initial goals of having features
# of text, poetry, randomization, movement, and iteration.


# THEN I added extra lines so there was even more "iteration" and "randomness" that also 
# refreshed with a spacebar click. I then spaced them out a ton so they were legible 
# altogether.
    

        

    
