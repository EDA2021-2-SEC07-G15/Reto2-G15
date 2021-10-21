"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


from DISClib.DataStructures.arraylist import newList
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.ADT import orderedmap as om
from DISClib.Algorithms.Sorting import mergesort as Mg
import time
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    catalogo = {'artist': None,
               'artworks': None,
               'Artw_Nacionalidades': None,
               "medium": None,
               "nationality":None,
               "ID":None}

    catalogo['artist'] = lt.newList(datastructure= "ARRAY_LIST")
    catalogo['artworks'] = lt.newList(datastructure= "ARRAY_LIST")
    catalogo["medium"] = mp.newMap(1000,maptype="PROBING",loadfactor=0.80)
    catalogo["nationality"] = mp.newMap(1000,maptype="CHAINING",loadfactor=0.80)
    catalogo["ID"] = mp.newMap(1000,maptype="CHAINING",loadfactor=0.36)
    catalogo["Begindates"] = mp.newMap(1000,maptype="PROBING",loadfactor=0.80)
    catalogo["DateAcquired"] = mp.newMap(1000,maptype="PROBING",loadfactor=0.80)

    return catalogo

# Funciones para agregar informacion al catalogo
def buscarArtworks(lista_artworks,id,lista):
    tamañoArw = lt.size(lista_artworks)
    i = 0
    while i < tamañoArw:
        elemento = lt.getElement(lista_artworks,i)
        artwork = elemento["ConstituentID"]
        C_id = artwork.strip("[]")
        if id in C_id:
            lt.addLast(lista,elemento)
        i+=1   
def addArtists(catalog, artist):
    lt.addLast(catalog['artist'], artist)
    # Datos  
    nacionalidad = artist['Nationality']
    iD = artist['ConstituentID']
    begindate = artist["BeginDate"]
    #Mapas
    mapaBDates = catalog["Begindates"]
    mapaNat = catalog['nationality']
    mapaId = catalog["ID"]
    artworks = catalog['artworks']
    #Agregar Mapas
    addBeginDates(begindate,mapaBDates,artist)
    AddNatMap(nacionalidad, iD, mapaNat, artworks)
    AddIdMap(iD,mapaId,artworks)
  
def AddIdMap(identificador,mapa,lista):
    existId = mp.contains(mapa,identificador)
    if existId == True:
        Pareja = mp.get(mapa,identificador)
        valor = me.getValue(Pareja)
        buscarArtworks(lista,identificador,valor)
    else:
        lista_art = lt.newList(datastructure="ARRAY_LIST")
        buscarArtworks(lista,identificador,lista_art)
        mp.put(mapa,identificador,lista_art)
    

def AddNatMap(nacionalidad, iD, mapa, artworks):
    existNat = mp.contains(mapa,nacionalidad)
    if existNat == True:
        Pareja = mp.get(mapa,nacionalidad)
        valor = me.getValue(Pareja)
        buscarArtworks(artworks,iD,valor)
    else:
        lista_art = lt.newList(datastructure="ARRAY_LIST")
        buscarArtworks(artworks,iD,lista_art)
        mp.put(mapa,nacionalidad,lista_art)
"Mapa begindates"
def addBeginDates(begindate,mapa,artist):
    exitDate= mp.contains(mapa,begindate)
    if exitDate == True:
        pareja = mp.get(mapa,begindate)
        valor = me.getValue(pareja)
        lt.addLast(valor,artist)
    else: 
        lista_art= lt.newList(datastructure="ARRAY_LIST")
        lt.addLast(lista_art,artist)
        mp.put(mapa,begindate,lista_art)
def addArtworks(catalog, artwork):
    lt.addLast(catalog['artworks'], artwork)
    #Datos 
    Dateacquired = artwork["DateAcquired"]
    #Mapas
    DateAcMap = catalog["DateAcquired"]
    #Agregar a mapas
    addDateAc(Dateacquired,DateAcMap,artwork)
    mp.put(catalog["medium"], artwork["Medium"], artwork )
"Mapa Date Acquired"
def addDateAc(fecha,mapa,artwork):
    existDate = mp.contains(mapa,fecha)
    if existDate:
        pareja = mp.get(mapa,fecha)
        valor = me.getValue(pareja)
        lt.addLast(valor,artwork)
    else:
        lista = lt.newList(datastructure="ARRAY_LIST")
        lt.addLast(lista,artwork)
        mp.put(mapa,fecha,lista)


# Funciones para creacion de datos

# Funciones de consulta
def ArtistSize(catalog):
    return lt.size(catalog["artist"])

def ArtworksSize(catalog):
    return lt.size(catalog["artworks"])
def getNumberNat(cont,nacionalidad):
    mapa = cont["nationality"]
    pareja = mp.get(mapa,nacionalidad)
    total = me.getValue(pareja)
    return lt.size(total)
"-------------------------Requerimiento 1---------------"
def getartistsByrange(catalog,InitialDate,FinalDate):
    lista = lt.newList(datastructure="ARRAY_LIST")
    totalartist = 0 
    mapa = catalog["Begindates"]
    dates = mp.keySet(mapa)
    i = 1 
    while i < lt.size(dates):
        llave = lt.getElement(dates,i)
        if int(llave) >= InitialDate and int(llave) <= FinalDate:
            entry = mp.get(mapa,llave)
            valor = me.getValue(entry)
            totalartist += ArtistinRange(lista,totalartist,valor)
        i +=1 
    return lista
    
def ArtistinRange(lista,conteo,valores):
    i = 0 
    while i < lt.size(valores):
        conteo = 0
        artista = lt.getElement(valores,i)
        lt.addLast(lista,artista)
        conteo += 1
        i += 1
    return conteo
"------------------Requerimiento 2 ------------------"
def ArtinRange(lista,valores):
    Numpurchase = 0
    i = 0 
    while i < lt.size(valores):
        artista = lt.getElement(valores,i)
        purchase = artista["CreditLine"]
        if "urchase" in purchase:
            Numpurchase +=1
        lt.addLast(lista,artista)
        i += 1
    return Numpurchase
def Artorksinrange(catalog,date1,date2):
    fecha1 = time.strptime(date1, "%Y-%m-%d")
    fecha2 = time.strptime(date2, "%Y-%m-%d")
    lista = lt.newList(datastructure="ARRAY_LIST")
    Numpurchase = 0
    mapa = catalog["DateAcquired"]
    dates = mp.keySet(mapa)
    i = 1
    while i < lt.size(dates):
        llave = lt.getElement(dates,i)
        if llave != "":
            fecha_a_comparar = time.strptime(llave, "%Y-%m-%d")
            comparacion = fecha_a_comparar >= fecha1 and fecha_a_comparar <= fecha2
            if comparacion:
                entry = mp.get(mapa,llave)
                valor = me.getValue(entry)
                Numpurchase += ArtinRange(lista,valor)
                
        i +=1
    return lista,Numpurchase
def searchConstituentID (Lista_artista,idAw):
    size = lt.size(Lista_artista)
    i = 1 
    id_a_comparar = idAw.strip("[]")
    while i < size:
        elemento = lt.getElement(Lista_artista,i)
        C_id = elemento["ConstituentID"]
        if C_id in id_a_comparar:
            return elemento["DisplayName"]

        i+= 1
"-----------Requerimiento 4 -------------"
def NumArtByNat(catalog):
    lista = lt.newList(datastructure="ARRAY_LIST")
    mapa = catalog["nationality"]
    Nacionalidades = mp.keySet(mapa)
    i = 1
    while i < lt.size(Nacionalidades):
        nacionalidad = lt.getElement(Nacionalidades,i)
        pareja = mp.get(mapa,nacionalidad)
        valor = me.getValue(pareja)
        CantidadByNat = lt.size(valor)
        catalogo = {"Nacionalidad": nacionalidad, "Artworks": CantidadByNat}
        lt.addLast(lista,catalogo)
        i += 1
    return lista


# Funciones utilizadas para comparar elementos dentro de una lista
def cmpArtistByBirthDate(artist1, artist2):
    date1 = artist1["BeginDate"] 
    date2 = artist2["BeginDate"] 
    if date1 < date2:
        return True
    else:
        return False
def cmpArtworkByDateAcquired(artwork1, artwork2):
    date1= artwork1["DateAcquired"]
    date2= artwork2["DateAcquired"]
    if date1 != "" and date2 != "":
        fecha1 = time.strptime(date1, "%Y-%m-%d")
        fecha2 = time.strptime(date2, "%Y-%m-%d")
        comparacion = fecha1 < fecha2
        return comparacion
    else:
        return True
def cmpArtVsNatByNumber(num1,num2):
    Numero1=num1["Artworks"]
    Numero2=num2["Artworks"]
    if Numero1 > Numero2:
        return True
    else:
        return False

# Funciones de ordenamiento
def sortArtistbyDate (lista):
    sub_list2 = lt.subList(lista,1, lt.size(lista))
    sub_list2 = sub_list2.copy()
    sorted_list = Mg.sort(sub_list2, cmpArtistByBirthDate)
    return sorted_list
def sortDate(total):
    sub_list1 = lt.subList(total, 1, lt.size(total))
    sub_list1 = sub_list1.copy()
    sorted_list = Mg.sort(sub_list1, cmpArtworkByDateAcquired)
    return sorted_list
def sortArtVsNatBynum (catalog):
    sub_list2 = lt.subList(catalog,1, lt.size(catalog))
    sub_list2 = sub_list2.copy()
    sorted_list = Mg.sort(sub_list2, cmpArtVsNatByNumber)
    return sorted_list

