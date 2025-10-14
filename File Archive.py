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

"""
================== Inicio ==============================================
"""

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
================= Filtrado por metodo alfabetico =================
"""
if metodo_usuario == 1:  
    print("\n Aquí esta su lista por orden alfabético:" )
    
    archivo = lista_archivos_usuario.sort()
    for archivo in lista_archivos_usuario:
        print(archivo)
      
"""
================= Filtrado por tema ================= 
"""
if metodo_usuario == 2:
    print("\nAquí esta su lista por tema:" )
    
    lista_temas = [["Trabajo"],
                   ["Escuela"],
                   ["Personal"],
                   ["Sin Asignar"]]
    
    print("Te recordamos el nombre de tus archivos para que les asignes un tema: ", lista_archivos_usuario)
    
    archivo = lista_archivos_usuario
    for archivo in lista_archivos_usuario:
        tema_usuario = input("\nElije la categoría para tus archivos, las opciones son:\n'trabajo (tra)', 'escuela (es)' o 'personal (per)': ")
    
        if tema_usuario.lower() == "tra":
            lista_temas[0].append(archivo)
        elif tema_usuario.lower() == "es":
            lista_temas[1].append(archivo)
        elif tema_usuario.lower() == "per":
            lista_temas[2].append(archivo)
        else:
            lista_temas[3].append(archivo)
        
    for tema in lista_temas:
        print(tema[0], tema[1:])
"""
================= Filtrado por tiempo (números) =================
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

""" Códigos para darle color al texto """

ROJO = '\033[31m'
AZUL = '\033[34m'
VERDE = '\033[32m'
NEGRO = '\033[30m'

if metodo_usuario == 3:
    print("\nAquí esta su lista por tiempo:")
    
    if res1 > 2:
        print(archivo_1, f"{ROJO}antiguo{NEGRO}")
    if res2 > 2:
        print(archivo_2, f"{ROJO}antiguo{NEGRO}")
    if res3 == 2:
        print(archivo_3, f"{AZUL}hace un rato{NEGRO}")
    if res4 < 2:
        print(archivo_4, f"{VERDE}reciente{NEGRO}")
    if res5 < 2:
        print(archivo_5, f"{VERDE}reciente{NEGRO}")
        
"""
=================================== Final =================================================
"""


print("\nDesea intentar organizar sus archivos por otro método?")
print("Y/N?")
ans = input()

while ans not in ["Y","y","N","n"]:
    ans = input("\nLo siento, no entendimos tu respuesta, favor de intentar de nuevo con una respuesta de Y/N: ")

if ans in ["N","n"]:
    print("\nGracias por usar el programa, adiós :D")
    
elif ans in ["Y","y"]:
    metodo_usuario = 0
    while metodo_usuario == 0:
        metodo_usuario = int(input("\n¿Qué método desea utilizar esta vez? (1), (2), o (3)? "))
        if metodo_usuario in [1,2,3]:
            print("\nLo sentimos, esta acción estará disponible hasta el lanzamiento official del programa. Por el momento esperamos este DEMO hay sido de su agrado, que tenga un buen día :)")       
        elif metodo_usuario not in [1,2,3]:
            print("No se ha seleccionado una opción valida. Favor de intentar de nuevo.")
            metodo_usuario = metodo_usuario * 0
            
"""           
============== Investigación ===============
"""

#Colores
"""
Para poder dar fomato de color se debe introducir el inicio '\033, seguido de un [ y se debe introducir un número, el número que se introduzca representa un color. En la página viene una lista con el número para cada color,
por ejemplo el rojo tiene el número asignado de 31, azul 34, etc. Una vez hacemos esto debemos finalizar anotando una m' y al haber guardado los coloes en valores, puedo llamar a cada color sin tener que repetir
el código una y otra vez.
Referencia:
Dar color a las salidas en la consola. (2025, October 14). Blogspot.com. https://python-para-impacientes.blogspot.com/2016/09/dar-color-las-salidas-en-la-consola.html
"""

#'In' y 'Not in'
"""
In y Not in, se utilizan para verificar datos dentro de una lista, en el caso de mi proyecto, la lista son las opciones que quiero que se tomen en consideración para saber si el programa actua o no, marcando estos como una lista
de opciones al introducirlos dentro de corchetes [], una vez que esta generada la lista de opciones, uso la funcion de in o not in para que verifique si el dato que introduzca el usuario esta dentro del rango creado en la lista y
pueda realizar differentes acciones dependiendo de esto. Por ejemplo, cuando se le pide al usuario una respuesta de Y o N, hago uso de in ["N", "n"] para que si la respuesta del usurio esta en mínuscula o mayúscula, el programa actue,
pero si la respuesta del usuario no es una de Y o N, hice uso de not in[] para que devuelva un "error" y pida al usuario que introduzca un dato que si sea válido.
Referencia:
TechNesis. (2024, 16 agosto). Python - 27 Usos de los operadores IN y NOT IN [Vídeo]. YouTube. https://www.youtube.com/watch?v=EmYWXh8P5h8
"""
