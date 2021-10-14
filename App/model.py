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


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.ADT import orderedmap as om
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
    catalogo["nationality"] = mp.newMap(1000,maptype="PROBING",loadfactor=0.80)
    catalogo["ID"] = mp.newMap(1000,maptype="CHAINING",loadfactor=4.0)
    catalogo["Begindates"] = om.newMap(omaptype="BST", comparefunction=compareDates)

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
    nacionalidad = artist['Nationality']
    iD = artist['ConstituentID']
    mapaNat = catalog['nationality']
    mapaId = catalog["ID"]
    artworks = catalog['artworks']
    AddNatMap(nacionalidad, iD, mapaNat, artworks)
    AddIdMap(iD,mapaId,artworks)
    updateDates(catalog["Begindates"], artist)
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
def addArtworks(catalog, artwork):
    lt.addLast(catalog['artworks'], artwork)
    mp.put(catalog["medium"], artwork["Medium"], artwork )
def newDataEntry(artist):
    entry = lt.newList("SINGLE_LINKED", compareDates)
    return entry
def updateDates( map, artist):
    ocurrentDate = int(artist["BeginDate"])
    entry = om.get(map, ocurrentDate)
    if entry is None:
        dateentry = newDataEntry(artist)
        om.put(map,ocurrentDate,dateentry)
    else:
        dateentry = me.getValue(entry)
    lt.addLast(dateentry,artist)
    return map
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

def getartistsByrange(catalog,InitialDate,FinalDate):
    lista = om.values(catalog["Begindates"],InitialDate,FinalDate)
    totalartist = 0
    for artista in lt.iterator(lista):
        totalartist += lt.size(artista)
    return totalartist, lista



# Funciones utilizadas para comparar elementos dentro de una lista
def compareDates(date1,date2):
    if date1 == date2:
        return 0
    elif (date1 > date2):
        return 1
    else: 
        return -1 

# Funciones de ordenamiento
