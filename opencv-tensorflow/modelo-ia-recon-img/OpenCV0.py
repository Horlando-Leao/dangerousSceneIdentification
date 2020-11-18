import cv2 

carregaAlgoritmo = cv2.CascadeClassifier("Haarcascade/haarcascade_frontalface_default.xml")

imagem = cv2.imread("./fotos/pessoa-1.jpg")

#DETECÇÃO DAS FACES
#DEFINE MINHA MATRIZ: X, Y , LARG, ALTU
faces = carregaAlgoritmo.detectMultiScale(imagem)

print(faces)

cv2.imshow("Faces", imagem)
cv2.waitKey()

