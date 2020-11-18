#DETECÇÃO DE 
import cv2 

carregaAlgoritmo = cv2.CascadeClassifier("Haarcascade/haarcascade_frontalface_default.xml")

imagem = cv2.imread("./fotos/pessoa-2.jpg")
imagem = cv2.resize(imagem, (0,0), fx=0.7, fy=0.7) 
#IMAGEM CINZA
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

#DETECÇÃO DAS FACES
#DEFINE MINHA MATRIZ: X, Y , LARG, ALTU
faces = carregaAlgoritmo.detectMultiScale(
    imagemCinza, 
    scaleFactor=1.1, 
    minNeighbors=3,  #abordagem de vizihança, (^) = + perder os verdadeiros positivos, (v) = + falsos positivos
    minSize=(20,20) #tamanho da detecção de uma face
    )

print(faces)


#INDETIFICAR OS PONTOS QUE detectMultiScale DETECTOU DAS IMG
for(x, y, l, a) in faces:
    #crie um retangulo nas faces que detectMultiScale localizou
    cv2.rectangle( imagem, ( x , y ), ( x + l, y + a ),( 0, 255, 0 ), 2 )



cv2.imshow("Faces", imagem)
cv2.waitKey()







