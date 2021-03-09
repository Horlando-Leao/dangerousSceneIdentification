#importação do flask no py3.7
import sys
sys.path.append("src\controllers")
from flask import Flask, request
from urllib.request import urlopen

from handiling import handiling_auto
from handiling import handiling_control

app = Flask("SecView-IA")

def valid_url(url_valid:str =False)-> bool:
    """VALIDA A DISPONIBILIDADE DO SERVIDOR"""
    try:
        if ( isinstance(url_valid, str) ):
            url = urlopen(url_valid)
            return True
        else:
            return False
    except Exception as e:
        #print("Servidor indisponível. Erro:", e)
        return False

def array_to_string(array) -> str:
    """TRANFORMA UM ARRAY EM STRING SEPARADOS POR  '|' """
    divider = "|"
    seq = (str(array[0]), str(array[1]), str(array[2]), str(array[3]))
    return ( divider.join(seq) )

#rota de teste
@app.route("/olamundo/<string:user>", methods=["GET"])
def olaMundo(user: str) -> str:
    return {"Olá":"{0}".format(user)}


@app.route("/detectartudo/<string:url>", methods=["GET"])
def detect_no_treat(url):
    
    url = url.replace("||", "/")

    if(valid_url(url) == False):
        return response_generator( 400, "o parametro (url) é obrigatório")

    result = handiling_auto(url)
    return response_generator(200, "Imagem processada com sucesso", str(result[0]), str(result[1]), str(result[2]), str(result[3]))

#trabalhar com todas as respostas das rotas
def response_generator(status: int, mensage: str, quatPeople:str ="", quatFaces:str = "", probilidGun:str = "", noProbilidGun:str = "" ):

    response = {}
    response["status"] = status
    response["mensagem"] = mensage
    response["pessoas"] = quatPeople
    response["faces"] = quatFaces
    response["probabilidadeArma"] = probilidGun
    response["probabilidadeNaoSerArma"] = noProbilidGun
    return (response)


#Rodar api
if __name__ == "__main__":
    app.run()