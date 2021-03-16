import random 

lista = []

while len(lista) < 4 :
    nome = input("Digite o nome de um aluno: ")
    lista.append(nome)

escolhido = random.choice(lista)
print("O aluno escolhido foi {}".format(escolhido))