from utilities.utils import url_to_image_normal
from utilities.utils import truncate

import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np


def detection_guns(url_image: str) -> float:
    """1:RECEBE UMA URL E RETORNA TODAS AS PREDIÇÕES."""

    np.set_printoptions(suppress=True)
    model = tensorflow.keras.models.load_model("src\controllers\detects\ModelsKeras\keras_model-2.h5")
    #model = tensorflow.keras.models.load_model('detects/ModelsKeras/keras_model-2.h5', compile=False)

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
    
""" url = "https://cdn-istoe-ssl.akamaized.net/wp-content/uploads/sites/14/2019/01/e7f66c0f0c153eba4cbf868f5eccab26632176e2.jpg"
print(detection_guns(url_image = url, n_classes= 1)) """



