import requests
from io import BytesIO
import cv2 
from PIL import Image, ImageFilter


def detection_faces(imagem_url: str) -> str:
    
    carregaAlgoritmo = cv2.CascadeClassifier("Haarcascade/haarcascade_frontalface_default.xml")

    """ url = 'https://i0.wp.com/gamelogia.com.br/wp-content/uploads/2016/11/gamer.jpg?resize=1280%2C640&ssl=1'
    response = requests.get(url)

    im = Image.open(BytesIO(response.content)) """

    imagem = cv2.imread("./fotos/pessoa-2.jpg")

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
        if faces == ():
            print("sem pessoas")
        else:
            count = 0
            for faces_x in faces:
                print(faces[count])
                count += 1
            print("Quat. de pessoas: ", count)

    except Exception as erro:
        print("Erro: ", EOFError)
