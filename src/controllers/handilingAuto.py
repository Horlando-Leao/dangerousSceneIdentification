
import detects.detectionFaces as df
import detects.detectionBodys as db
import detects.detectionGuns as dg

def handiling_auto(url_imagem: str) -> str:

    
    face = df.detection_faces(url_imagem)
    body = db.detection_bodys(url_imagem)
    gun  = dg.detection_guns(url_imagem)
    
    return[face, body, gun[0], gun[1]]

url = "https://cdn-istoe-ssl.akamaized.net/wp-content/uploads/sites/14/2019/01/e7f66c0f0c153eba4cbf868f5eccab26632176e2.jpg"
print(handiling_auto(url))
