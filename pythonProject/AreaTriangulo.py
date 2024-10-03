#Ejemplo para calcular area del triangulo
from array import array

#Variables de entrada
base = int(input("ingrese la base: " ))
altura = int(input("ingrese la altura: "))

#Proceso
def calcularAreaTriangulo(b,a):
    area = (b*a/2)
    return area

#Invocar funcion
resultado = calcularAreaTriangulo(base,altura)

#salida
print(f"El area del triangulo cuya {base} y altura {altura} es : {resultado}")

#Funcion con argumentos predeterminados
def my_function(contry = "colombia"):
    print("I am from "+contry)

#invocar funcion
my_function()
my_function("sweden")

#Argumentos arbitrarios
def mostrarEstudiantes(*args):
    print("El estudiante: "+args[2])

#invocamos funcion
mostrarEstudiantes("Emil","Tobias","Linus","Bill","Andres")

#Clave valor

def mostrarCarroa(carro1,carro2,carro3):
    print("El carro es : "+carro2)

mostrarCarroa(carro1="BM2w", carro3="Ferrari", carro2 = "Ford")

#Cuando no se sabe el argumentos clave = valor

def mostrarCliente(**kwargs):
    print("su apellido es :" + kwargs["telefono"])

mostrarCliente(nombre= "Tobias", apellido= "Refsnes", telefono = "300212850")

#de paso

def miFuncion():
    pass

#Ejemplo funciones integradas

x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

#potencia

num1 = pow(7, 4)

print(num1)

#import

import math

num2 = math.sqrt(34)

print(num2)

#redondea numero

import math
num3 = math.ceil(7.8)
num4 = math.floor(7.8)

print(num3) #return8
print(num4) #return7