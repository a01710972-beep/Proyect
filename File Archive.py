"""
Proyecto python
Filtrador de Archivos.
El programa ordena los archivos por diferentes tipos de métodos, ya sea por orden alfabético, 
tema de archivo y el archivo más reciente al más antiguo.
Se le pedirá al usuario que ponga el nombre de sus archivos (máximo 5) con el nombre de su elección 
siempre y cuando este tenga en su terminación el tema de este (ej. escuela, trabajo, etc.).
Al final, el usuario debería poder buscar sus archivos previamente guardados por cualquiera
de los 3 métodos existentes. 
"""
#bibliotecas

print("Hola, buen día, hoy filtraremos tus archivos por ti :) \n")
print("NOTA: Favor de escribir el nombre de cada archivo sin utilizar números")
archivo_1 = str(input("Por favor escriba el nombre de su primer archivo: "))
archivo_2 = str(input("Por favor escriba el nombre de su segundo archivo: "))
archivo_3 = str(input("Por favor escriba el nombre de su tercer archivo: "))
archivo_4 = str(input("Por favor escriba el nombre de su cuarto archivo: "))
archivo_5 = str(input("Por favor escriba el nombre de su quinto archivo: "))

lista_archivos_usuario = [archivo_1, archivo_2, archivo_3, archivo_4, archivo_5]

print("\n Elige el número de método por el cual quieres que organizemos tus archivos, las opciones son las siguientes:")
lista_metodos = ("(1) Orden Alfabético", "(2) Orden por tema", "(3) Orden por tiempo")
for i in lista_metodos:
    print(i)
    
metodo_usuario = int(input())
while metodo_usuario not in [1,2,3]:
    print("No es una opción valida, por favor intente de nuevo")
    metodo_usuario = int(input())

"""
================= Funciones de filtrado por metodo alfabetico =================
"""
if metodo_usuario == 1:  
    print("\n Aquí esta su lista por orden alfabético:" )
    
    archivo = lista_archivos_usuario.sort()
    for archivo in lista_archivos_usuario:
        print(archivo)
      
"""
================= Funciones de filtrado por tema =================
"""
if metodo_usuario == 2:  
    print("\n Aquí esta su lista por tema:" )
    print("Característica en desarrollo, favor de esperar hasta nuestro siguiente parche.")

"""
Tomando el tipo de archivo, estos se classificarán de acuerdo a este
recibe: val_1 valor string, val_2 valor string, val_3 valor string.
val_4 valor string, val_5 valor string
devuelve: conjunto por palabra clave (ej. trabajo)
Usar ifs, tipo, 
if nombre_de_archivo contiene palabra "trabajo"
cuando el usuario busque por palabra "trabajo"
print(nombre_de_archivo)
"""
"""
================= Funciones de filtrado por tiempo (números) =================
"""
para_resta = 5

val_1 = 1
val_2 = 2
val_3 = 3
val_4 = 4
val_5 = 5

def evalua_resta(para_resta, val_1):
    resultado1 = para_resta - val_1
    return resultado1
res1 = evalua_resta(para_resta, val_1)

def evalua_resta1(para_resta, val_2):
    resultado2 = para_resta - val_2
    return resultado2
res2 = evalua_resta1(para_resta, val_2)

def evalua_resta2(para_resta, val_3):
    resultado3 = para_resta - val_3
    return resultado3
res3 = evalua_resta2(para_resta, val_3)

def evalua_resta3(para_resta, val_4):
    resultado4 = para_resta - val_4
    return resultado4    
res4 = evalua_resta3(para_resta, val_4)

def evalua_resta4(para_resta, val_5):
    resultado5 = para_resta - val_5
    return resultado5
res5 = evalua_resta4(para_resta, val_5)

#NOTA!!!!
#En la siguiente parte solo investigue como ponerle color al texto, no afecta en nada al programa más allá de darle color al texto
ROJO = '\033[31m'
AZUL = '\033[34m'
VERDE = '\033[32m'
RESET = '\033[0m'

if metodo_usuario == 3:
    print("\n Aquí esta su lista por tiempo:\n")
    
    if res1 > 2:
        print(archivo_1, f"{ROJO}antiguo{RESET}")
    if res2 > 2:
        print(archivo_2, f"{ROJO}antiguo{RESET}")
    if res3 == 2:
        print(archivo_3, f"{AZUL}hace un rato{RESET}")
    if res4 < 2:
        print(archivo_4, f"{VERDE}reciente{RESET}")
    if res5 < 2:
        print(archivo_5, f"{VERDE}reciente{RESET}")

"""
======================================================================================================
"""


print("\n Desea intentar organizar sus archivos por otro método?")
print("Y/N?")
ans = input()

while ans not in ["Y","y","N","n"]:
    ans = input("Lo siento, no entendimos tu respuesta, favor de intentar de nuevo con una respuesta de Y/N: ")

if ans in ["N","n"]:
    print("Gracias por usar el programa, adiós :D")
    
elif ans in ["Y","y"]:
    metodo_usuario = 0
    while metodo_usuario == 0:
        metodo_usuario = int(input("¿Qué método desea utilizar esta vez? (1), (2), o (3)? "))
        if metodo_usuario in [1,2,3]:
            print("Lo sentimos, esta acción aun no esta disponible, esperamos que esta caracteristica este disponible en nuestro siguiente parche, gracias por su comprensión :)")       
        elif metodo_usuario not in [1,2,3]:
            print("No se ha seleccionado una opción valida. Favor de intentar de nuevo.")
            metodo_usuario = metodo_usuario * 0
