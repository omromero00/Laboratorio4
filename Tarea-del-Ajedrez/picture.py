from colors import *
class Picture:
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):#""" Devuelve el espejo vertical de la imagen """
    vertical = []
    for value in self.img:
    	vertical.append(value[::-1])
    return Picture(vertical)

  def horizontalMirror(self):#""" Devuelve el espejo horizontal de la imagen """
    horizontal = []
    for tmp in self.img:
      horizontal.insert(0,tmp)
    return Picture(horizontal)

  def negative(self):#""" Devuelve un negativo de la imagen """
    negative = []
    iteration = '';
    for value in self.img:
      for char in value:
        iteration += self._invColor(char)
      negative.append(iteration)
      iteration = ''
    return Picture(negative)

  def join(self, p):#""" Devuelve una nueva figura poniendo la figura del argumento 
    joined = []#al lado derecho de la figura actual """
    position = 0
    for tmp in self.img:
      joined.append(tmp + "" +p.img[position])
      position += 1
    return Picture(joined)

  def up(self, p):
    image = self.img
    image.extend(p.img)
    return Picture(image)

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
  
  def horizontalRepeat(self, n):
    image = []#""" Devuelve una nueva figura repitiendo la figura actual al costado
    for i in range(0, len(self.img)):#la cantidad de veces que indique el valor de n """
      image.append(self.img[i] * n)
    return Picture(image)

  def verticalRepeat(self, n):
    VRepeat = []
    i = 0
    while i < n:
      i += 1
      for value in self.img:
        VRepeat.append(value)
    return Picture(VRepeat)

  #Extra: Sólo para realmente viciosos 
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

