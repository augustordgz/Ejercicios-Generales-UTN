#Actividad Práctica 1A

#1

nombre_usuario = str(input("Nombre de usuario: "))
print(f"Hola {nombre_usuario}")

#2

variable_a = int(input("Ingrese el primer número: "))
variable_b = int(input("Ingrese el segundo número: "))
print(variable_a + variable_b)

#3

nombre = str(input("Ingrese su nombre: "))
apellido = str(input("Ingrese su apellido: "))
edad = int(input("Ingrese su edad: "))

print(f"El nombre ingresado fue: {nombre}, el apellido ingresado fue: {apellido} y la edad ingresada fue: {edad}")

#4

nombre_2 = str(input("Ingrese su nombre: "))
comision = int(input("Ingrese el número de su comisión: "))
asignatura = str(input("Ingrese su asignatura: "))
docente = str(input("Ingrese el nombre del docente: "))
presente = str(input("¿Estuvo presente?: "))

print(f"{nombre}, de la comisión {comision}, Asignatura: {asignatura}, Docente: {docente}, ¿estuvo presente? {presente}")

#5 

lado_cuadrado = int(input("Lado de un cuadrado: "))
superficie = lado_cuadrado * lado_cuadrado
print(superficie)

#6

largo_rectangulo = int(input("Largo del rectangulo: "))
ancho_rectangulo = int(input("Ancho lado del rectangulo: "))
superficie_rectangulo = largo_rectangulo * ancho_rectangulo
print(superficie_rectangulo)

#7

base_triangulo = int(input("Base del triangulo: "))
altura_triangulo = int(input("Altura del triangulo: "))
superficie_triangulo = ((base_triangulo * altura_triangulo) / 2)
print(superficie_triangulo)

#8

nombre_producto = str(input("Ingrese el nombre del producto: "))
precio_producto = int(input("Ingrese el precio del producto: "))
iva = precio_producto * 0.21
print(f"El IVA que contiene el producto '{nombre_producto}' es de: {iva} ")

#9

nombre_y_apellido = str(input("Ingrese su nombre y apellido: "))
nota_1 = int(input("Ingrese la primer nota: "))
nota_2 = int(input("Ingrese la segundo nota: "))
nota_3 = int(input("Ingrese la tercer nota: "))
promedio_notas = ((nota_1 + nota_2 + nota_3) / 3)
print(promedio_notas)

#10

usuario_nombre = str(input("Ingrese su nombre: "))
usuario_edad = int(input("Ingrese su edad: "))
edad_10años = usuario_edad + 10
print(f"Usted en 10 años tendra la edad de: {edad_10años}")