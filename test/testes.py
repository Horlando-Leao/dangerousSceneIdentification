from PIL import Image, ImageFilter
import requests
from io import BytesIO

url = 'https://i0.wp.com/gamelogia.com.br/wp-content/uploads/2016/11/gamer.jpg?resize=1280%2C640&ssl=1'
response = requests.get(url)

im = Image.open(BytesIO(response.content))
im.show()

#HASH
import random

hash = random.getrandbits(128)

print("hash value: %032x" % hash)