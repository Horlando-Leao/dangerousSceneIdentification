from urllib.request import urlopen
import numpy as np
import cv2

def url_to_image(url: str):
	
    try:
        resp = urlopen(url)
        image = np.asarray(bytearray(resp.read()), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        return image
    except Exception as erro:
        print("ERRO:", erro)
        return False
	
	

	
