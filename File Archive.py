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

print("Hola, buen día, hoy filtraremos tus archivos por ti :)")

val_1_ = input("Por favor escriba el nombre de su primer archivo: ")
val_2_ = input("Por favor escriba el nombre de su segundo archivo: ")
val_3_ = input("Por favor escriba el nombre de su tercer archivo: ")
val_4_ = input("Por favor escriba el nombre de su cuarto archivo: ")
val_5_ = input("Por favor escriba el nombre de su quinto archivo: ")

print("Elige el número de método por el cual quieres que organizemos tus archivos, las opciones son las siguientes:")
lista = ("(1) Orden Alfabético", "(2) Orden por tema", "(3) Orden por tiempo")
for i in lista:
    print(i)
    
metodo = int(input())
while metodo not in [1,2,3]:
    print("No es una opción valida, por favor intente de nuevo")
    metodo = int(input())

"""
================= Funciones de filtrado por metodo alfabetico =================
"""
"""
Dependiendo de la primera letra del archivo se desplazará la lista de estos
recibe: val_1 valor string, val_2 valor string, val_3 valor string.
val_4 valor string, val_5 valor string
devuelve: lista de elementos por orden alfabetico
"""
while metodo == 1:  
    print("Aquí esta su lista por orden alfabético:" )
    print("Característica en desarrollo, favor de esperar hasta nuestro siguiente parche.")
    break
      

"""if val_1  ---       #Aun no se como ponerle que filtre por letra inicial, I'll figure it out eventually
print(val_1)
if val_1  ---
print(val_2)
if val_1  ---
print(val_3)
if val_1  ---
print(val_4)
if val_1  ---
print(val_5)
"""

"""
================= Funciones de filtrado por tema =================
"""
while metodo == 2:  
    print("Aquí esta su lista por tema:" )
    print("Característica en desarrollo, favor de esperar hasta nuestro siguiente parche.")
    break
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
"""
A los datos que el usuario introduzca se les asigna un valor numérico.
(uso de operadores)
recibe: val_1 valor númerico, val_2 valor númerico, val_3 valor númerico,
val_4 valor númerico, val_5 valor númerico
resta 5 a cada valor
devuelve: los valores ordenados de acuerdo a que tan grande es el número final
"""
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

"""
Dependiendo del valor de la resta, se clasificará el archivo como "reciente", "hace un rato",
y "antiguo"
En este caso: x < 2 
devuelve: antiguo
x == 2
devuelve: hace un rato
x > 2
devuelve: reciente
"""
#NOTA!!!!
#En la siguiente parte solo investigue como ponerle color al texto, no afecta en nada al programa más allá de darle color al texto
ROJO = '\033[31m'
AZUL = '\033[34m'
VERDE = '\033[32m'
RESET = '\033[0m'

while metodo == 3:
    print("Aquí esta su lista por tiempo:")
    
    if res1 > 2:
        print(val_1_, f"{ROJO}antiguo{RESET}")
    if res2 > 2:
        print(val_2_, f"{ROJO}antiguo{RESET}")
    if res3 == 2:
        print(val_3_, f"{AZUL}hace un rato{RESET}")
    if res4 < 2:
        print(val_4_, f"{VERDE}reciente{RESET}")
    if res5 < 2:
        print(val_5_, f"{VERDE}reciente{RESET}")
    break
"""
======================================================================================================
"""


print("Desea intentar organizar sus archivos por otro método? Y/N")
ans = input("Y/N? ")

while ans not in ["Y","y","N","n"]:
    ans = input("Lo siento, no entendimos tu respuesta, favor de intentar de nuevo con una respuesta de Y/N: ")

if ans in ["N","n"]:
    print("Gracias por usar el programa, adiós :D")
    
elif ans in ["Y","y"]:
    metodo = 0
    while metodo == 0:
        metodo = int(input("¿Qué método desea utilizar esta vez? (1), (2), o (3)? "))
        if metodo in [1,2,3]:
            print("Lo sentimos, esta acción aun no esta disponible, esperamos que esta caracteristica este disponible en nuestro siguiente parche, gracias por su comprensión :)")       
        elif metodo not in [1,2,3]:
            print("No se ha seleccionado una opción valida. Favor de intentar de nuevo.")
            metodo = metodo * 0
