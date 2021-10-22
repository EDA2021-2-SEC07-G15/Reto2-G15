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
 """

import config as cf
import model
import csv
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def initCatalog():
    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos
def loadData(catalog,artists,artworks):

    loadArtworks(catalog,artworks)
    loadArtists(catalog,artists)
    

def loadArtists(catalog,filename):
    """
    Carga los artistas del archivo.  
    """
    artsfile = cf.data_dir + filename
    lectura = csv.DictReader(open(artsfile, encoding="utf-8"))
    for artist in lectura:
        model.addArtists(catalog,artist)

def loadArtworks(catalog,filename):
    """
    Carga las obras de arte del archivo.  
    """
    artworksfile = cf.data_dir + filename
    lectura = csv.DictReader(open(artworksfile, encoding="utf-8"))
    for artwork in lectura:
        model.addArtworks(catalog, artwork)
    

# Funciones de ordenamiento
def sortArtistByDate(catalog, ):
    return model.sortArtistbyDate(catalog)
def sortDate(total):
    return model.sortDate(total)
def sortArtVsNatBynum(Catalogo_Art_Nacionalidad):
    return model.sortArtVsNatBynum(Catalogo_Art_Nacionalidad)
def sortDepabydate(lista_c):
    return model.sortDepBydate(lista_c)
def sortDepbyprice(listac):
    return model.sortDepbyCost(listac)

# Funciones de consulta sobre el catálogo
def artistsize(catalog):

    return model.ArtistSize(catalog)
def artworkssize(catalog):

    return model.ArtworksSize(catalog)
def getartistsByrange(catalogo,fechaInicial, fechaFinal):

    return model.getartistsByrange(catalogo,fechaInicial,fechaFinal)
def getNumberNat(cont,nacionalidad):
    
    return model.getNumberNat(cont,nacionalidad)
def Artorksinrange(catalog,date1,date2):
    return model.Artorksinrange(catalog,date1,date2)
def searchConstituentID (Lista_artista,idAw):
    return model.searchConstituentID (Lista_artista,idAw)
def NumArtByNat(catalog):
    return model.NumArtByNat(catalog)
def Calcular_Costo_dep (departamento,mapa):
    pareja = mp.get(mapa,departamento)
    valor = me.getValue(pareja)
    return model.Calcular_Costo_dep (valor)

