import cv2 
from utils import url_to_image_array
from PIL import Image, ImageFilter


def detection_faces(imagem_url: str) -> int:

    carregaAlgoritmo = cv2.CascadeClassifier("Haarcascade/haarcascade_frontalface_default.xml")

    imagem = url_to_image_array(imagem_url)

    #imagem = cv2.imread('caminho')
    imagem = cv2.resize(imagem, (0,0), fx=0.7, fy=0.7) 
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    #DETECÇÃO DAS FACES
    faces = carregaAlgoritmo.detectMultiScale(
        imagemCinza, 
        scaleFactor=1.1, 
        minNeighbors=3,  #abordagem de vizihança, (^) = + perder os verdadeiros positivos, (v) = + falsos positivos
        minSize=(20,20) #tamanho da detecção de uma face
        )

    #Pequena regra de negócio
    count = 0
    try:
        for faces_x in faces:
            print(faces[count])
            count += 1
        print("Quat. de pessoas: ", count)
        return (count)

    except Exception as erro:
        print("Erro: ", EOFError)
        return (count)

