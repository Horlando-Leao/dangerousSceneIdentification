import cv2 

carregaAlgoritmo = cv2.CascadeClassifier("Haarcascade/haarcascade_frontalface_default.xml")

imagem = cv2.imread("./fotos/pessoa-1.jpg")

#Por recomendação o OpenCV diz para usar a img escala de cinza
#A efetividade dele é maior dessa forma
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

#DETECÇÃO DAS FACES
#DEFINE MINHA MATRIZ: X, Y , LARG, ALTU
faces = carregaAlgoritmo.detectMultiScale(imagemCinza)



print(faces)
#INDETIFICAR OS PONTOS QUE detectMultiScale CAPTROU DAS IMG
#faces[0] = X, faces[1] = Y, faces[2] = L, faces[3] = A
cv2.rectangle( imagem, ( faces[0], faces[1] ), ( faces[0] + faces[2], faces[1] + faces[3] ),( 0, 255, 0 ),2)



cv2.imshow("Faces", imagem)
cv2.waitKey()

