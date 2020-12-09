from urllib.request import urlopen
from PIL import Image, ImageFilter, ImageOps
from io import BytesIO
import requests as req
import numpy as np

import cv2
import tensorflow.keras


def url_to_image_array(url_image: str):
    """RECEBE UMA URL STRING E RETORNA UMA IMAGEM FORMATADA EM ARRAY
    ,SALVA APENAS NA MÉMORIA RAM."""

    try:
        resp = urlopen(url_image)
        image = np.asarray(bytearray(resp.read()), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        return image
    except Exception as erro:
        print("ERRO:", erro)
        return False


def url_to_image_download(url_image: str):
    """RECEBE UMA URL STRING E SALVA UMA IMAGEM, 
    RETORNANDO O CAMINHO DA IMAGEM SALVA."""

    path = 'Pictures/pic1.jpg'

    with open(path, 'wb') as handle:
        response = req.get(url_image, stream=True)

        if not response.ok:
            print (response)
            return 'no-save'

        for block in response.iter_content(1024):
            if not block:
                break
            handle.write(block)
            return path


def url_to_image_normal(url_image: str):
    """RECEBE UMA URL STRING E RETORNA UMA IMAGEM SEM FORMATAÇÃO
    ,SALVA APENAS NA MÉMORIA RAM."""

    response = req.get(url_image)
    im = Image.open(BytesIO(response.content))
    return (im)

    #im.show() #mostrar imagem

def truncate(f, n):
    """ Trunca / preenche um flutuante f para n casas decimais sem arredondamento """
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])


def detection_guns(url_image: str) -> float:
    """1:RECEBE UMA URL E RETORNA TODAS AS PREDIÇÕES."""

    np.set_printoptions(suppress=True)

    model = tensorflow.keras.models.load_model('ModelsKeras/keras_model-2.h5', compile=False)

    data = np.ndarray(shape=(1, 300, 300, 3), dtype=np.float32)

    #image = Image.open('fotos/com-arma/pessoa-15.jpg')
    image = url_to_image_normal(url_image)

    size = (300, 300)

    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    # transforme a imagem em um array numpy
    image_array = np.asarray(image)

    # exibe a imagem redimensionada
    #image.show()

    # Normaliza a imagem
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    # Carregue a imagem no array
    data[0] = normalized_image_array

    # execute a inferência
    prediction = model.predict(data)
    
    ##organizando e formatando

    classes = []
    for x in prediction[0]:
        class_ = float(truncate(x,2))
        classes.append(class_)

    return(classes)



def detection_faces(imagem_url: str) -> int:
    """RECEBE UMA URL DE IMAGEM E RETORNA UMA QUANTIDADE DE FACES DETECTADAS"""
    carregaAlgoritmo = cv2.CascadeClassifier("haarcascade/haarcascade_frontalface_default.xml")
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
        #print("Quat. de pessoas: ", count)
        return (count)

    except Exception as erro:
        print("Erro: ", EOFError)
        return (count)


def detection_bodys(imagem_url: str) -> int:
    """RECEBE UMA URL DE IMAGEM, E RETORNA A QUANTIDADE 
    DE PARTES SUPERIORES DAS PESSOAS NA FOTO"""

    carregaAlgoritmo = cv2.CascadeClassifier("haarcascade/haarcascade_upperbody.xml")

    imagem = url_to_image_array(imagem_url)

    #=============================================

    scale_percent = 120 # percent of original size
    width = int(imagem.shape[1] * scale_percent / 100)
    height = int(imagem.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    imagem = cv2.resize(imagem, dim, interpolation = cv2.INTER_AREA)

    #=============================================
    #imagem = cv2.resize(imagem, (0,0), fx=1, fy=1) 
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    #DETECÇÃO DAS bodys
    bodys = carregaAlgoritmo.detectMultiScale(
        imagemCinza, 
        scaleFactor=1.1, 
        #minNeighbors=3,  #abordagem de vizihança, (^) = + perder os verdadeiros positivos, (v) = + falsos positivos
        minSize=(1,1),
        maxSize=(50,50) 
        )

    ##crie um retangulo nas bodys que detectMultiScale localizou
    """ for(x, y, l, a) in bodys:
        cv2.rectangle( imagem, ( x , y ), ( x + l, y + a ),( 0, 255, 0 ), 2 ) """

    ##exibe a imagem
    """ cv2.imshow("bodys", imagem)
    cv2.waitKey() """

    #Pequena regra de negócio
    count = 0
    try:
        for bodys_x in bodys:
            count += 1

        print("Quat. de pessoas: ", count)
        return (count)

    except Exception as erro:
        print("Erro: ", EOFError)
        return (count)

def handlee(url:str) -> float:
    face = detection_faces(url)
    body = detection_bodys(url)
    gun  = detection_guns(url)
    return ([face, body, gun])

url = "https://cdn-istoe-ssl.akamaized.net/wp-content/uploads/sites/14/2019/01/e7f66c0f0c153eba4cbf868f5eccab26632176e2.jpg"
print(handlee(url))

