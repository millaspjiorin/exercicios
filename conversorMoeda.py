reais = float(input("Quantos reais você tem na carteira? R$ "))

dolar = reais / 5.61
euro = reais / 6.69

print ("Com R${} você pode comprar US${:.2f} ou €{:.2f}.".format(reais, dolar, euro))