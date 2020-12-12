""" 
#importação do flask no py3.7
from flask import Flask, request
app = Flask("SecView-IA")

from src.controllers.handilingAuto import handiling_auto as hand_a
#from src.controllers.handilingControl import handiling_control as hand_c

#rotas com método GET
@app.route("/olamundo/<string:user>", methods=["GET"])
def olaMundo(user: str) -> str:
    return {"Olá":"{0}".format(user)}

#rota com método POST
@app.route("/alertas", methods=["POST"])
def cadastraUsuario():
    
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

#Rodar api - aplicações
app.run() """