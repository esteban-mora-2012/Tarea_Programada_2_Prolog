# -*- coding: utf-8 -*-
#Instituto Tecnológico de Costa Rica
#Escuela de Ingeniería en computación
#Administración de Tecnologias de Información
#Curso: TI-3404 Lenguajes de Programación
#Profesor: Andréi Fuentes Leyva
#Proyecto programado #2 Le Puolet
#Seccion de sistema principal.
#Lenguajes utilizados
	#WSI-Prolog versión 6.0.2
	#Python versión 2.7.3
#Desarrolladores
	#Estefany Quesada Montero
	#Esteban Aguilar Varverde
	#Esteban Mora Soto

#-------------------------------------------------------------------------#
#Importado de bobliotecas.
from string import *            #Biblioteca para el control de strings.
from pyswip import *		#Biblioteca para el control de prolog.
prolog = Prolog()               #Variable global que inicializa prolog.
#-------------------------------------------------------------------------#
#Variables globales del sistema.
lista_recetas = []      #Esta lista contendra las recetas.
nombre_recetas= [] #Esta lista contendra los ingredientes.
#-------------------------------------------------------------------------#
#Funciones del sistema.
#-------------------------------------------------------------------------
#Funciones de verificacion.

#Verificar 1.
#Verifica las entradas para el sistema de insercion y actualizacion.
def verificar_1(nombre,autor,estilo,ingrediente,preparacion):
    if(nombre == "" or autor == "" or estilo == "" or ingrediente == "" or preparacion == ""):
        return False
    else:
        return True

#Verificar 2.
#Verifica la entrada para el sistema de borrado.
    def verificar_2(nombre):
        if nombre == "" :
            return False
        else:
            return True
#-------------------------------------------------------------------------#
#Funcion escribir: Escribe en el archivo de prolog la receta.
def escribir_1():
    archivo=open("recetas.pl","w")
    for ele in lista_recetas:
        ele = ele+"\n"
        archivo.write(ele)
    archivo.close()
    prolog.consult("recetas.pl")
    return True
#-------------------------------------------------------------------------#
#Funcion leer: Lee el archivo de prolog de recetas.
def leer_1():
    archivo=open("recetas.pl","r")
    lista = []
    for ele in archivo.readlines():
        lista.append(str(ele[:-1]))
    archivo.close()
    prolog.consult("recetas.pl")
    return lista
#-------------------------------------------------------------------------#
#Funcion escribir: Escribe en el archivo de texto la receta.
def escribir_2():
    archivo=open("recetas.txt","w")
    for ele in nombre_recetas:
        ele = ele+"\n"
        archivo.write(ele)
    archivo.close()
    return True
#-------------------------------------------------------------------------#
#Funcion leer: Lee el archivo de texto de recetas.
def leer_2():
    archivo=open("recetas.txt","r")
    lista = []
    for ele in archivo.readlines():
        lista.append(ele[:-1])
    archivo.close()
    return lista
#-------------------------------------------------------------------------
#Funcion agregar_receta:Agrega una receta a la base de conocimiento.
def agregar_receta(nombre,autor,estilo,ingrediente,preparacion):
    receta = "receta("+nombre+","+autor+","+estilo+","+ingrediente+","+preparacion+")."
    lista_recetas.append(receta)
    nombre_recetas.append(nombre)
    escribir_1()
    escribir_2()
    return True
#-------------------------------------------------------------------------
#Funcion organizar_consulta:Organiza la informacion para generar una consulta a prolog si algun dato esta vacio lo transforma en variable
def consulta(nombre,autor,estilo,ingrediente):
    if(nombre == ""):
        nombre = "Nombre"
    if(autor == ""):
        autor = "Autor"
    if(estilo == ""):
        estilo = "Estilo"
    if(ingrediente == ""):
        ingrediente = "Ingrediente"
    preparacion = "Preparacion"
    #Construccion de la consulta
    consulta = "receta("+nombre+","+autor+","+estilo+","+ingrediente+","+preparacion+")"
    #Realiza la consulta a prolog y lo comoca en una lista
    solucion = list(prolog.query(consulta))
    #Revisa la información obtenida e introduce la informacion no variable al la solicion.
    for element in solucion:
        if(nombre != "Nombre"):
            element["Nombre"]=nombre
        if(autor != "Autor"):
            element["Autor"]=autor
        if(estilo != "Estilo"):
            element["Estilo"]=estilo
        if(ingrediente != "Ingrediente"):
            element["Ingrediente"]=ingrediente
    return solucion
#-------------------------------------------------------------------------
#Funcion borrado:Borra un predicado del sistema
def borrar(nombre_receta):
    if nombre_receta not in nombre_recetas:
        return False
    else:
        indice = nombre_recetas.index(nombre_receta)
        receta = lista_recetas[indice]
        nombre_recetas.remove(nombre_receta)
        lista_recetas.remove(receta)
        escribir_1()
        escribir_2()
        return True
#-------------------------------------------------------------------------
nombre_recetas = leer_2()
lista_recetas  = leer_1()
