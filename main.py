from PIL import Image
from pyzbar.pyzbar import decode

image_source = ''

data = decode(Image.open(image_source))
print(data)