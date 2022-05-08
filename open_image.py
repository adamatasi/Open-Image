# Python program to read
# image using PIL module
 
# python3 open_image.py

# importing PIL
from PIL import Image
 
# Read image - 'My_Logo2.jpg' is your image
img = Image.open('My_Logo.jpg')
 
# Output Images
img.show()
 
# prints format of image
print(img.format)
 
# prints mode of image
print(img.mode)