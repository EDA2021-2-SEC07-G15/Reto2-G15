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
def LoadArtNat (catalogo,lista):
    model.addArtw_Nt(lista,catalogo)

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
