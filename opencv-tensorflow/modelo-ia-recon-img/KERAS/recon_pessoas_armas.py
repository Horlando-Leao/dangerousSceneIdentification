import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np

# Desative a notação científica para maior clareza
#np.set_printoptions(suppress=False)
np.set_printoptions(suppress=True)
# Load the model
model = tensorflow.keras.models.load_model('keras_model-2.h5', compile=False)

# Crie a matriz da forma certa para alimentar o modelo keras
# O 'comprimento' ou número de imagens que você pode colocar no array é
# determinado pela primeira posição na tupla de forma, neste caso 1.
data = np.ndarray(shape=(1, 300, 300, 3), dtype=np.float32)

# IMAGEM DE ARMAS
#image = Image.open('fotos/com-arma/pessoa-6.jpg')#1 -   [[0.00000107 0.9999989 ]];[0.9983941  0.00160587]
#image = Image.open('fotos/com-arma/pessoa-10.jpg')#2 - [[0. 1.]];                 [0.00000724 0.9999927 ]
image = Image.open('fotos/com-arma/pessoa-15.jpg')#3 -     NULL  ;                  [0.72943753 0.2705625 ]

# IMAGEM DE PESSOAS
#image = Image.open('fotos/sem-arma/image_64.jpg')#3    [[0. 1.]];                 [0.00086649 0.9991335 ]
#image = Image.open('fotos/sem-arma/image_82.jpg')#4    [[0. 1.]];                 [0.00000088 0.99999917]

#redimensionar a imagem para 224x224 com a mesma estratégia do TM2:
#redimensionar a imagem para pelo menos 224 x 224 e depois cortar do centro
size = (300, 300)
image = ImageOps.fit(image, size, Image.ANTIALIAS)

# transforme a imagem em um array numpy
image_array = np.asarray(image)

# exibe a imagem redimensionada
image.show()

# Normaliza a imagem
#normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
# Carregue a imagem no array
data[0] = normalized_image_array

# execute a inferência
prediction = model.predict(data)
print(prediction[0])



