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

print("Hola, buen día, hoy filtraremos tus archivos por ti :)4 \n")

archivo_1 = str(input("Por favor escriba el nombre de su primer archivo: "))
archivo_2 = str(input("Por favor escriba el nombre de su segundo archivo: "))
archivo_3 = str(input("Por favor escriba el nombre de su tercer archivo: "))
archivo_4 = str(input("Por favor escriba el nombre de su cuarto archivo: "))
archivo_5 = str(input("Por favor escriba el nombre de su quinto archivo: "))

"""Se le pide al usuario que nombre 5 archivos y estos se guiardan dentro de una lista, una vez guardados, se le pedirá al usuario que eliga un
método para organizar sus archivos"""

lista_archivos_usuario = [archivo_1, archivo_2, archivo_3, archivo_4, archivo_5]

print("\n Elige el NÚMERO de método por el cual quieres que organizemos tus archivos, las opciones son las siguientes:")
lista_metodos = ("(1) Orden Alfabético", "(2) Orden por tema", "(3) Orden por tiempo")
for i in lista_metodos:
    print(i)
    
"""En caso de que el usuario no de un número de método valido, se le pedira una y otra vez que vuelva a esribir su respuesta hasta
que escriba un número de opción valida para poder continuar"""

metodo_usuario = int(input())
while metodo_usuario not in [1,2,3]:
    print("No es una opción valida, por favor intente de nuevo")
    metodo_usuario = int(input())

"""
================= Filtrado por metodo alfabetico =================
"""
if metodo_usuario == 1:  
    print("\n Aquí esta su lista por orden alfabético:" )

    """Usando .sort(), podemos hacer que la lista que creamos previamente con los nombres que dio el usuario se organizen de forma automática"""
    archivo = lista_archivos_usuario.sort()
    for archivo in lista_archivos_usuario:
        print(archivo)
      
"""
================= Filtrado por tema ================= 
"""
if metodo_usuario == 2:
    print("\nAquí esta su lista por tema:" )
    
    """Haciendo uso de las listas anidadas, creamos una lista que contenga otras listas, en este caso los temas, con el fin de asignar cada archivo a un tema"""
    lista_temas = [["Trabajo"],
                   ["Escuela"],
                   ["Personal"],
                   ["Sin Asignar"]]
    
    print("Te recordamos el nombre de tus archivos para que les asignes un tema: ", lista_archivos_usuario)
    
    """Aquí, al usuario se le pedirá que le asigne una categoría de las disponibles a cada uno de sus archivos e incluso se le muestran nuevamente para facilitar la clasificación"""
    archivo = lista_archivos_usuario
    for archivo in lista_archivos_usuario:
        tema_usuario = input("\nElije la categoría para tus archivos, las opciones son:\n'trabajo (tra)', 'escuela (es)' o 'personal (per)': ")
        
    """Ya que el usuario asignó las categorías a cada archivo, los archivos son añadidos a las listas para poderse imprimir con su tema correspondiente"""
        if tema_usuario.lower() == "tra":
            lista_temas[0].append(archivo)
        elif tema_usuario.lower() == "es":
            lista_temas[1].append(archivo)
        elif tema_usuario.lower() == "per":
            lista_temas[2].append(archivo)
        else:
            lista_temas[3].append(archivo)
        
    for tema in lista_temas:
        print(tema[0], tema[1])
"""
================= Filtrado por tiempo (números) =================
"""

"""Se realizan operaciones para luego poder organizar nuestros archivos"""
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

""" Códigos para darle color al texto, lo guardamos porque no queremo escribir el codigo 28428 veces y es mejor solo llamarlo por ROJO, AZUL, etc. """

ROJO = '\033[31m'
AZUL = '\033[34m'
VERDE = '\033[32m'
NEGRO = '\033[30m'

if metodo_usuario == 3:
    print("\nAquí esta su lista por tiempo:")
    """Usando los resultdos de las operaciones anteriores, organizamos cada archivo y este devuelve que tan antiguo o reciente es"""
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

"""Aquí se da el cierre del programa y damos la ilusión de la libre elcción ya que en esta vida no todo es como queremos, también se obliga al usuario a que de una respuesta entre las que el
programa acepta y en caso de no hacerlo se repetirá hasta que se de una respuesta valida"""
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
            print("\nPues, lol que mal, esta acción estará disponible hasta el lanzamiento official del programa. Por el momento esperamos este DEMO hay sido de su agrado, que tenga un buen día :)")       
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

#.sort()
"""
Python cuenta con 2 funciones que nos permiten ordenar los valores dentro de una lista, sorted() y .sort(), la diferencia es que sorted() crea una lista nueva mientras que .sort() solo modifica una lista existente,
estas funciones ya estan configuradas para ordenar texto por metódo alfabético y números de forma descendiente a ascendiente, existen formas de invertir el orden, crear llaves y más con esta función para que relice tareas más complejas.
Referencias:
What is the difference between list.sort() and sorted() in Python? (2021, June 12). 30secondsofcode.org; Angelos Chalaris. https://www.30secondsofcode.org/python/s/sortedlist-vs-list-sort/
Navarro, A. (2023, June 21). Ordenamiento de listas en Python - Junco TIC. Junco TIC. https://juncotic.com/ordenamiento-de-listas-en-python/
"""
