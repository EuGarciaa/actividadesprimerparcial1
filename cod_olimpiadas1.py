
#1 ronda 

def multi(a,b):
  x= a*b
  return x
print("deme un numero")
a= int(input())
print("deme otro numero")
b= int(input())
print("la division da", division(a,b), " y la multi da", multi(a,b))

#2 ronda

def conversion():
  print("cantidad de kilometros que quieras convertir")
  kilometros=input()
  print("te dare tus kilometros en metros")
  b=int(kilometros)/100
  print("el resultadoes",(metros))
  conversion()
  
def area_triangulo(base,altura):
  x= (base*altura)/2
  return x
print("deme la base de un triamgulo")
base= int(input())
print("deme la altura del triangulo")
altura= int(input())
print("su area de tu triangulo es", area_triangulo(base,altura))
