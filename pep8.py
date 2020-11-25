#ANOTAÇÕES DE TIPO
def sum_two_numbers(a: int, b: int) -> int:
    "Retorn a soma de a + b"
    return a + b

results: [str, int] = {
    "result_sum_1" : sum_two_numbers(5, 5),
    "result_sum_2" : sum_two_numbers(10, 5)
}

print(results)

##GERENCIADORES DE CONTEXTO

#NORMAL
data = open("meu_arquivo.txt")
data.close

#COM GERENCIADORES DE CONTEXTO
with open("meu_arquivo.txt") as data:
#faça algunha coisa

"""ao sair do contexto, ele fecha"""
