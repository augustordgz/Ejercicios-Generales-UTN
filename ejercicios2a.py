#1

num_1 = int(input("Ingrese su edad: "))
if num_1 == 18 :
    print("Usted tiene 18 años")

#2

num_2 = int(input("Ingrese su edad: "))
if num_2 >= 18 :
    print("MAYOR")
else : 
    print("MENOR")

#3

altura = float(input("Ingrese su altura en metros: "))
if altura >= 1.80 :
    print("Es pivot")

#4

num_3 = int(input("Ingrese su edad: "))
if num_3 >= 13 and num_3 <= 17 :
    print("Sos adolescente")

#5

num_4 = int(input("Ingrese su edad: "))
if num_4 < 10 :
    print("Sos niño/a")
elif num_4 >= 10 and num_4 < 13 :
    print("Sos pre-adolescente")
elif num_4 >= 13 and num_4 <= 17 :
    print("Sos adolescente")
elif num_4 >= 18 :
    print("Sos mayor de edad")