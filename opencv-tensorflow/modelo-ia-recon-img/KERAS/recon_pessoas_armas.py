import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np

# Desative a notação científica para maior clareza
#np.set_printoptions(suppress=False)
np.set_printoptions(suppress=True)
# Load the model
model = tensorflow.keras.models.load_model('keras_model.h5', compile=False)

# Crie a matriz da forma certa para alimentar o modelo keras
# O 'comprimento' ou número de imagens que você pode colocar no array é
# determinado pela primeira posição na tupla de forma, neste caso 1.
data = np.ndarray(shape=(1, 600, 600, 3), dtype=np.float32)

# IMAGEM DE ARMAS
image = Image.open('fotos/armas/armas (2).jpg.rf.726496ca5e4a8e90337f56332fe00432.jpg')#1
#image = Image.open('fotos/armas/armas (15).jpg.rf.f52633782a3100f93d122151463773ca.jpg')#2

# IMAGEM DE PESSOAS
#image = Image.open('fotos/pessoas/image_59.jpg')#3
#image = Image.open('fotos/pessoas/image_64.jpg')#4

#redimensionar a imagem para 224x224 com a mesma estratégia do TM2:
#redimensionar a imagem para pelo menos 224 x 224 e depois cortar do centro
size = (600, 600)
image = ImageOps.fit(image, size, Image.ANTIALIAS)

# transforme a imagem em um array numpy
image_array = np.asarray(image)

# exibe a imagem redimensionada
image.show()

# Normaliza a imagem
#normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
normalized_image_array = (image_array.astype(np.float32) / 10.0) - 1
# Carregue a imagem no array
data[0] = normalized_image_array

# execute a inferência
prediction = model.predict(data)
print(prediction)



"""
a = (model.predict(X_test)>0.5).astype(int).ravel()
print(a)

reverse_pred = label_enc.inverse_transform(a.ravel())
print(reverse_pred)
"""

