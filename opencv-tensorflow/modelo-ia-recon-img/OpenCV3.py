import cv2 

carregaAlgoritmo = cv2.CascadeClassifier("Haarcascade/haarcascade_frontalface_default.xml")

imagem = cv2.imread("./fotos/pessoa-2.jpg")

#Por recomendação o OpenCV diz para usar a img escala de cinza
#A efetividade dele é maior dessa forma
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

#DETECÇÃO DAS FACES
#DEFINE MINHA MATRIZ: X, Y , LARG, ALTU
faces = carregaAlgoritmo.detectMultiScale(imagemCinza)

#AUMENTAR ACURACIA NOS PARÂMETROS
"""
detectMultiScale(
    const Mat& image,  vector<Rect>& objects, 
    double scaleFactor=1.1, int minNeighbors=3, 
    int flags=0, Size minSize=Size(), Size maxSize=Size() )
"""


print(faces)
#INDETIFICAR OS PONTOS QUE detectMultiScale CAPTROU DAS IMG
for(x, y, l, a) in faces:
    #crie um retangulo nas faces que detectMultiScale localizou
    cv2.rectangle( imagem, ( x , y ), ( x + l, y + a ),( 0, 255, 0 ), 2 )



cv2.imshow("Faces", imagem)
cv2.waitKey()

