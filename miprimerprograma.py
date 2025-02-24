# Esto es un comentario de una sola línea
''' Este es un comentario de varias líneas
como podemos ver en este'''
# imprimir("Hola people")
print("Hola people")
# Se prueba en consola con python3 miprimerprograma.py
# Si utilizamos comillas simples, habrá que hacerlo en todo el programa
'''
Reglas de Python
No se usan llaves
No se usa ;
La indentation es obligatoria
Los comentarios se hacen con almohadillas o comillas simple
'''
x="El valor de la (a+b)*c es"
a,b,c=4,3,2
d=(a+b)*c
f=True
if f:
    print(x,d)
# Creando variables
x=y=z=10
print(x,y,z)
# Asignar valores
x,y=10,25
# Python siempre lee de arriba a abajo y de izquierda a derecha
'''
Para nombrar las variables de forma correcta:
_variable=10
vari_able=20
variable10=30
variable=40
variaBle=50

No son válidas:
2variable=10
var-iable=20
var iable=30
'''
'''
Palabras reservadas:
False,None,True,and,as,assert,break,class,continue,def,del,elif,else,except,finally,for,from,global,if,import,in,is,lambda,nonlocal,not,or,pass,raise,return,try,while,with,yield
'''
import keyword
print(keyword.kwlist)
# Constantes
PI=3.1416
print(PI)
# Funciones
def funcion():
    x=5
funcion()
print(x)
