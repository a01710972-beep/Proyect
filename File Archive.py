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
