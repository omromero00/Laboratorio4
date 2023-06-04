from interpreter import draw
from chessPictures import *
#Juntaremos un cuadrado oscuro con uno claro y repetiremos 4 veces
result = square.join(square.negative()).horizontalRepeat(4)
draw(result)
