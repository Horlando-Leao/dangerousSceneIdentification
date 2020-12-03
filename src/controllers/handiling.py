from detects.detectionFaces import detection_faces
from detects.detectionGuns import  detection_guns
from detects.detectionBody import  detection_body
from detects.reconFacial import reconginit_face

def handiling(url_imagem: str) -> str:

    def process_img(url_imagem: str):
        try:
            face = detection_faces(url_imagem)#int 0 até ...
            body = detection_body(url_imagem)#int 0 até ...
            gun  = detection_guns(url_imagem)#array 2 posições
            return [face, body, gun[0], gun[1]]

        except Exception as erro:
            print("erro: ", erro)
            return[0]

    def set_weights():
        """SETA OS PESOS"""
        return True

    def rating():
        return True
    
    return true
