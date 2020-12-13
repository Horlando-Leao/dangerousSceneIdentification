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


@app.route("/alerta/semtratamento/<string:url>", methods=["GET"])
def detect_no_treat(url):
    
    url = url.replace("||", "/")

    if(valid_url(url) == False):
        return geraResponse( 400, "o parametro (url) é obrigatório")

    
    result = handiling_auto(url)
    
    result_str = array_to_string(result)

    return geraResponse(200, "Imagem processada com sucesso", "deteção", result_str)


@app.route("/alerta/comtratamento/<string:url>", methods=["GET"])
def detect_with_treat(url):
    
    #o corpo é igual a requisição feita pelo cliente em formato json
    body = request.get_json()

    #verificar se o nome foi passado no corpo da requisição
    if("nome" not in body):
        return geraResponse( 400, "o parametro (nome) é obrigatório")
    
    #chamar a função desejada
    #no meu caso, chamei a função para inserir um usuario, passando tudo que peguei no corpo da requisição do cliente
    usuario = [body["nome"], body["email"], body["senha"]]

    # na minha função coloquei um retorno se o usuario foi inserido corretament na base.
    #por padrão: se sim status code:200, se não, status code:400.
    #e mais algunha mensagem de preferência do desenvolvedor.
    return geraResponse(200, "Usuário inserido", "user", usuario)

#trabalhar com todas as respostas das rotas
def geraResponse(status: int, mensagem: str, nomeConteudo:str =False , conteudo:str =False ):
    response = {}
    response["status"] = status
    response["mensagem"] = mensagem

    #verificar se o conteudo foi inserido
    if(nomeConteudo and conteudo):
        response[nomeConteudo] = conteudo

    return (response)

#Rodar api
if __name__ == "__main__":
    app.run()