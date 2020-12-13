""" import sys
sys.path.append("src\controllers")
from handiling import handiling_auto
from handiling import handiling_control


url = "https://cdn-istoe-ssl.akamaized.net/wp-content/uploads/sites/14/2019/01/e7f66c0f0c153eba4cbf868f5eccab26632176e2.jpg"
print(handiling_control(url, faces=False, bodys=False, guns=True)) """

""" from urllib.request import urlopen

def valid_url(url_valid:str =False)-> bool:

    try:
        if ( isinstance(url_valid, str) ):
            url = urlopen(url_valid)
            return True
        else:
            return False
    except Exception as e:
        #print("Servidor indisponível. Erro:", e)
        return False """

""" def array_to_string(array) -> str:
    divider = "|"
    seq = (str(array[0]), str(array[1]), str(array[2]), str(array[3]))
    return ( divider.join(seq) )
 """

""" from urllib.request import urlopen
try:
    url = urlopen("//image.freepik.com/fotos-gratis/pessoas-andando-agarrado-por-ombros_1139-456.jpg")
    print(url)
except Exception as identifier:
    print("erro", identifier)
 """

str1 = "https://image.freepik.com/fotos-gratis/pessoas-andando-agarrado-por-ombros_1139-456.jpg"
str2 = str1.replace("/", "||")
print(str2)

str3 = str2.replace("||", "/")
print(str3)


