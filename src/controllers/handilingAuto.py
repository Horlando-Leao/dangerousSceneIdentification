
import detects.detectionFaces as df
import detects.detectionBodys as db
import detects.detectionGuns as dg

def handiling_auto(url_imagem: str) -> str:

    
    face = df.detection_faces(url_imagem)
    body = db.detection_bodys(url_imagem)
    gun  = dg.detection_guns(url_imagem)
    
    return[face, body, gun]
    """ #tem corpo
    if(body > 0):
        #tem rosto e tem arma
        if(face > 0 and gun > 0.65):
            return ("Cuidado")
        else:
            #esta mascarado e tem arma
            if(gun > 0.50):
                return ("Cuidado")
            #pode estar de chapeu ou capacete e não tem arma
            else:
                return ("Relaxa")
    #nao tem corpo
    else:
        #tem 1 ou 2 rostos, suspeito, e tem arma
        if (face > 0 and face <= 2 and gun > 0.40):
            return("Cuidado")
        #não tem movimento suspeito e parece não ter arma
        else:
            return("Relaxa") """

url = "https://cdn-istoe-ssl.akamaized.net/wp-content/uploads/sites/14/2019/01/e7f66c0f0c153eba4cbf868f5eccab26632176e2.jpg"
print(handiling_auto(url))
