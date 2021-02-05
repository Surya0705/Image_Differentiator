from PIL import Image, ImageChops # Importing the Pillow Module for this Program.

a = Image.open("Image1.jpg") # Defining 'a' as the Image1.
b = Image.open("Image2.jpg") # Defining 'b' as the Image2.
c = ImageChops.difference(a, b) # Making the Program Differentiate between both Images.
if c.getbbox(): # Getting the bbox from Pillow fo rthis Program.
    c.show() # Displaying the differentiated parts of the Image.