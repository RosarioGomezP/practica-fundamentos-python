nombre = input("Introduce tu nombre:")

# cadena de caracteres
print(f"Hola {nombre}")
print("Hola, {}!".format(nombre))

# entera
edad = 20
# flotante
altura = 1.63
# convertir flotante
edadString = str(edad)
boolleanos = False

print(edad + edad)
print(edadString + edadString)

print(type(edadString))

tuEdad = input("Introduce tu edad:")
tuEdad = int(tuEdad)

# estructura de control if
if tuEdad >= 18 and tuEdad < 100:
    print("Eres mayor de edad")
elif tuEdad >= 200:
    print("¿Eres inmortal?")
elif tuEdad <= 0:
    print("No existes")
else:
    print("Eres menor de edad")

# estructura de control for
for i in range(0,10):
    print(i)


