﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import list as lt
assert cf
import time
def printSortResults1(ord_artists):
    size = lt.size(ord_artists)
    rango = 4
    print("Los primeros y ultimos 3 son: ")
    #Primeros 3 
    i = 1
    while i < rango:
        primeros = lt.getElement(ord_artists,i)
        print("Nombre: " + primeros["DisplayName"] + "; Año de Nacimiento: " + primeros["BeginDate"] + "; Año de Fallecimiento: " + primeros["EndDate"] + "; Nationality: " + primeros["Nationality"] + "; Gender: " + primeros["Gender"])
        i+=1
    #Uiltimos 3
    j = 2
    while j >= 0:
        ultimos = lt.getElement(ord_artists,size-j)
        print("Nombre: " + ultimos["DisplayName"] + "; Año de Nacimiento: " + ultimos["BeginDate"] + "; Año de Fallecimiento: " + ultimos["EndDate"] + "; Nationality: " + ultimos["Nationality"] + "; Gender: " + ultimos["Gender"])
        j -=1
def printSortResults2(ord_artworks,lista_artistas):
    size = lt.size(ord_artworks)
    rango = 4
    print("Los primeros y ultimos 3 son: ")
    #Primeros 3 
    i = 1
    while i < rango:
        primeros = lt.getElement(ord_artworks,i)
        C_id = primeros["ConstituentID"]
        nombre = controller.searchConstituentID(lista_artistas,C_id)
        print("Titulo: " + primeros["Title"] + "; Nombre: " + str(nombre) + "; Fecha: " + primeros["Date"] + "; Medio: " + primeros["Medium"] + "; Dimensiones: " + primeros["Dimensions"])
        i+=1
    #Uiltimos 3
    j = 2
    while j >= 0:
        ultimos = lt.getElement(ord_artworks,size-j)
        C_idu = ultimos["ConstituentID"]
        nombreU = controller.searchConstituentID(lista_artistas,C_idu)
        print("Titulo: " + ultimos["Title"] + "; Nombre: " + nombreU + "; Fecha: " + ultimos["Date"] + "; Medio: " + ultimos["Medium"] + "; Dimensiones: " + ultimos["Dimensions"])
        j -=1
def PrintResults4(lista,mapa,lista_artistas):
    print( "El top 10 paises en MoMA son :")
    i = 1
    range = 11
    while i < range:
        elemento = lt.getElement(lista,i)
        nacionalidad = elemento["Nacionalidad"]
        if nacionalidad == "" or nacionalidad == None:
            nacionalidad = "Unknown"
        print("Nacionalidad: " + str(nacionalidad) + " Artworks: " + str(elemento["Artworks"]))
        i+=1
    Mejor_pais = lt.getElement(lista,1)
    pais = Mejor_pais["Nacionalidad"]
    pareja = mp.get(mapa,pais)
    lista2= me.getValue(pareja)
    print("La mejor naciolanidad en el museo es: " + str(pais) + " con " + str(lt.size(lista2)) + " piezas unicas" )
    print("Las primeras y ultimas 3 obras in la lista de obas amercianas son: ")
    #Primeros 3 
    d = 1
    while d < 4:
        primeros = lt.getElement(lista2,d)
        C_id = primeros["ConstituentID"]
        nombre = controller.searchConstituentID(lista_artistas,C_id)
        print("Titulo: " + primeros["Title"] + "; Nombre: " + str(nombre) + "; Fecha: " + primeros["Date"] + "; Medio: " + primeros["Medium"] + "; Dimensiones: " + primeros["Dimensions"])
        d+=1
    #Uiltimos 3
    j = 2
    while j >= 0:
        ultimos = lt.getElement(lista2,lt.size(lista2)-j)
        C_idu = ultimos["ConstituentID"]
        nombreU = controller.searchConstituentID(lista_artistas,C_idu)
        print("Titulo: " + ultimos["Title"] + "; Nombre: " + nombreU + "; Fecha: " + ultimos["Date"] + "; Medio: " + ultimos["Medium"] + "; Dimensiones: " + ultimos["Dimensions"])
        j -=1

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Requerimiento 1")
    print("3- Requerimiento 2")
    print("5- Requerimiento 4")
    print("6- Requerimiento 5")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Inicializando catálogo ....")
        cont = controller.initCatalog()
        print("Cargando información de los archivos ....")
        controller.loadData(cont,'Artists-utf8-small.csv','Artworks-utf8-small.csv')
        print("Se cargo exitosamente la información")
        print("Artistas cargados: " + str(controller.artistsize(cont)))
        print("Artworks cargados: " + str(controller.artworkssize(cont)))
    elif int(inputs[0]) == 2:
        fechaInicial = int(input("Digite el año inicial (YYYY): "))
        fechaFinal = int(input("Digite el año final (YYYY): "))
        total = controller.getartistsByrange (cont,fechaInicial,fechaFinal)
        print("Hay " + str(lt.size(total)) + " artistas entre " + str(fechaInicial) + " y " + str(fechaFinal))
        ordenada = controller.sortArtistByDate(total)
        printSortResults1(ordenada)
    elif int(inputs[0]) == 3:
        date1 = input("Indique el año inicial de la búsqueda en formato AAAA-MM-DD: ")
        date2 = input("Indique el año final de la búsqueda en formato AAAA-MM-DD: ")
        total = controller.Artorksinrange(cont,date1,date2)
        print("Hay " + str(lt.size(total[0])) + " adquisiciones hechas entre " + str(date1) + " y " + str(date2))
        print("El MoMA adquirió " + str(total[1]) + " piezas unicas entre " + str(date1) + " y " + str(date2) )
        ordenada = controller.sortDate(total[0])
        printSortResults2(ordenada,cont["artist"])
    elif int(inputs[0]) == 4:
        pass
    elif int(inputs[0]) == 5:
        Catalogo_Art_Nacionalidad = controller.NumArtByNat(cont)
        ordenada = controller.sortArtVsNatBynum(Catalogo_Art_Nacionalidad)
        mapa = cont["nationality"]
        PrintResults4(ordenada,mapa,cont["artist"])
    elif int(inputs[0])== 6:
        pass

    else:
        sys.exit(0)
sys.exit(0)
