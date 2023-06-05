from interpreter import draw
from chessPictures import *
#Piezas en su versión negativa
torreNegra = rock.negative()
caballoNegro = knight.negative()
alfilNegro = bishop.negative()
reynaNegra = queen.negative()
reyNegro = king.negative()
peonNegro = pawn.negative()
cuadradoNegro = square.negative()
#Ponemos todas las fichas negras en diferentes cuadrados (CC:claro, CO: oscuro)
torreNegraCC = square.under(torreNegra)
caballoNegroCC = square.under(caballoNegro)
alfilNegroCC = square.under(alfilNegro)
peonNegroCC = square.under(peonNegro)
torreNegraCO = cuadradoNegro.under(torreNegra)
caballoNegroCO = cuadradoNegro.under(caballoNegro)
alfilNegroCO = cuadradoNegro.under(alfilNegro)
peonNegroCO = cuadradoNegro.under(peonNegro)
#Ponemos las fichas blancas en diferentes cuadrados (CC: claro, CO: oscuro)
torreBlancaCC = square.under(rock)
caballoBlancoCC = square.under(knight)
alfilBlancoCC = square.under(bishop)
peonBlancoCC = square.under(pawn)
torreBlancaCO = cuadradoNegro.under(rock)
caballoBlancoCO = cuadradoNegro.under(knight)
alfilBlancoCO = cuadradoNegro.under(bishop)
peonBlancoCO = cuadradoNegro.under(pawn)
#Posicionamos a la reyna negra en un cuadrado oscuro
reynaNegra = cuadradoNegro.under(reynaNegra)
#Posicionamos al rey negro en un cuadrado claro
reyNegro = square.under(reyNegro)
#Posicionamos a la reyna blanca en un cuadrado claro
reynaBlanca = square.under(queen)
#Posicionamos al rey blanco en un cuadrado oscuro
reyBlanco = cuadradoNegro.under(king)
#Generamos cada una de las filas del tablero
fila1 = torreNegraCC.join(caballoNegroCC).join(alfilNegroCC).join(reynaNegra).join(reyNegro).join(alfilNegroCO).join(caballoNegroCC).join(torreNegraCO)
fila2 = (peonNegroCO.join(peonNegroCC)).horizontalRepeat(4)
aux1 = (square.join(cuadradoNegro).horizontalRepeat(4)) #Para las lineas que se repetiran.
aux2 = aux1.verticalMirror()
fila3a6 = aux1.up(aux2).verticalRepeat(2)
fila7 = (peonBlancoCC.join(peonBlancoCO)).horizontalRepeat(4)
fila8 = torreBlancaCO.join(caballoBlancoCC).join(alfilBlancoCO).join(reynaBlanca).join(reyBlanco).join(alfilBlancoCC).join(caballoBlancoCO).join(torreBlancaCC)

result = fila1.up(fila2.up(fila3a6.up(fila7.up(fila8))))
draw(result)
