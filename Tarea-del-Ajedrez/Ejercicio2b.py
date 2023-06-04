from interpreter import draw
from chessPictures import *
#Creo un caballo negativo
negativeK = knight.negative()
#Creo la primera linea con el caballo normal y con join agrego el caballo negativo
firstLine = knight.join(negativeK)
#Creo el caballo negativo invertido verticalmente
negativeInv = negativeK.verticalMirror()
#Creo la segunda linea con el caballo negativamente invertido y con 
#join agrego el caballo normal invertido verticalmente
secondLine = negativeInv.join(knight.verticalMirror())
#Con la función up agrego la primera linea y la segunda linea
result = firstLine.up(secondLine)

draw(result)
