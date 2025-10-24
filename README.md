# File Archive
*Contexto*

La biblioteca digital del Tecnológico de Monterrey, es como lo dice el nombre, una biblioteca que se encuentra de forma digital en línea, permitiendo que el docente y alumnado del Tecnológico de Monterrey puedan acceder a contenido de múltiples bibliotecas, esto con el propósito de facilitar el acceso a distintas fuentes de información confiables para mejorar la calidad del aprendizaje y trabajo académico.

Para poder llevar a cabo sus funciones, la biblioteca digital cuenta con secciones para cada elemento de su inventario, ya sea que se clasifique por el género, clasificación alfabética, tipo de artículo, entre muchos otros. No solo esto, ya que la biblioteca cuenta con una barra de búsqueda por la cual se puede buscar el título o autor de algún recurso, incluso se cuenta con una herramienta de búsqueda avanzada, la cual nos permite realizar búsquedas más detalladas que filtren información no deseada para obtener resultados más precisos y que sean de utilidad para quien la use.

Este programa busca crear un sistema a través de python por el cual archivos que sean guardados por el usuario sean organizados y categorizados de forma que se puedan realizar búsquedas similares a las de la Biblioteca digital para facilitar el manejo de la información para el alumnado y docente de instituciones educativas, separando archivos personales de los archivos académicos y permitiendo filtrarlos por ejemplo en asignaturas, grupos y proyectos.

Instrucciones para correr el programa

Descargar el archivo y correr en terminal con:

o abrir en Thonny y dar botón de play.

Para esto se solicitará como parte del Demo que se introduzca una serie de datos relacionados a asignaturas o trabajos personales los cuales serán clasificados como archivos y el programa los organizará, permitiendo al usuario usar la herramienta de clasificación al introducir una palabra o más que permitan al sistema lanzar una respuesta.

Se espera que el programa sea de su agrado.






!!!! Correcciones !!!!

Entrega 1:
Componente: plantea una situación problema que le permite aplicar y demostrar sus conocimientos de programación (avance 1)

Error: hacía falta el código básico, esto se corrigió al añadir un primer avance para el código del programa

Cambio realizado: Empezar con el código
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

"""
================= Funciones de filtrado por metodo alfabetico =================
"""
"""
Dependiendo de la primera letra del archivo se desplazará la lista de estos
recibe: val_1 valor string, val_2 valor string, val_3 valor string.
val_4 valor string, val_5 valor string
devuelve: lista de elementos por orden alfabetico
"""

"""
================= Funciones de filtrado por tema =================
"""
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
def evalua_resta(para_resta, val_1)
"""
A los datos que el usuario introduzca se les asigna un valor numérico.
(uso de operadores)
recibe: val_1 valor númerico, val_2 valor númerico, val_3 valor númerico,
val_4 valor númerico, val_5 valor númerico
resta 5 a cada valor
devuelve: los valores ordenados de acuerdo a que tan grande es el número final
"""
return para_resta - val_1

def evalua_resta(para_resta, val_2)
return para_resta - val_2

def evalua_resta(para_resta, val_3)
return para_resta - val_3

def evalua_resta(para_resta, val_4)
return para_resta - val_4

def evalua_resta(para_resta, val_5)
return para_resta - val_5}

"""
Dependiendo del valor de la resta, se clasificará el archivo como "reciente", "hace un rato",
y "antiguo"
En este caso: x < 3 
devuelve: antiguo
x == 3
devuelve: hace un rato
x > 3
devuelve: reciente
"""

if resultado_de_resta = < 3
print("antiguo2")
if resultado_de_resta = == 3
print("hace un rato")
if resultado_de_resta = > 3
print("reciente")

"""
============ parte principal ===========
"""

Entrega 2:
Componente: usa operadores aritméticos de manera eficaz (avance 2)

Error: El código no funcionaba y se mencionaba que no había aritmética, aunque la inclusión de esta si estaba presente por medio de restas, asumo no se tomarón en cuenta debido a que el código no funcionaba

Cambios: Asegurarme que el código anterios SÍ funcionara y se hace la inclusión de colores

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

"""
================= Funciones de filtrado por metodo alfabetico =================
"""
"""
Dependiendo de la primera letra del archivo se desplazará la lista de estos
recibe: val_1 valor string, val_2 valor string, val_3 valor string.
val_4 valor string, val_5 valor string
devuelve: lista de elementos por orden alfabetico
"""
print("Aquí esta su lista por orden alfabético:" )
      

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
print("Aquí esta su lista por tema:" )
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

val_1_ = input("Por favor escriba el nombre de su primer archivo: ")
val_2_ = input("Por favor escriba el nombre de su segundo archivo: ")
val_3_ = input("Por favor escriba el nombre de su tercer archivo: ")
val_4_ = input("Por favor escriba el nombre de su cuarto archivo: ")
val_5_ = input("Por favor escriba el nombre de su quinto archivo: ")

val_1 = 1
val_2 = 2
val_3 = 3
val_4 = 4
val_5 = 5

print("Aquí esta su lista por tiempo:")

def evalua_resta(para_resta, val_1):
    resultado1 = para_resta - val_1
    return resultado1
"""
A los datos que el usuario introduzca se les asigna un valor numérico.
(uso de operadores)
recibe: val_1 valor númerico, val_2 valor númerico, val_3 valor númerico,
val_4 valor númerico, val_5 valor númerico
resta 5 a cada valor
devuelve: los valores ordenados de acuerdo a que tan grande es el número final
"""
def evalua_resta(para_resta, val_2):
    resultado2 = para_resta - val_2
    return resultado2

def evalua_resta(para_resta, val_3):
    resultado3 = para_resta - val_3
    return resultado3

def evalua_resta(para_resta, val_4):
    resultado4 = para_resta - val_4
    return resultado4    

def evalua_resta(para_resta, val_5):
    resultado5 = para_resta - val_5
    return resultado5

"""
Dependiendo del valor de la resta, se clasificará el archivo como "reciente", "hace un rato",
y "antiguo"
En este caso: x < 3 
devuelve: antiguo
x == 3
devuelve: hace un rato
x > 3
devuelve: reciente
"""
#NOTA!!!!
#En la siguiente parte solo investigue como ponerle color al texto, no afecta en nada al programa más allá de darle color al texto
ROJO = '\033[31m'
AZUL = '\033[34m'
VERDE = '\033[32m'
RESET = '\033[0m'
if val_1 < 3:
    print(val_1_, f"{ROJO}antiguo{RESET}")
if val_2 < 3:
    print(val_2_, f"{ROJO}antiguo{RESET}")
if val_3 == 3:
    print(val_3_, f"{AZUL}hace un rato{RESET}")
if val_4 > 3:
    print(val_4_, f"{VERDE}reciente{RESET}")
if val_5 > 3:
    print(val_5_, f"{VERDE}reciente{RESET}")




    

!!!!! Investigación !!!!!

Aquí incluyo cosas sobre las que investigue para realizar mi proyecto:

#Colores
Para poder dar fomato de color se debe introducir el inicio '\033, seguido de un [ y se debe introducir un número, el número que se introduzca representa un color. En la página viene una lista con el número para cada color,
por ejemplo el rojo tiene el número asignado de 31, azul 34, etc. Una vez hacemos esto debemos finalizar anotando una m' y al haber guardado los coloes en valores, puedo llamar a cada color sin tener que repetir
el código una y otra vez.
Referencia:
Dar color a las salidas en la consola. (2025, October 14). Blogspot.com. https://python-para-impacientes.blogspot.com/2016/09/dar-color-las-salidas-en-la-consola.html

#'In' y 'Not in'
In y Not in, se utilizan para verificar datos dentro de una lista, en el caso de mi proyecto, la lista son las opciones que quiero que se tomen en consideración para saber si el programa actua o no, marcando estos como una lista
de opciones al introducirlos dentro de corchetes [], una vez que esta generada la lista de opciones, uso la funcion de in o not in para que verifique si el dato que introduzca el usuario esta dentro del rango creado en la lista y
pueda realizar differentes acciones dependiendo de esto. Por ejemplo, cuando se le pide al usuario una respuesta de Y o N, hago uso de in ["N", "n"] para que si la respuesta del usurio esta en mínuscula o mayúscula, el programa actue,
pero si la respuesta del usuario no es una de Y o N, hice uso de not in[] para que devuelva un "error" y pida al usuario que introduzca un dato que si sea válido.
Referencia:
TechNesis. (2024, 16 agosto). Python - 27 Usos de los operadores IN y NOT IN [Vídeo]. YouTube. https://www.youtube.com/watch?v=EmYWXh8P5h8

#.sort()
Python cuenta con 2 funciones que nos permiten ordenar los valores dentro de una lista, sorted() y .sort(), la diferencia es que sorted() crea una lista nueva mientras que .sort() solo modifica una lista existente,
estas funciones ya estan configuradas para ordenar texto por metódo alfabético y números de forma descendiente a ascendiente, existen formas de invertir el orden, crear llaves y más con esta función para que relice tareas más complejas.
Referencias:
What is the difference between list.sort() and sorted() in Python? (2021, June 12). 30secondsofcode.org; Angelos Chalaris. https://www.30secondsofcode.org/python/s/sortedlist-vs-list-sort/
Navarro, A. (2023, June 21). Ordenamiento de listas en Python - Junco TIC. Junco TIC. https://juncotic.com/ordenamiento-de-listas-en-python/
