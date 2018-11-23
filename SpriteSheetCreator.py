'''given a bunch of sprites of the same width and height,
this script creates a single image out of them,
evenly spacing the images next to each other'''

import sys
from PIL import Image
import os

noOfImages = 105 #no of images to find

images = [None]*noOfImages
noInRowColumn = 11

width = height = 278 # the width and height of each image

#open each image ending with .png and add it to the list
i = 0
for f in os.listdir('.'):
    if f.endswith('.png'):
        images[i] = Image.open(f)
        i+=1

newImage = Image.new('RGBA', (width*noInRowColumn, height*noInRowColumn)) #initialise the new image

# paste the images on the new image one after the other
i = 0
while (i < 105):
    newImage.paste(images[i],((((i%noInRowColumn))*height),((int)(i/noInRowColumn))*width))
    i+=1

newImage.save('test.png') # can change new file name here