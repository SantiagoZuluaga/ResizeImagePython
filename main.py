import os
from PIL import Image

#Loading all files (images) in folder ImageToResize
files = os.listdir('./ImagesToResize')

for file in files:
    #Each file (image) is opening and loading in Img
    Img = Image.open('./ImagesToResize/'+file)
    #Createing a new size
    newSize = [Img.size[0]/2, Img.size[1]/2]
    #Image size is change for newSize
    Img.thumbnail(newSize)
    #Image with new size is save in folder Outputs
    Img.save('./Outputs/'+file)
