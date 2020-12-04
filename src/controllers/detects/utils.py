"""FUNÇÕES DE IMAGENS"""

from urllib.request import urlopen
import requests as req

import numpy as np
import cv2

from PIL import Image, ImageFilter
from io import BytesIO


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


""" url = "https://renovamidia.com.br/wp-content/uploads/2019/01/youth-weapon-pistol-stupid-people-with-guns-pb-FEATURE.jpg"
teste = url_to_image_normal(url)
teste.show() """
	