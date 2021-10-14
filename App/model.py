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
               "nationality":None}

    catalogo['artist'] = lt.newList(datastructure= "ARRAY_LIST")
    catalogo['artworks'] = lt.newList(datastructure= "ARRAY_LIST")
    catalogo["Artw_Nacionalidades"] = lt.newList(datastructure= "ARRAY_LIST")
    catalogo["medium"] = mp.newMap(1000,maptype="CHAINING",loadfactor=4.0)
    catalogo["nationality"] = mp.newMap(1000,maptype="CHAINING",loadfactor=4.0)


    return catalogo

# Funciones para agregar informacion al catalogo
def addArtists(catalog, artist):
    lt.addLast(catalog['artist'], artist) 
    Id = artist["ConstituentID"]
    nacionalidad = artist["Nationality"]
    addArtistbyNat(catalog,Id,artist,nacionalidad)



def addArtworks(catalog, artwork):
    lt.addLast(catalog['artworks'], artwork)
    mp.put(catalog["medium"], artwork["Medium"], artwork )
def addArtw_Nt(Lista,catalog):
    lt.addLast(Lista["Artw_Nacionalidades"],catalog)
def addArtistbyNat(catalog,id,information,nacionality):
    nacionalidades = catalog["nationality"]
    artworks = catalog["artworks"]
    i = 1 
    listaObras = lt.newList(datastructure="ARRAY_LIST")
    while i < lt.size(artworks):
        artworkAcomparar = lt.getElement(artworks,i)
        constituentId = artworkAcomparar["ConstituentID"]
        if id == constituentId:
            lt.addLast(listaObras,artworkAcomparar)
        i+=1

    pass
# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
