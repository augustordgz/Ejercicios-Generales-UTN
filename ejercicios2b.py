#1 

numeros_pares = [2,4,6,8]
for i in numeros_pares:
    suma = numeros_pares[0] + numeros_pares[1] + numeros_pares[2] + numeros_pares[3]
    print(f"La suma de los números pares es: {suma}")
    break


#2

contraseña = str(input("Ingrese una contraseña:"))
while contraseña != "utn750" :
    print("Contraseña incorrecta, vuelva a intentarlo")
    contraseña = str(input("Ingrese una contraseña:"))
else :
    print("Contraseña correcta")

#3

numero = int(input("Ingrese un número:"))
while numero < 0 or numero > 9:
    print("No validado, vuelva a intentarlo")
    numero = int(input("Ingrese un número:"))
else :
    print("Validado")

#4

letra = input("Ingrese una letra:")
while letra != "U" and letra != "T" and letra != "N":
    letra = input("No validado, ingrese nuevamente una letra:")
else :
    print("Validado")

#5

num1 = int(input("Ingrese el primer número:"))
num2 = int(input("Ingrese el segundo número:"))
num3 = int(input("Ingrese el tercer número:"))
num4 = int(input("Ingrese el cuarto número:"))
num5 = int(input("Ingrese el quinto número:"))
suma = (num1 + num2 + num3 + num4 + num5)
promedio = ((num1 + num2 + num3 + num4 + num5) / 5)

print(f"La suma de los números {num1}, {num2}, {num3}, {num4} y {num5} es: {suma}")
print(f"El promedio de los números ingresados es: {promedio}")