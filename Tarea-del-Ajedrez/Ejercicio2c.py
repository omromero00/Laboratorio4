from interpreter import draw
from chessPictures import *
#Hacemos una concatenación usando la función join de la clase picture, 4 veces
result = queen.join(queen.join(queen.join(queen)))
draw(result)
