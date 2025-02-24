# 24022025_Donato_Ramos_Martínez
'''
Crear un programa que almacene información sobre un producto
nombre, precio, cantidad en stock
y muestre un mensaje indicando si el producto está disponible 
(si la cantidad en stock es mayor que cero)
'''
nombre_producto="Laptop"
precio=1200.60
cantidad_stock=5
if cantidad_stock>0:
    print(f"El producto ",nombre_producto," está disponible")
else:
    print(f"El producto",nombre_producto," no está disponible")
# fin del programa
# Condicionales (if,else,elif)
'''
Tomar decisiones según las condiciones
Crear un programa que simule un sistema de acceso. Pide al usuario que ingrese su nombre y contraseña
Si el nombre es "admin" y la contraseña es "1234" permite el acceso; de lo contrario muestra un
mensaje de error
'''
usuario=input("Ingrese su nombre de usuario: ")
contrasena=input("Ingrese su contraseña: ")
if usuario=="admin" and contrasena=="1234":
    print("Acceso concedido")
else:
    print("Acceso denegado")