#Free Project 2, free project 11-1 from Programming Textbook


#putting text on a picture
#%%
from PIL import Image, ImageDraw

def transformimage(text, bgcolor):
    img = Image.new('RGB', (100, 30), color = bgcolor)


    d = ImageDraw.Draw(img)
    d.text ((10,10), text, fill=(255,255,0))
    return img


transformimages("Dani Was HERE", "pink")



#putting text on an image on my local computer and making the
#text show up closer to the center of it (because the image is
#larger than before)
#%%
from PIL import Image, ImageDraw

def transformlocalimage(text):
    img = Image.open("Project-2\DAWGS.jpg")
    width,height = img.size
    w = width / 2
    h = height / 2

    d = ImageDraw.Draw(img)
    d.text ((w,h), text, fill=(255,255,0))
    return img


transformlocalimage("HI JOHN MURRAY")







