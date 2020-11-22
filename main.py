import os
from PIL import Image

if os.path.exists('ImagesToResize'):
    #Loading all files (images) in folder ImageToResize
    files = os.listdir('./ImagesToResize')

    if not os.path.exists('Outputs'):
        os.makedirs('Outputs')

    if len(files) != 0:

        for file in files:
            #Each file (image) is opening and loading in Img
            Img = Image.open('./ImagesToResize/'+file)
            #Createing a new size
            newSize = [Img.size[0]/2, Img.size[1]/2]
            #Image size is change for newSize
            Img.thumbnail(newSize)
            #Image with new size is save in folder Outputs
            Img.save('./Outputs/'+file)
    else:
        print("There are no images in the folder")

else:
    print("Folder ImagesToResize don't exists")