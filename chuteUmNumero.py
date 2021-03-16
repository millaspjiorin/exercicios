# Objetivo: criar um programa onde o usuário deve adivinhar o número gerado aleatóriamente pelo computador


# Importando método randint da biblioteca random
from random import randint

# Criando objeto que recebe o valor sorteado 
sorteado = randint(1,30)
numero = 0

# Laço de repetição para que o usuário digite um número até acertar
while numero != sorteado:
    numero = int(input ("Adivinhe o número de 1 a 30: "))
    # Garantindo que o usuário digitou um número dentro do range solicitado
    if numero > 30 or numero == 0:
        print("Você deve digitar um número válido")
    else:
        if numero > sorteado:
            print (f"O número {numero} é maior que o número sorteado, tente um número menor")
        elif numero < sorteado:
            print (f"O número {numero} é menor que o número sorteado, tente um número maior")
        else:
            print ("Parabéns, você acertou o número sorteado pelo computador! :)")