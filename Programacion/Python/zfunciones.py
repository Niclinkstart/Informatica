#Conjunto de lineas de codigo agrupados, es un bloque de codigo, que funcionan como
#una unidad realizando una tarea especifica
#Las funciones en python pueden de volver valores
#Las funciones pueden tener parametros/argumentos
#A las funciones tambien se los denomina metodos cuando se encuentran definidos en una clase
#en la programacion orientada a objetos
#Utilidad
#Reutilizacion de codigo(cuando sea necesario o si es necesario)

#Sintaxis

def Message():
    print("Hola mi nombre es Nicolas")
    print("Bienvenido a la Fju de Once")
    print("Se feliz de verdad")

Message()
Message()
print("se puede ejecutar codigo fuera de la funcion")
Message()    

#Funciones con Parametros
def suma(num1, num2):
    print(num1+num2)
suma(5,7)
suma(5,5)

#Maquina de Golosinas
#Porque una funcion que devuelve o retorna un valor tiene el mismo funcionamiento.
num3=int(input("Ingrese un valor"))
num4=int(input("Ingrese el segundo valor"))
def operacion(num3, num4):
    resultado=num3+num4
    return resultado
resultado_de_la_suma=operacion(num3, num4)

if operacion(5,6):
    print("Papitas")
    print(resultado_de_la_suma)
elif operacion(6,5):
    print("pepsi")
    print(resultado_de_la_suma)
elif operacion(5,3):
    print(resultado_de_la_suma)
    print(operacion)
else:
    print("no existe")
#El uso del return tu puedes almacenar en una variable lo que nos devuelve la funcion.
