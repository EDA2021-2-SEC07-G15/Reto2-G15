"""
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
from DISClib.ADT import list as lt
assert cf
import time


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Inicializar el catálogo")
    print("2- Cargar información en el catálogo")
    print("3- Requerimiento lab 6")

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

    elif int(inputs[0]) == 2:
        print("Cargando información de los archivos ....")
        start_time = time.process_time()
        controller.loadData(cont,'Artists-utf8-small.csv','Artworks-utf8-small.csv')
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        print(elapsed_time_mseg)
        print("Se cargo exitosamente la información")
        print("Artistas cargados: " + str(controller.artistsize(cont)))
        print("Artworks cargados: " + str(controller.artworkssize(cont)))
    elif int(inputs[0]) == 3:
        # Requerimiento para lab #6 
        nacionalidad = input("Ingrese una nacionalidad: ")
        total = controller.getNumberNat(cont,nacionalidad)
        print ("Hay" + str(total) + " obras con esa nacionalidad")
    elif int(inputs[0]) == 4:
        fechaInicial = int(input("Digite el año inicial (YYYY): "))
        fechaFinal = int(input("Digite el año final (YYYY): "))
        total = controller.getartistsByrange (cont,fechaInicial,fechaFinal)
        print("Hay " + str(total[0]) + " artistas entre " + str(fechaInicial) + " y " + str(fechaFinal))
        print(lt.getElement(total[1],lt.size(total[1])))

    else:
        sys.exit(0)
sys.exit(0)
