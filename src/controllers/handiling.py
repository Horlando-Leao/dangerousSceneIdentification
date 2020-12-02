from detects.detectionFaces import detection_faces
from detects.detectionGuns import  detection_guns
from detects.detectionBody import  detection_body

def handiling(url_imagem: str) -> json:

    def process_img(url_imagem: str) -> array:
        try:
            face = detection_faces(url_imagem)
            body = detection_body(url_imagem)
            gun  = detection_guns(url_imagem)
            return [face, body, gun]

        except Exception as erro:
            print("erro: ", erro)
            return[0]

    def set_weights():
        return True

    def handiling():
        return True
    
    return true
