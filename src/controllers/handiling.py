
import detects.detectionFaces as df
import detects.detectionBodys as db
import detects.detectionGuns as dg

def handiling_auto(url_imagem: str) -> float:

    body = db.detection_bodys(url_imagem)
    face = df.detection_faces(url_imagem)
    gun  = dg.detection_guns(url_imagem)
    
    return[body, face, gun[0], gun[1]]


def handiling_control(url_imagem: str, faces:bool = True, bodys:bool = True, guns:bool = True, compile:bool = False):

      
    if (faces == True and bodys == True and guns == True):
        face = df.detection_faces(url_imagem)
        body = db.detection_bodys(url_imagem)
        gun = dg.detection_guns(url_imagem)

        return[face, body, gun[0], gun[1]]

    elif (faces == False and bodys == True and guns == True):
        body = db.detection_bodys(url_imagem)
        gun = dg.detection_guns(url_imagem)

        return[body, gun[0], gun[1]]

    else:
        gun = dg.detection_guns(url_imagem)

        return[gun[0], gun[1]]
    
""" url = "https://cdn-istoe-ssl.akamaized.net/wp-content/uploads/sites/14/2019/01/e7f66c0f0c153eba4cbf868f5eccab26632176e2.jpg"
print(handiling_auto(url))
 """