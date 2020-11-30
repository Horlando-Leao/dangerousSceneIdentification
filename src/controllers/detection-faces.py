import cv2 
from PIL import Image, ImageFilter
from convert_url_to_img import url_to_image
#from controllers.convert_url_to_img import url_to_image()


def detection_faces(imagem_url: str) -> str:

    carregaAlgoritmo = cv2.CascadeClassifier("Haarcascade/haarcascade_frontalface_default.xml")

    imagem = url_to_image(imagem_url)

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
    try:
        count = 0
        for faces_x in faces:
            print(faces[count])
            count += 1
        print("Quat. de pessoas: ", count)

    except Exception as erro:
        print("Erro: ", EOFError)


url = ("https://s2.glbimg.com/lUP7OVzUYf7V6LQ0lsA_dPavEG4=/640x0/s.glbimg.com/et/nv/f/original/2013/01/14/favela-01.jpg")
detection_faces(url)