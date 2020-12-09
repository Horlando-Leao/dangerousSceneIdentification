from detects.detectionFaces import detection_faces
from detects.detectionGuns import  detection_guns
from detects.detectionBody import  detection_bodys
from detects.reconFacial import reconginit_face

def handiling_control(url_imagem: str, predictis = 'yy') -> str:

    def process_img(url_imagem: str, df = True, db = True , dg = True):
        try:
            if(df == True and db == True and dg == True):
                face = detection_faces(url_imagem = url_imagem)
                body = detection_bodys(url_imagem = url_imagem)
                gun = detection_guns(url_image = url_image)


            elif():
                face = detection_faces(url_imagem = url_imagem)
                gun = detection_guns(url_image = url_image)


            elif():
                body = detection_bodys(url_imagem = url_imagem)
                gun = detection_guns(url_image = url_image)
             
            else:
                gun = detection_guns(url_image = url_image)
            

        except Exception as erro:
            print("erro: ", erro)
            return[0]

    #url = url, n_classes = 1, predictis = 'yy'
    result = process_img(url_imagem = url_imagem)

    return True

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