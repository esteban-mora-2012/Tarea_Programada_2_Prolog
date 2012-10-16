# -*- coding: utf-8 -*-
#Instituto Tecnológico de Costa Rica
#Escuela de Ingeniería en computación
#Administración de Tecnologias de Información
#Curso: TI-3404 Lenguajes de Programación
#Profesor: Andréi Fuentes Leyva
#Proyecto programado #2 Le Puolet
#Seccion de Interfaz grafica.
#Lenguajes utilizados
	#WSI-Prolog versión 6.0.2
	#Python versión 2.7.3
#Desarrolladores
	#Estefany Quesada Montero
	#Esteban Aguilar Varverde
	#Esteban Mora Soto
#-------------------------------------------------------------------------#
#Importado de bobliotecas
from Tkinter import * 		#Biblioteca de interfaz tkinter.
from string import *            #Biblioteca para el control de strings.
from sys import *               #Biblioteca de integración con el programa en python
import os                	#Biblioteca de integración con sistema operativo.
from sistema import *           #Carga las funciones del archivo "sistema.py"
import tkMessageBox             #Modulo de mensajes para información y errores.
resultado = []
#-------------------------------------------------------------------------#
#Funciones de mensages del programa.

def cambio_basededatos():
    mensaje = "La base de conocimientos ha sido actulizada."
    tkMessageBox.showinfo("NOTIFICACIÓN", mensaje)

def entrys_vacios():
    mensaje = "ERROR: Uno o más Entrys estan vacios por favor introdusca la información."
    tkMessageBox.showerror("Error", mensaje)

def exceso():
    mensaje = "ERROR: Esta colocando más de un estatuto se recomienda no usar ','."
    tkMessageBox.showerror("Error", mensaje)

def no_existe():
    mensaje = "ERROR: No existe la receta que busca."
    tkMessageBox.showerror("Error", mensaje)

def acerca_de():
    mensaje = "Este es un sistema de manejo de recetas para el restaurante Le Puolet."
    tkMessageBox.showinfo("Acerca del programa", mensaje)

def info_general():
    mensaje = "Programa hecho en Python version 2.7.3 y SWI-Prolog versión 6.0.2 ."
    tkMessageBox.showinfo("Información general", mensaje)

def developers():
    mensaje = "Estefany Quesada Montero,Esteban Aguilar Varverde,Esteban Mora Soto." 
    tkMessageBox.showinfo("Desarrolladores", mensaje)

def abrir_manual():
	return os.system("/usr/bin/xdg-open manual.pdf")

def abrir_docu():
	return os.system("/usr/bin/xdg-open documentacion.pdf")

def salir():
    sys.exit()
#-------------------------------------------------------------------------#
#Interfaz grafica de usuario.
#-------------------------------------------------------------------------#
#Ventana de borrado de recetas.
def ventana_resultado(resultado):
#-------------------------------------------------------------------------#
#Función de la ventana de resultado.
#Funcion verificar resultado: Verifica los resultados para imprimir
    def colocar_respuesta(texto_respuesta):
	texto_consulta.delete('1.0',END)
        texto_consulta.insert(END, texto_respuesta)

    def verificar_resultado(resultado):
        if (resultado == []):
            texto_respuesta = "No se encontraron animales esas caracteristicas"
        else:
            texto_respuesta = ""
            indice = 1
            for elem in resultado:
                texto_respuesta =(texto_respuesta + "-------------------------"+
                                  "\nResultado Número: " + str(indice) +
                                  "\nNombre: "+ str(elem["Nombre"]) +
                                  "\nAutor: "+ str(elem["Autor"]) +
                                  "\nEstilo: "+ str(elem["Estilo"]) +
                                  "\nIngrediente: "+ str(elem["Ingrediente"]) +
                                  "\nPreparación: "+ str(elem["Preparacion"]) +"\n")
                indice = indice +1
            texto_respuesta =(texto_respuesta + "-------------------------")
            #Coloca el texto en la ventana
            colocar_respuesta(texto_respuesta)
#-------------------------------------------------------------------------#
    #Interfaz grafica de la ventana de resultado.
    imagen5		    = PhotoImage(file = "resultado.gif")
    ventana_general5        = Label(bg="black",image=imagen5,width=750,height=600)
    texto_consulta          = Text(ventana_general5,height=15,width=90,background='white')
    scroll_respuesta        = Scrollbar(ventana_general5)
    texto_consulta.configure(yscrollcommand=scroll_respuesta.set)
    texto_consulta.pack(side=LEFT)
    scroll_respuesta.pack(side=RIGHT,fill=Y)
    ventana_general5.place(x=0,y=0)
    verificar_resultado(resultado)
    ventana_general5.mainloop()
#-------------------------------------------------------------------------#
#Ventana principal.
def ventana_principal():
    imagen1             = PhotoImage(file = "principal.gif")
    ventana_general1    = Label(bg="black",image=imagen1,width=750,height=600)
    ventana_general1.place(x=0,y=0)
    ventana_general1.mainloop()
#-------------------------------------------------------------------------#
#Ventana de inserción y actualización de recetas.
def ventaba_creacion():
#-------------------------------------------------------------------------#
#Función de la ventana de inserción y actualización.
    #Limpieza de los entrys
    def limpiar_1():
        entrada0.delete(0,END)
        entrada1.delete(0,END)
        entrada2.delete(0,END)
        entrada3.delete(0,END)
        entrada4.delete('1.0',END)
    #Toma la información de la ventana de creación de recetas para crear
    def tomar_info_1():
        receta_nombre           =   lower(entrada0.get())
        receta_autor            =   lower(entrada1.get())
        receta_estilo           =   lower(entrada2.get())
        receta_ingredientes     =   lower(entrada3.get())
        receta_preparacion      =   lower(entrada4.get('1.0',END))
        listaing                =   receta_ingredientes.split(',')
        listapre                =   receta_preparacion.split(',')
        limpiar_1()
        if verificar_1(receta_nombre,receta_autor,receta_estilo,receta_ingredientes,receta_preparacion) == False:
            entrys_vacios()
        if (len(listaing) > 1) or (len(listapre) > 1):
            exceso()
        else:
            agregar_receta(receta_nombre,receta_autor,receta_estilo,receta_ingredientes,receta_preparacion)
            cambio_basededatos()

    #Toma la información de la ventana de creación de recetas para actualizar
    def tomar_info_2():
        receta_nombre           =   lower(entrada0.get())
        receta_autor            =   lower(entrada1.get())
        receta_estilo           =   lower(entrada2.get())
        receta_ingredientes     =   lower(entrada3.get())
        receta_preparacion      =   lower(entrada4.get('1.0',END))
        listaing                =   receta_ingredientes.split(',')
        listapre                =   receta_preparacion.split(',')
        limpiar_1()
        if verificar_1(receta_nombre,receta_autor,receta_estilo,receta_ingredientes,receta_preparacion) == False:
            entrys_vacios()
        if (len(listaing) > 1) or (len(listapre) > 1):
            exceso()
        else:
	    if borrar(receta_nombre) == True:
		agregar_receta(receta_nombre,receta_autor,receta_estilo,receta_ingredientes,receta_preparacion)
            	cambio_basededatos()
	    else:
		no_existe()
#-------------------------------------------------------------------------#
    #Interfaz grafica de la ventana de inserción y actualización.
    imagen2             = PhotoImage(file = "insertar.gif")
    ventana_general2    = Label(bg="black",image=imagen2,width=750,height=600)
    entrada0            = Entry(ventana_general2,bg="white",fg="black",font=("URW Chancery L",15),width=20)
    entrada1            = Entry(ventana_general2,bg="white",fg="black",font=("URW Chancery L",15),width=20)
    entrada2            = Entry(ventana_general2,bg="white",fg="black",font=("URW Chancery L",15),width=20)
    entrada3            = Entry(ventana_general2,bg="white",fg="black",font=("URW Chancery L",15),width=20)
    entrada4            = Text (ventana_general2,bg="white",fg="black",font=("URW Chancery L",15),width=50,height=6)
    boton1              = Button(ventana_general2,bg="white",fg="black",text="Introducir receta",font=("URW Chancery L",15),command=tomar_info_1)
    boton2              = Button(ventana_general2,bg="white",fg="black",text="Actualizar receta",font=("URW Chancery L",15),command=tomar_info_2)
    entrada0.place(x=290,y=100)
    entrada1.place(x=290,y=180)
    entrada2.place(x=290,y=250)
    entrada3.place(x=290,y=320)
    entrada4.place(x=280,y=420)
    boton1.place(x=530,y=175)
    boton2.place(x=530,y=245)
    ventana_general2.place(x=0,y=0)
    ventana_general2.mainloop()
#-------------------------------------------------------------------------#
#Ventana de busqueda de recetas.
def ventana_consulta():
#-------------------------------------------------------------------------#
#Función de la ventana de busqueda de recetas.
    #Limpieza de los entrys
    def limpiar_2():
        entrada5.delete(0,END)
        entrada6.delete(0,END)
        entrada7.delete(0,END)
        entrada8.delete(0,END)
    #Toma la información de la ventana de busqueda de recetas
    def tomar_info_3():
        nombre           =   lower(entrada5.get())
        autor            =   lower(entrada6.get())
        estilo           =   lower(entrada7.get())
        ingrediente1     =   lower(entrada8.get())
        ingrediente2     =   ingrediente1.split(',')
        if len(ingrediente2) > 1:
            exceso()
        else:
            limpiar_2()
            resultado = consulta(nombre,autor,estilo,ingrediente1)
            ventana_resultado(resultado)
#-------------------------------------------------------------------------#
    #Interfaz grafica de la ventana de busqueda de recetas.
    imagen3             = PhotoImage(file = "consulta.gif")
    ventana_general3    = Label(bg="black",image=imagen3,width=750,height=600)
    entrada5            = Entry(ventana_general3,bg="white",fg="black",font=("URW Chancery L",15),width=20)
    entrada6            = Entry(ventana_general3,bg="white",fg="black",font=("URW Chancery L",15),width=20)
    entrada7            = Entry(ventana_general3,bg="white",fg="black",font=("URW Chancery L",15),width=20)
    entrada8            = Entry(ventana_general3,bg="white",fg="black",font=("URW Chancery L",15),width=20)
    boton3              = Button(ventana_general3,bg="white",fg="black",text="Consultar Receta",font=("URW Chancery L",15),command=tomar_info_3)
    boton4              = Button(ventana_general3,bg="white",fg="black",text="Consulta  Geneal",font=("URW Chancery L",15),command=tomar_info_3)
    boton3.place(x=300,y=500)
    boton4.place(x=550,y=500)
    entrada5.place(x=280,y=120)
    entrada6.place(x=280,y=230)
    entrada7.place(x=280,y=320)
    entrada8.place(x=280,y=390)
    ventana_general3.place(x=0,y=0)
    ventana_general3.mainloop()
#-------------------------------------------------------------------------#
#Ventana de borrado de recetas.
def ventana_borrado():
#-------------------------------------------------------------------------#
#Función de la ventana de borrado de recetas.
    #Limpieza del entry
    def limpiar_3():
        entrada9.delete(0,END)
    #Toma la información de la ventana de borrado de recetas
    def tomar_info_4():
        receta_nombre           =   lower(entrada9.get())
        if receta_nombre == "":
            entrys_vacios()
        else:
            limpiar_3()
            if borrar(receta_nombre) == True:
            	cambio_basededatos()
	    else:
		no_existe()
		
            
#-------------------------------------------------------------------------#
    #Interfaz grafica de la ventana de borrado de recetas.
    imagen4             = PhotoImage(file = "eliminar.gif")
    ventana_general4    = Label(bg="black",image=imagen4,width=750,height=600)
    entrada9            = Entry(ventana_general4,bg="white",fg="black",font=("URW Chancery L",15),width=30)
    boton5              = Button(ventana_general4,bg="white",fg="black",text="Borrar receta",font=("URW Chancery L",15),command=tomar_info_4)
    boton5.place(x=300,y=160)
    entrada9.place(x=250,y=100)
    ventana_general4.place(x=0,y=0)
    ventana_general4.mainloop()
#-------------------------------------------------------------------------#
#Contenedor principal y menu principal.
root=Tk()
menubar = Menu(root)
root.config(menu = menubar)
Ventana = Menu(menubar, tearoff = 0)
Ayuda   = Menu(menubar, tearoff = 0)
#Opciones de seleccion principal del menu
menubar.add_cascade(label = "Ventanas", menu = Ventana)
menubar.add_cascade(label = "Ayuda", menu = Ayuda)
menubar.add_command(label = "Salir",command=salir)
#Opciones del modulo de ventana.
Ventana.add_command(label = "Ventana Principal",command=ventana_principal)
Ventana.add_command(label = "Sistema de Consulta",command=ventana_consulta)
Ventana.add_command(label = "Sistema Ins-Act",command=ventaba_creacion)
Ventana.add_command(label = "Sistema de borrado",command=ventana_borrado)
#Opciones del modulo de Ayuda
Ayuda.add_command(label = "Acerda de",command=acerca_de)
Ayuda.add_command(label = "Información general",command=info_general)
Ayuda.add_command(label = "Desarrolladores",command=developers)
Ayuda.add_command(label = "Documentoción externa",command=abrir_docu)
Ayuda.add_command(label = "Manual de usuario",command=abrir_manual)
root.title("Restaurante Le Puolet")
#Carga de la ventana principal y composisción fisica del programa
root.minsize(750,600)
root.maxsize(750,600)
ventana_principal()
menubar.mainloop()
root.mainloop()
#-------------------------------------------------------------------------#
