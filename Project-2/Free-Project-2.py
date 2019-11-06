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


#%%




