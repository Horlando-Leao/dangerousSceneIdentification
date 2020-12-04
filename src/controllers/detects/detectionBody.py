import cv2 
from utils import url_to_image_array
from PIL import Image, ImageFilter


def detection_bodys(imagem_url: str) -> int:
    """RECEBE UMA URL DE IMAGEM, E RETORNA A QUANTIDADE 
    DE PARTES SUPERIORES DAS PESSOAS NA FOTO"""

    carregaAlgoritmo = cv2.CascadeClassifier("Haarcascade/haarcascade_upperbody.xml")

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


""" url = "https://www.tvsaj.com.br/wp-content/uploads/2020/06/Pessoa-em-situa%C3%A7%C3%A3o-de-rua-resgatada-pela-prefeitura-de-santo-antonio-de-jesus.jpeg"
url2 = "https://amenteemaravilhosa.com.br/wp-content/uploads/2018/09/homem-andnaod-e-mexendo-no-celular.jpg"
print(detection_bodys(url)) """
