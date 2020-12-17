# DETECÇÃO DE CENAS POTENCIALMENTE PERIGOSAS
## Projeto da disciplina de inteligência artificial

### Descrição:
O repositório é uma api, que recebe apenas uma url de imagem, e retorna se aquela imagem apresenta perigo

### Blz, mas o que está rodando?:
Muitas libs, as principais são openCV e Keras.

### o que pretendo:
Disponibilizar uma api muito simples, aonde um usuário poderá usar em seu sistema de segurança local

### o que essa api faz:
Avalia se a pessoa está encapuzado, quantidade de pessoas e se possui armas na imagem

### blz, mas como usar:
#### 0: chame a url (http://servidor.inexistente.ainda/)
#### 1: escolha um link url de imagem e troque as barras "/" por "||" (use algum replace)
####    1.1: antes = "http://fotos.google/minha-imagem.jpg"
####    1.2 depois = "http:||||fotos.google||minha-imagem.jpg"
#### 2: passe o link já modificado como parâmetro após a última barra da url

### Ficaria algo assim:
url = "http://servidor.inexistente.ainda/http:||||fotos.google||minha-imagem.jpg"
