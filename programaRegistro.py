#RETOMANDO ASPECTOS BASICOS DE PYTHON   
def validacionEdad():
    #Imprimir nombre
    nombre = input("Introduce tu nombre:")
    #Concatenacion: poner una variable junto con un texto plano
    print(f"Hola {nombre}") 
    print("Hola {}".format(nombre))
    print("Hola ",nombre)

    #Introducimos edad
    #Entero
    edad = input("Ahora introduce tu edad:")

    #Flotante
    estatura = 1.76

    #Convertir flotante
    edadString = str(edad)

    #BooleanoS
    booleanos = False

    print(type(edad)) #Imprimir el tipo de dato en python

    #Transformar string a entero

    edad = int(edad)

    #Estructura de control
    if edad >= 18 and edad <= 100:
        print("Hola {} pasale por tu tonayán".format(nombre))
    elif edad >= 100:
        print("¿A caso eres chavelo?")
    elif edad <= 0:
        print("No existe")
    else:
        print("Tas bebe")

while True:
    validacionEdad()       