from interpreter import draw
from chessPictures import *
#Formaremos los cuadrados verticales
image = Picture(square.negative().img+square.img).verticalRepeat(2)
#Juntamos la linea image con su negativo, repetimos 4 veces
result = image.join(image.negative()).horizontalRepeat(4)
draw(result)
