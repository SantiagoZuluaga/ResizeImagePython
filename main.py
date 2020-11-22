import os
from PIL import Image

if os.path.exists('ImagesToResize'):
    #Loading all files (images) in folder ImageToResize
    files = os.listdir('./ImagesToResize')

    if not os.path.exists('Outputs'):
        os.makedirs('Outputs')

    if len(files) != 0:

        for file in files:

            scale = 0
            print(file)
            while True:
                inputscale = input("Enter a scale to resize image: ")
                try:
                    scale = float(inputscale)
                    break
                except ValueError:
                    print("Scale is not valid.")
            
            #Each file (image) is opening and loading in Img
            Img = Image.open('./ImagesToResize/'+file)
            #Createing a new size
            newSize = [Img.size[0]/scale, Img.size[1]/scale]
            #Image size is change for newSize
            Img.thumbnail(newSize)
            #Image with new size is save in folder Outputs
            Img.save('./Outputs/'+file)
            print("Reized image succesfully.")
    else:
        print("There are no images in the folder")

else:
    print("Folder ImagesToResize don't exists")