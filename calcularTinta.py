largura = float (input("Qual a largura da parede? ")) 
altura =  float (input ("Qual a altura da parede? "))

area = largura * altura
tinta = area/2

print ("A área total da parede é de {:.2f}, portanto será necessário {} litros de tinta para pintar.".format(area, tinta))