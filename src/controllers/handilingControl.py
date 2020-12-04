from detects.detectionFaces import detection_faces
from detects.detectionGuns import  detection_guns
from detects.detectionBody import  detection_bodys
from detects.reconFacial import reconginit_face

def handiling_control(url_imagem: str, n_classes:int = 1, predictis = 'yy') -> str:

    def process_img(url_imagem: str, n_classes, predictis):
        try:
            if(predictis == 'yy'):
                face = detection_faces(url_imagem = url_imagem)
                body = detection_bodys(url_imagem = url_imagem)
                gun = detection_guns(url_image = url_image, n_classes= n_classes)

                if(n_classes == 1):
                    return [face, body, gun[0]]
                else:
                    return [face, body, gun[0], gun[1]]

            elif(predictis == 'yn'):
                face = detection_faces(url_imagem = url_imagem)
                gun = detection_guns(url_image = url_image, n_classes= n_classes)

                if(n_classes == 1):
                    return [face, gun[0]]
                else:
                    return [face, gun[0], gun[1]]

            elif(predictis == 'ny'):
                body = detection_bodys(url_imagem = url_imagem)
                gun = detection_guns(url_image = url_image, n_classes= n_classes)

                if(n_classes == 1):
                    return [body, gun[0]]
                else:
                    return [body, gun[0], gun[1]]                
    
            else:
                gun = detection_guns(url_image = url_image, n_classes= n_classes)

                if(n_classes == 1):
                    return [gun[0]]
                else:
                    return [gun[0], gun[1]]  
            

        except Exception as erro:
            print("erro: ", erro)
            return[0]

    #url = url, n_classes = 1, predictis = 'yy'
    result = process_img(url_imagem = url_imagem, n_classes = n_classes, predictis = predictis)
    items = len(result)
    
    if(n_classes == 1):
        pass
    else:
        pass
    """ face = result[0]
    body = result[1]
    gun = result[2] """

    return true
