# INFORME DE LABORATORIO 04
<div align="center">
<table>
    <theader>
        <tr>
            <td><img src="https://github.com/rescobedoq/pw2/blob/main/epis.png?raw=true" alt="EPIS" style="width:50%; height:auto"/></td>
            <th>
                <span style="font-weight:bold;">UNIVERSIDAD NACIONAL DE SAN AUGUSTIN</span><br />
                <span style="font-weight:bold;">FACULTAD DE INGENIERÍA DE PRODUCCIÓN Y SERVICIOS</span><br />
                <span style="font-weight:bold;">ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS</span>
            </th>
                  </tr>
    </theader>
    <tbody>
        <tr><td colspan="3"><span style="font-weight:bold;">Formato</span>: Guía del Estudiante / Talleres / Centros de Simulación</td></tr>
        <tr><td><span style="font-weight:bold;">Aprobación</span>:  2023/06/04</td><td><span style="font-weight:bold;">Código</span>: GUIA</td><td><span style="font-weight:bold;">Página</span>: 1</td></tr>
    </tbody>
</table>
</div>

<div align="center">
<span style="font-weight:bold;">GUÍA DEL ESTUDIANTE</span><br />
<span>(formato del estudiante)</span>
</div>


<table>
<theader>
<tr><th colspan="6">INFORMACIÓN BÁSICA</th></tr>
</theader>
<tbody>
<tr><td>ASIGNATURA:</td><td colspan="5">Programación Web 2</td></tr>
<tr><td>TÍTULO DE LA PRÁCTICA:</td><td colspan="5">Laboratorio 04</td></tr>
<tr>
<td>NÚMERO DE PRÁCTICA:</td><td>04</td><td>AÑO LECTIVO:</td><td>2023 A</td><td>NRO. SEMESTRE:</td><td>III</td>
</tr>
<tr>
<td>FECHA INICIO::</td><td>MAY-2023</td><td>FECHA FIN:</td><td>07-JUN-2023</td><td>DURACIÓN:</td><td>04 horas</td>
</tr>
<tr><td colspan="6">INTEGRANTE:
<ul>
<li>ROMERO CHIPANA OMAR -------------------- oromero@unsa.edu.pe</li>
</ul>
</td>
</<tr>
<tr><td colspan="6">DOCENTE:
<ul>
<li>Carlo CORRALES DELGADO</li>
</ul>
</td>
</<tr>
</tdbody>
</table>




<table>
<theader>
<tr><th colspan="6">SOLUCIÓN Y RESULTADOS</th></tr>
</theader>
<tbody>
</tr>
<tr><td colspan="6">
<tr>
#I. SOLUCIÓN DE EJERCICIOS PROBLEMAS:
A. <br><br>
-   verticalMirror: Devuelve el espejo vertical de la imagen.
    
```python
    def verticalMirror(self):#""" Devuelve el espejo vertical de la imagen """
        vertical = []
        for value in self.img:
    	    vertical.append(value[::-1])
        return Picture(vertical)
```
</tr>
<tr>
-   horizontalMirror: Devuelve el espejo horizontal de la imagen.

```python
  def horizontalMirror(self):#""" Devuelve el espejo horizontal de la imagen """
    horizontal = []
    for tmp in self.img:
      horizontal.insert(0,tmp)
    return Picture(horizontal)
```
</tr><tr>
-   negative: Devuelve un negativo de la imagen.

```python
  def negative(self):#""" Devuelve un negativo de la imagen """
    negative = []
    iteration = '';
    for value in self.img:
      for char in value:
        iteration += self._invColor(char)
      negative.append(iteration)
      iteration = ''
    return Picture(negative)
```
</tr><tr>
-   join: Devuelve una nueva figura poniendo la figura del argumento al lado derecho de la figura actual.

```python
  def join(self, p):#""" Devuelve una nueva figura poniendo la figura del argumento 
    joined = []#al lado derecho de la figura actual """
    position = 0
    for tmp in self.img:
      joined.append(tmp + "" +p.img[position])
      position += 1
    return Picture(joined)
```
</tr><tr>
-   up: Devuelve una nueva figura poniendo la figura recibida como argumento, encima de la figura actual.

```python
  def up(self, p):
    image = self.img
    image.extend(p.img)
    return Picture(image)
```
</tr><tr>
-   under: Devuelve una nueva figura poniendo la figura recibida como argumento, sobre la figura actual.

```python
  def under(self, p):#""" Devuelve una nueva figura poniendo la figura p sobre la
    image = []#figura actual """
    for i in range(0, len(p.img)):
      line = ""
      for j in range(0, len(p.img[i])):
        if (p.img[i][j] == " "):
          line += self.img[i][j]
        else:
          line += p.img[i][j]
      image.append(line)
    return Picture(image)
```
</tr><tr>
-   horizontalRepeat, Devuelve una nueva figura repitiendo la figura actual al costado la cantidad de veces que indique el valor de n.

```python
  def horizontalRepeat(self, n):
    image = []#""" Devuelve una nueva figura repitiendo la figura actual al costado
    for i in range(0, len(self.img)):#la cantidad de veces que indique el valor de n """
      image.append(self.img[i] * n)
    return Picture(image)
```
</tr><tr>
-   verticalRepeat Devuelve una nueva figura repitiendo la figura actual debajo, la cantidad de veces que indique el valor de n

```python
  def verticalRepeat(self, n):
    VRepeat = []
    i = 0
    while i < n:
      i += 1
      for value in self.img:
        VRepeat.append(value)
    return Picture(VRepeat)
```
</tr><tr>
-   #Extra: Sólo para realmente viciosos 

```python
  def rotate(self):#"""Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    rotate = []#o antihorario"""
    i = 0
    for value in self.img:
      rotate.append(value[0])
    while i < len(rotate):
      for value in self.img:
        rotate[i] += value[i]
      i += 1
    return Picture(rotate)
```
</tr>

## B. Usando únicamente los métodos de los objetos de la clase Picture dibuje las siguientes figuras (invoque a draw):<br>
</td><tr>

## Ejercicio2 a)

```python
from interpreter import draw
from chessPictures import *
#Creo un Picture de la imagen del caballo negro
negativeK= knight.negative()
#Creo en un Picture la primera linea incluyendo un caballo y el caballo negativo
firstLine = knight.join(negativeK)
#Creo en un Picture la segunda liena incluyenda el caballo negativo y el caballo
secondLine = negativeK.join(knight)
#Usando la funcion up de Picture, creo un Picture con la primera linea y la segunda linea
result = firstLine.up(secondLine)

draw(result)
```
![Ejercicio2a](Tarea-del-Ajedrez/resultados/Ejercicio2a.png)
</tr><tr><br>

## Ejercicio2 b)

```python
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
```
![Ejercicio2b](Tarea-del-Ajedrez/resultados/Ejercicio2b.png)
</tr><tr><br>

## Ejercicio2 c)

```python
from interpreter import draw
from chessPictures import *
#Hacemos una concatenación usando la función join de la clase picture, 4 veces
result = queen.join(queen.join(queen.join(queen)))
draw(result)
```

![Ejercicio2c](Tarea-del-Ajedrez/resultados/Ejercicio2c.png)
</tr><tr><br>

## Ejercicio2 d)

```python
from interpreter import draw
from chessPictures import *
#Juntaremos un cuadrado oscuro con uno claro y repetiremos 4 veces
result = square.join(square.negative()).horizontalRepeat(4)
draw(result)
```

![Ejercicio2d](Tarea-del-Ajedrez/resultados/Ejercicio2d.png)
</tr><tr><br>

## Ejercicio2 e)

```python
from interpreter import draw
from chessPictures import *
#Una linea del tablero, pero iniciando con oscuro
result = square.negative().join(square).horizontalRepeat(4)
draw(result)
```

![Ejercicio2e](Tarea-del-Ajedrez/resultados/Ejercicio2e.png)
</tr><tr><br>

## Ejercicio2 f)

```python
from interpreter import draw
from chessPictures import *
#Formaremos los cuadrados verticales
image = Picture(square.negative().img+square.img).verticalRepeat(2)
#Juntamos la linea image con su negativo, repetimos 4 veces
result = image.join(image.negative()).horizontalRepeat(4)
draw(result)

```

![Ejercicio2f](Tarea-del-Ajedrez/resultados/Ejercicio2f.png)
</tr><tr><br>

## Ejercicio2 g)

```python
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
```

![Ejercicio2g](Tarea-del-Ajedrez/resultados/Ejercicio2g.png)
</tr>


<tr><td colspan="6">II. SOLUCIÓN DE CUESTIONARIO: <br>

-   ¿Qué son los archivos *.pyc?: 
    Los archivos pyc son creados por el intérprete de python cuando compila. Estos archivos contienen el traductor bytecode que traduce el código a bytecode. Lo que permite que se pueda omitir a la segunda ejecución si se hace una primera. Son como los archivos class en java cuyo bytecode se encuentra dentro de este.

-   ¿Para qué sirve el directorio __pycache__?: 
    _pycache_ es un directorio donde se guardan las versiones simplificadas de nuestros archivos .py, estas versiones se ejecutan con mayor velocidad que las originales, ya que son archivos ya compilados y listos para ser ejecutados. Estos archivos son la versión 'Bytecode' de nuestros archivos python.

-   ¿Cuáles son los usos y lo que representa el subguión en Python?: 
    El guion bajo en python significa el tipo de comportamiento que tendrá una variable, clase o método, pudiendo variar de esta manera entre un guion bajo antes de la palabra, después o doble guiones antes y después. En el archivo de picture, se usa para el __init__,  al tener doble guion bajo a los costados se indica que es un método específico de python. 


</tr>
</tr>
<tr><td colspan="6">III. CONCLUSIONES:

-   Tras la realización de los ejercicios se concluye que, el uso de draw() es único, ya que nos permite crear el tablero de ajedrez como una sola imagen, a partir de concatenaciones, append, bucles, etc, y así poder utilizar draw() una sola vez.
-   El uso de los entornos virtuales en los proyectos es de suma importancia, ya que nos permite aislar las librerías que vamos a utilizar de otros entornos virtuales, esto lo podemos ver al agregar el módulo de pygame, que se añadía específicamente al entorno virtual en el que estabamos trabajando, y de esa manera funcionaban los imports de interpreter.py
-   Python es un lenguaje de programación que a diferencia de otros lenguajes, cuida su correcta compilación a travez de la sintaxis del código, donde la indentación toma mucha importancia. La sintaxis de este lenguaje a diferencia de java, es mucho más sencillo de entender y visualmente más cómodo. 
</tr>

</tdbody>
</table>


<table>
<theader>
<tr><th colspan="6">RETROALIMENTACIÓN GENERAL</th></tr>
</theader>
<tbody>
</tr>
<tr><td colspan="6">
<ul>
<li><a </a></li>
<li><a </a></li>
<li><a </a></li>
</ul>
</td>
</<tr>
</tdbody>
</table>


<table>
<theader>
<tr><th colspan="6">REFERENCIAS BIBLIOGRÁFICAS</th></tr>
</theader>
<tbody>
</tr>
<tr><td colspan="6">
<ul>
<li>https://www.tutorialspoint.com/What-are-pyc-files-in-Python#:~:text=pyc%20files%20are%20created%20by,is%20newer%20than%20the%20corresponding%20.</li>
<li>https://stackoverflow.com/questions/8822335/what-do-the-python-file-extensions-pyc-pyd-pyo-stand-for#:~:text=you've%20written.-,.,later%20easier%20(and%20faster).
</li>
<li>https://web.archive.org/web/20160130165632/http://www.network-theory.co.uk/docs/pytut/CompiledPythonfiles.html
</li>

<li></li>
</ul>
</td>
</<tr>
</tdbody>
</table>


