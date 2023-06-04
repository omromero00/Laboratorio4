from interpreter import draw
from chessPictures import *
#Una linea del tablero, pero iniciando con oscuro
result = square.negative().join(square).horizontalRepeat(4)
draw(result)