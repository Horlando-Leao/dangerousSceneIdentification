from utils import url_to_image_normal
import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np


def detection_guns(url_image: str) -> array:

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
    image.show()

    # Normaliza a imagem
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    # Carregue a imagem no array
    data[0] = normalized_image_array

    # execute a inferência
    prediction = model.predict(data)
    print(prediction[0])
    return (prediction[0])

url = "https://renovamidia.com.br/wp-content/uploads/2019/01/youth-weapon-pistol-stupid-people-with-guns-pb-FEATURE.jpg"
predi = detection_guns(url)
print(predi[1])



