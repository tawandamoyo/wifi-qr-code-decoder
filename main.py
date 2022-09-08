from PIL import Image
from pyzbar.pyzbar import decode

image_source = './pp/jpg'

data = decode(Image.open(image_source))
print(type(data))
print(len(data))
print(data)