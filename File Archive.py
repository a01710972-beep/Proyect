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
print("Aquí esta su lista por tema": )
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

val_1 = input("Por favor escriba el nombre de su primer archivo: ")
val_2 = input("Por favor escriba el nombre de su segundo archivo: ")
val_3 = input("Por favor escriba el nombre de su tercer archivo: ")
val_4 = input("Por favor escriba el nombre de su cuarto archivo: ")
val_5 = input("Por favor escriba el nombre de su quinto archivo: ")

val_1 = 1
val_2 = 2
val_3 = 3
val_4 = 4
val_5 = 5

print("Aquí esta su lista por tiempo")

def evalua_resta(para_resta, val_1):
    resultado1 = para_resta - val_1
    return resultado1

print(evalua_resta(5, 1))
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

if resultado_de_resta = < 3
print("antiguo")
if resultado_de_resta = == 3
print("hace un rato")
if resultado_de_resta = > 3
print("reciente")

