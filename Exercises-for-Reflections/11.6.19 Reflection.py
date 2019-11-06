#Exercise 10-2 - Flipping along the other axis

#%%
from PIL import Image

img = Image.open("Exercises-for-Reflections\DAWGS.jpg")
img.rotate(180).show()

#^^^Here, I wrote code to rotate an image 180 degrees,
# which effectively "flips it along an axis." I want to NOW
# try and write a FUNCTION that does this, considering I now 
# know which components I need to call to make the desired outcome
# happen.


#%%
from PIL import Image
img = Image.open("Exercises-for-Reflections\DAWGS.jpg")

img = ImageOps.flip(img)

img.show

#This is my first attempt, it doesn't work. Trying to figure out what
# "ImageOps" is and why it's not defined and what it should do in this 
# function.
    



