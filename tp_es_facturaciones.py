producto_1 = int(input("ingrese el valor del producto 1:"))
producto_2 = int(input("ingrese el valor del producto 2:"))
producto_3 = int(input("ingrese el valor del producto 3:"))

print(f"El precio del producto 1 es: {producto_1}")
print(f"El precio del producto 2 es: {producto_2}")
print(f"El precio del producto 3 es: {producto_3}")

suma1 = producto_1 + producto_2 + producto_3

print(f"La suma de los precios es: {suma1}")

promedio_precios = ((producto_1 + producto_2 + producto_3)/3)

print(f"El promedio de los precios es: {promedio_precios}")

suma_e_iva = ((producto_1 + producto_2 + producto_3)*1.21 )

print(f"La suma de los productos más el IVA da un total de: {suma_e_iva}")