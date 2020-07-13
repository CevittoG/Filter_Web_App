"""

Made by CevittoG
21/03/2020 - 08/07/2020


	FUNCIONAMIENTO:
 								1. Creacion de aplicacion web
 								2. Tipo de acceso que se entregara a la credencial
 								3. Autentificacion de credencial guardada en archivo "creds.json", el cual debe estar en el mismo directorio
 								4. Creacion de cliente para utilizar credencial
 								5. Abrir archivo "Data" (primera hoja de calculo)
 								6. Extraccion de datos desde Google Sheet seleccionado
 								7. Creacion de matriz con todos los ingredientes, tal como se visualiza en Google Sheet
 								8. Creacion de matriz con todos los datos, a expecion de ingredietes
 								9. Arreglo para facilitar la impresion de los datos, contiene el titulo da cada campo de matriz anterior.
 								10. Creacion arreglo que almacenara el total de ingredientes (no se ocupa en resto de codigo)
 								11. Relleno de arreglo anterior
 								12. Pagina inicial de busqueda
 								13. Definicion ruta y metodos de transmicion de datos
 								14. Pagina Crealo en casa
 								15. Definicion ruta y metodos de transmicion de datos
 								16. Pagina Tipos de filtro
 								17. Definicion ruta y metodos de transmicion de datos
 								18. Pagina Filtro por id
 								19. Definicion ruta y metodos de transmicion de datos
 								20. Pagina Filtro por caracteristicas
 								21. Definicion ruta y metodos de transmicion de datos
 								22. Funcion busqueda de concidencias por tipo de caracteristicas implementada en Filto por caracteristicas
 								23. Pagina Mejor sanguche segun ingrediente a eleccion
 								24. Definicion ruta y metodos de transmicion de datos
 								25. Pagina Mejor sanguche segun comuna a eleccion
 								26. Definicion ruta y metodos de transmicion de datos
 								27. Pagina en la que se muestran resultados de busquedas
 								28. Definicion ruta y metodos de transmicion de datos
 								29. Implementacion de Aplicacion Web
 								30. Ejecutar y actualizar automaticamente al realizar cambios en el codigo
"""



from flask import Flask, redirect, url_for, render_template, request	# Libreria conexion Python con HTML
import gspread															# Libreria manipulacion datos Google Sheet
from oauth2client.service_account import ServiceAccountCredentials		# Libreria seguridad Google Drive API
import numpy as np    													# Libreria matrices
import pandas as pd    													# Libreria manipulacion de datos
import sys    															# Libreria manejo de sistema
import time    															# Libreria control de tiempo



# 1. Creacion de aplicacion web
app = Flask(__name__)
# 2. Tipo de acceso que se entregara a la credencial
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
# 3. Autentificacion de credencial guardada en archivo "creds.json", el cual debe estar en el mismo directorio
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
# 4. Creacion de cliente para utilizar credencial
client = gspread.authorize(creds)
# 5. Abrir archivo "Data" (primera hoja de calculo)
sanguches_tabla = client.open("Data").sheet1
# 6. Extraccion de datos desde Google Sheet seleccionado
ids = sanguches_tabla.col_values(2)						# Creacion arreglo "ids" con todos los valores de columna 2
ids.remove('ID')										# Eliminacion de titulo de columna en arreglo
links = sanguches_tabla.col_values(3)					# Creacion arreglo "ids" con todos los valores de columna 3
links.remove('Link')									# Eliminacion de titulo de columna en arreglo
ciudades = sanguches_tabla.col_values(4)				# Creacion arreglo "ids" con todos los valores de columna 4
ciudades.remove('Ciudad')								# Eliminacion de titulo de columna en arreglo
comunas = sanguches_tabla.col_values(5)					# Creacion arreglo "ids" con todos los valores de columna 5
comunas.remove('Comuna')								# Eliminacion de titulo de columna en arreglo
direcciones = sanguches_tabla.col_values(6)				# Creacion arreglo "ids" con todos los valores de columna 6
direcciones.remove('Direccion')							# Eliminacion de titulo de columna en arreglo
locales = sanguches_tabla.col_values(7)					# Creacion arreglo "ids" con todos los valores de columna 7
locales.remove('Local')									# Eliminacion de titulo de columna en arreglo
sandwichs = sanguches_tabla.col_values(8)				# Creacion arreglo "ids" con todos los valores de columna 8
sandwichs.remove('Sandwich')							# Eliminacion de titulo de columna en arreglo
valoraciones = sanguches_tabla.col_values(9)			# Creacion arreglo "ids" con todos los valores de columna 9
valoraciones.remove('Valoración 1-5')


Ing1 = sanguches_tabla.col_values(10)					# Creacion arreglo "ids" con todos los valores de columna 10
Ing1.remove('1')										# Eliminacion de numero de ingrediente (titulo de columna) en arreglo
Ing2 = sanguches_tabla.col_values(11)					# Creacion arreglo "ids" con todos los valores de columna 11
Ing2.remove('2')										# Eliminacion de numero de ingrediente (titulo de columna) en arreglo
Ing3 = sanguches_tabla.col_values(12)					# Creacion arreglo "ids" con todos los valores de columna 12
Ing3.remove('3')										# Eliminacion de numero de ingrediente (titulo de columna) en arreglo
Ing4 = sanguches_tabla.col_values(13)					# Creacion arreglo "ids" con todos los valores de columna 13
Ing4.remove('4')										# Eliminacion de numero de ingrediente (titulo de columna) en arreglo
Ing5 = sanguches_tabla.col_values(14)					# Creacion arreglo "ids" con todos los valores de columna 14
Ing5.remove('5')
Ing6 = sanguches_tabla.col_values(15)
Ing6.remove('6')
Ing7 = sanguches_tabla.col_values(16)
Ing7.remove('7')
Ing8 = sanguches_tabla.col_values(17)
Ing8.remove('8')
Ing9 = sanguches_tabla.col_values(18)
Ing9.remove('9')
Ing10 = sanguches_tabla.col_values(19)
Ing10.remove('10')
Ing11 = sanguches_tabla.col_values(20)
Ing11.remove('11')
Ing12 = sanguches_tabla.col_values(21)
Ing12.remove('12')
Ing13 = sanguches_tabla.col_values(22)
Ing13.remove('13')
Ing14 = sanguches_tabla.col_values(23)
Ing14.remove('14')
Ing15 = sanguches_tabla.col_values(24)
Ing15.remove('15')
Ing16 = sanguches_tabla.col_values(25)
Ing16.remove('16')
# 7. Creacion de matriz con todos los ingredientes, tal como se visualiza en Google Sheet
ings = np.array([Ing1, Ing2, Ing3, Ing4, Ing5, Ing6, Ing7, Ing8, Ing9, Ing10, Ing11, Ing12, Ing13, Ing14, Ing15, Ing16], dtype=object)
# 8. Creacion de matriz con todos los datos, a expecion de ingredietes
type_data = np.array([ids, links, ciudades, comunas, direcciones, locales, sandwichs, valoraciones], dtype=object)
# 9. Arreglo para facilitar la impresion de los datos, contiene el titulo da cada campo de matriz anterior.
print_data = ["N° Sandwich: ", "Link: ", "Ciudad: ", "Comuna: ", "Dirección: ", "Local: ", "Sandwich: ", "Valoración: "]
# 10. Creacion arreglo que almacenara el total de ingredientes (no se ocupa en resto de codigo)
ings_total = []
# 11. Relleno de arreglo anterior
for i in range(len(ings)):										# Recorrido numero de ingrediente en matriz
    for s in range(len(ings[i])):								# Recorrido numero de sanguche en matriz
        if (ings[i][s] != ''):									# Verificacion elemento contiene datos
            ings_total.append(ings[i][s])						# Adjuntar dato a arreglo "ings_total"

ings_total = list(dict.fromkeys(ings_total))					# Aseguracion todos datos distintos y transformacion en lista

# 12. Pagina inicial de busqueda
@app.route("/", methods=["POST", "GET"])						# 13. Definicion ruta y metodos de transmicion de datos
def home_search():
    if request.method == "POST":												# Luego de seleccionar una opcion en la pagina, retorna la elecciona a la misma pagina bajo el nombre "subject"
    	if request.form["subject"] == "make_at_home":							# Si se selecciona el boton de "Crealo en casa"
        	return redirect(url_for("crealo_en_casa"))							# Se redirecciona a la funcion "crealo_em_casa"
    	elif request.form["subject"] == "filter":								# Si se selecciona el boton de "Filtro"
        	return redirect(url_for("filtro"))									# Se redirecciona a la funcion "filtro"
    	elif request.form["subject"] == "best_ing":								# Si se selecciona el boton de "Mejor sanguche segun ingrediente a eleccion"
       		return redirect(url_for("mejor_ing_eleccion"))						# Se redirecciona a la funcion "mejor_ing_eleccion"
    	elif request.form["subject"] == "best_com":								# Si se selecciona el boton de "Mejor sanguche segun comuna a eleccion"
        	return redirect(url_for("mejor_com_eleccion"))						# Se redirecciona a la funcion "mejor_com_eleccion"
    else:																		# Primera entrada de pagina
        return render_template("home_search.html")								# Direcciona a archivo "home_search,html" en directorio "template"

# 14. Pagina Crealo en casa
@app.route("/crealo_en_casa", methods=["POST", "GET"])			# 15. Definicion ruta y metodos de transmicion de datos
def crealo_en_casa():
	if request.method == "POST":												# Luego insertar criterios de busqueda
		search_ing = request.form["data"]										# Extrae input bajo el nombre "data", y lo guarda en variable "search_ing"
		search_ing = search_ing.split(",")										# Busca cada "," y corta la variable formando un arreglo
		for n in range(len(search_ing)):										# Recorre cada componente del arreglo
			search_ing[n] = search_ing[n].strip()								# Elimina espacios en extremos de componente

		found_sand = []															# Creacion arreglo para almacenar id de coincidencias

		if search_ing == ['']:													# En caso de que el input de usuario sea nulo
			return redirect(url_for("resultados", search = search_ing, found =found_sand))	# Redirecciona a archivo "resultados" en directorio "template", junto con los datos finales
		else:																	# En caso de que el input sea distinto a nulo
			for s in range (len(ings[0])):										# Recorrido de sanguches
				for i in range(len(ings)):										# Recorrido de ingredientes
					if (ings[i][s] == ''):										# En caso de ser nulo el dato
						continue												# Se continua al siguiente ingrediente
					found = False												# Estado de la concidencia
					for t in range(len(search_ing)):							# Recorrido input de usuario
						if (search_ing[t] in str(ings[i][s])):               	# Caso 1: Completamente igual
							found = True
						elif (search_ing[t].upper() in str(ings[i][s])):     	# Caso 2: Todo en mayuscula
							found = True
						elif (search_ing[t].lower() in str(ings[i][s])):     	# Caso 3: Todo en minuscula
							found = True
						elif (search_ing[t].title() in str(ings[i][s])):     	# Caso 4: Primeras letra de cada palabra en mayuscula
							found = True
						elif (search_ing[t].capitalize() in str(ings[i][s])):	# Caso 5: Primera letra de frase en mayuscula
							found = True
					if (found == False):										# En caso de NO encontrar coincidencia
						break													# Se pasa al siguiente sanguche
				if (found == True):												# En caso de encontrar coincidencia
					found_sand.append(s)										# Se adjunta id de sanguche a arreglo de resultados
			return redirect(url_for("resultados", search = search_ing, found =found_sand))	# Redirecciona a archivo "resultados" en directorio "template", junto con los datos finales
	else:																		# Primera entrada de pagina
		return render_template("crealo_en_casa.html")							# Direcciona a archivo "crealo_en_casa" en directorio "template"

# 16. Pagina Tipos de filtro
@app.route("/filtro", methods=["POST", "GET"])					# 17. Definicion ruta y metodos de transmicion de datos
def filtro():
	if request.method == "POST":												# Luego de seleccionar una opcion en la pagina, retorna la elecciona a la misma pagina bajo el nombre "subject"
		if request.form["subject"] == "filter_id":								# Si se selecciona el boton de "Filtro por N° de sanguche"
			return redirect(url_for("filtro_id"))								# Se redirecciona a la funcion "filtro_id"
		elif request.form["subject"] == "filter_c":								# Si se selecciona el boton de "Filtro por caracteristica de sanguche"
			return redirect(url_for("filtro_c"))								# Se redirecciona a la funcion "filtro_c"
		elif request.form["subject"] == "main_menu":							# Si se selecciona el boton de "Menu inicial de busqueda"
			return redirect(url_for("home_search"))								# Se redirecciona a la funcion "home_search"
	else:																		# Primera entrada de pagina
		return render_template("filter.html")									# Direcciona a archivo "home_search,html" en directorio "template"

# 18. Pagina Filtro por id
@app.route("/filtro_id", methods=["POST", "GET"])				# 19. Definicion ruta y metodos de transmicion de datos
def filtro_id():
	if request.method == "POST":												# Luego insertar criterios de busqueda
		search_ing = request.form["data"]										# Extrae input bajo el nombre "data", y lo guarda en variable "search_ing"
		search_ing = search_ing.split(",")										# Busca cada "," y corta la variable formando un arreglo
		for n in range(len(search_ing)):										# Recorre cada componente del arreglo
			search_ing[n] = search_ing[n].strip()								# Elimina espacios en extremos de componente

		found_sand = []															# Creacion arreglo para almacenar id de coincidencias
		
		if search_ing == ['']:													# En caso de que el input de usuario sea nulo
			return redirect(url_for("resultados", search = search_ing, found =found_sand))	# Redirecciona a archivo "resultados" en directorio "template", junto con los datos finales
		else:																	# En caso de que el input sea distinto a nulo
			for num_id in search_ing:											# Recorre cada componente de "search_ing"
				for d in range(len(type_data[0])):								# Recorre cada componente de "ids" en "type_data"
					if (num_id == str(type_data[0][d])):						# En caso de ser ambos componentes iguales
						found_sand.append(d)									# Se adjunta id de sanguche a arreglo de resultados
			return redirect(url_for("resultados", search = search_ing, found =found_sand))	# Redirecciona a archivo "resultados" en directorio "template", junto con los datos finales
	else:																		# Primera entrada de pagina
		return render_template("filter_id.html")								# Direcciona a archivo "crealo_en_casa" en directorio "template"

# 20. Pagina Filtro por caracteristicas
@app.route("/filtro_c", methods=["POST", "GET"])				# 21. Definicion ruta y metodos de transmicion de datos
def filtro_c():
	if request.method == "POST":												# Luego insertar criterios de busqueda
		search_ing = request.form["data"]										# Extrae input bajo el nombre "data", y lo guarda en variable "search_ing"
		search_ing = search_ing.split(",")										# Busca cada "," y corta la variable formando un arreglo
		for n in range(len(search_ing)):										# Recorre cada componente del arreglo
			search_ing[n] = search_ing[n].strip()								# Elimina espacios en extremos de componente

		found_sand = []															# Creacion arreglo para almacenar id de coincidencias

		if search_ing == ['']:													# En caso de que el input de usuario sea nulo
			return redirect(url_for("resultados", search = search_ing, found =found_sand))	# Redirecciona a archivo "resultados" en directorio "template", junto con los datos finales
		else:																	# En caso de que el input sea distinto a nulo
			f_sand1 = []														# Creacion arreglo para almacenar id de coincidencias con el primer componente de "search_ing"
			f_sand2 = []														# Creacion arreglo para almacenar id de coincidencias con el segundo componente de "search_ing"
			f_sand3 = []														# Creacion arreglo para almacenar id de coincidencias con el tercer componente de "search_ing"
			f_sand4 = []
			f_sand5 = []
			f_sand6 = []
			f_sand7 = []
			f_sand8 = []
			f_sand9 = []
			f_sand10 = []
			f_sand11 = []
			f_sand12 = []
			f_sand13 = []
			f_sand14 = []
			f_sand15 = []
			f_sand16 = []
			f_sand17 = []
			f_sand18 = []
			f_sand19 = []
			f_sand20 = []
			
			f_sand1 = search_data(search_ing, 0, f_sand1)						# Busqueda de concidencias para f_sand1 ocupando funcion "search_data" 
			f_sand2 = search_data(search_ing, 1, f_sand2)						# Busqueda de concidencias para f_sand2 ocupando funcion "search_data" 
			f_sand3 = search_data(search_ing, 2, f_sand3)						# Busqueda de concidencias para f_sand3 ocupando funcion "search_data" 
			f_sand4 = search_data(search_ing, 3, f_sand4)
			f_sand5 = search_data(search_ing, 4, f_sand5)
			f_sand6 = search_data(search_ing, 5, f_sand6)
			f_sand7 = search_data(search_ing, 6, f_sand7)
			f_sand8 = search_data(search_ing, 7, f_sand8)
			f_sand9 = search_data(search_ing, 8, f_sand9)
			f_sand10 = search_data(search_ing, 9, f_sand10)
			f_sand11 = search_data(search_ing, 10, f_sand11)
			f_sand12 = search_data(search_ing, 11, f_sand12)
			f_sand13 = search_data(search_ing, 12, f_sand13)
			f_sand14 = search_data(search_ing, 13, f_sand14)
			f_sand15 = search_data(search_ing, 14, f_sand15)
			f_sand16 = search_data(search_ing, 15, f_sand16)
			f_sand17 = search_data(search_ing, 16, f_sand17)
			f_sand18 = search_data(search_ing, 17, f_sand18)
			f_sand19 = search_data(search_ing, 18, f_sand19)
			f_sand20 = search_data(search_ing, 19, f_sand20)
			# Se crea matriz con todos los f_sandX para recorrer resultados
			found_sand = np.array([f_sand2, f_sand3, f_sand4, f_sand5, f_sand6, f_sand7, f_sand8, f_sand9, f_sand10, f_sand11, f_sand12, f_sand13, f_sand14, f_sand15, f_sand16, f_sand17, f_sand18, f_sand19, f_sand20], dtype=object)
			final_found_sand = []												# 
			# Para cada elemento de f_sand1 se recorre todos los datos de found_sand buscando que se repitan ids.
			# Para cada ingrediente de f_sand1 que se repita en todos los f_sandX (X >= 2), se guarda en final_found_sand el id
			if (len(search_ing) == 1):												# En el caso de solo ingresar una caracteristica como input
				final_found_sand = f_sand1    										# El resultado final de coincidencias es igual a f_sand1
			else:
				for k in range(len(f_sand1)):                                       # Se escoge el sandwich numero f_sand1[k] para realizar comparaciones
					count = 0                                                       # Comienza contador que nos ayuda a verificar que dicho sandwich se repita en todas las listas
					for p in range(len(search_ing)-1):                              # Se analizan las primeras len(search_ing)-1 -----> Numero de ingredientes que se ingresaron por pantalla menos uno 
						isThere = False                                             # Cada vez que comienza el analisis en un nuevo f_sand, se establece isThere
						for x in range(len(found_sand[p])):                         # Se recorren todos los id guardados en found_sand[p] ---> f_sandp+2
							if (f_sand1[k] == found_sand[p][x]):                    # Comparacion de id guardado en f_sand1[k] con cada id guardado en f_sandp+2
								isThere = True                                      # Despues de encontrar similitud, se cambia el estado de isThere
						if (isThere == False):                                      # Al terminar de recorrer found_sand[p] (f_sandp+2), se verifica si hubo alguna similitud en dicha lista
							break                                                   # Si no encuntra f_sand1[k] en esa lista, se pasa a f_sand1[k+1]
						else:
							count += 1                                              # Si se encuentra f_sand1[k] en la lista analizada, se le suma uno al contador
					if (count == len(search_ing)-1):                                # Despues de comparar f_sand1[k] con todos los datos de found_sand, se verifica haber encontrado 
		                                                                            # coincidencias en todos los f_sandX (X >= 2).
						final_found_sand.append(f_sand1[k])                         # Se agrega el id del sandwich a un nuevo arreglo llamado final_found_sand
			found_sand = final_found_sand											# Registro final de ids de sanguches en arreglo de resultados

			return redirect(url_for("resultados", search = search_ing, found =found_sand))	# Redirecciona a archivo "resultados" en directorio "template", junto con los datos finales
	else:																			# Primera entrada de pagina
		return render_template("filter_c.html")										# Direcciona a archivo "crealo_en_casa" en directorio "template"


# 22. Funcion busqueda de concidencias por tipo de caracteristicas implementada en Filto por caracteristicas
def search_data (a, k, b):              
    if (len(a) <= k):                                          					# INGREDIENTES ---------------------------------------------------------------------
        return																	# Identifica cuando se llega al ultimo componente de "search_ing"
    else:
        for t in range(len(ings)):												# Recorrido numero de ingrediente en matriz
            for l in range(len(ings[t])):										# Recorrido numero de sanguche en matriz
                if (a[k] in str(ings[t][l])):                  					# Caso 1: Completamente igual
                    b.append(l)
                elif (a[k].upper() in str(ings[t][l])):        					# Caso 2: Todo en mayuscula
                    b.append(l)
                elif (a[k].lower() in str(ings[t][l])):        					# Caso 3: Todo en minuscula
                    b.append(l)
                elif (a[k].title() in str(ings[t][l])):        					# Caso 4: Primeras letra de cada palabra en mayuscula
                    b.append(l)
                elif (a[k].capitalize() in str(ings[t][l])):   					# Caso 5: Primera letra de frase en mayuscula
                    b.append(l)
    
    if (len(a) <= k):                                          					# CIUDADES ---------------------------------------------------------------------
        return																	# Identifica cuando se llega al ultimo componente de "search_ing"
    else:		
        for h in range(len(ciudades)):											# Recorre componentes de arreglo "ciudades"
            if (a[k] in str(ciudades[h])):                     					# Caso 1: Completamente igual
                b.append(h)
            elif (a[k].upper() in str(ciudades[h])):           					# Caso 2: Todo en mayuscula
                b.append(h)
            elif (a[k].lower() in str(ciudades[h])):           					# Caso 3: Todo en minuscula
                b.append(h)
            elif (a[k].title() in str(ciudades[h])):           					# Caso 4: Primeras letra de cada palabra en mayuscula
                b.append(h)
            elif (a[k].capitalize() in str(ciudades[h])):      					# Caso 5: Primera letra de frase en mayuscula
                b.append(h)
    
    if (len(a) <= k):                                          					# COMUNAS ---------------------------------------------------------------------
        return																	# Identifica cuando se llega al ultimo componente de "search_ing"
    else:
        for d in range(len(comunas)):											# Recorre componentes de arreglo "comunas"
            if (a[k] in str(comunas[d])):                     					# Caso 1: Completamente igual
                b.append(d)
            elif (a[k].upper() in str(comunas[d])):           					# Caso 2: Todo en mayuscula
                b.append(d)
            elif (a[k].lower() in str(comunas[d])):           					# Caso 3: Todo en minuscula
                b.append(d)
            elif (a[k].title() in str(comunas[d])):           					# Caso 4: Primeras letra de cada palabra en mayuscula
                b.append(d)
            elif (a[k].capitalize() in str(comunas[d])):      					# Caso 5: Primera letra de frase en mayuscula
                b.append(d)
    
    
    if (len(a) <= k):                                          					# LOCALES ---------------------------------------------------------------------
        return																	# Identifica cuando se llega al ultimo componente de "search_ing"
    else:
        for u in range(len(locales)):											# Recorre componentes de arreglo "locales"
            if (a[k] in str(locales[u])):                     					# Caso 1: Completamente igual
                b.append(u)
            elif (a[k].upper() in str(locales[u])):           					# Caso 2: Todo en mayuscula
                b.append(u)
            elif (a[k].lower() in str(locales[u])):           					# Caso 3: Todo en minuscula
                b.append(u)
            elif (a[k].title() in str(locales[u])):           					# Caso 4: Primeras letra de cada palabra en mayuscula
                b.append(u)
            elif (a[k].capitalize() in str(locales[u])):      					# Caso 5: Primera letra de frase en mayuscula
                b.append(u)
    
    if (len(a) <= k):                                          					# SANDWICH ---------------------------------------------------------------------
        return																	# Identifica cuando se llega al ultimo componente de "search_ing"
    else:
        for v in range(len(sandwichs)):											# # Recorre componentes de arreglo "sandwichs"
            if (a[k] in str(sandwichs[v])):                     				# Caso 1: Completamente igual
                b.append(v)
            elif (a[k].upper() in str(sandwichs[v])):           				# Caso 2: Todo en mayuscula
                b.append(v)
            elif (a[k].lower() in str(sandwichs[v])):           				# Caso 3: Todo en minuscula
                b.append(v)
            elif (a[k].title() in str(sandwichs[v])):           				# Caso 4: Primeras letra de cada palabra en mayuscula
                b.append(v)
            elif (a[k].capitalize() in str(sandwichs[v])):      				# Caso 5: Primera letra de frase en mayuscula
                b.append(v)
    
    if (len(a) <= k):                                          					# VALORACION ---------------------------------------------------------------------
        return																	# Identifica cuando se llega al ultimo componente de "search_ing"
    else:
        for x in range(len(valoraciones)):										# Recorre componentes de arreglo "valoraciones"
            if (a[k] in str(valoraciones[x])):                     				# Caso 1: Completamente igual
                b.append(x)
            elif (a[k].upper() in str(valoraciones[x])):           				# Caso 2: Todo en mayuscula
                b.append(x)
            elif (a[k].lower() in str(valoraciones[x])):           				# Caso 3: Todo en minuscula
                b.append(x)
            elif (a[k].title() in str(valoraciones[x])):           				# Caso 4: Primeras letra de cada palabra en mayuscula
                b.append(x)
            elif (a[k].capitalize() in str(valoraciones[x])):      				# Caso 5: Primera letra de frase en mayuscula
                b.append(x)
    
    return b  																	# Retorna arreglo con id de sanguches que presentan coincidencias

# 23. Pagina Mejor sanguche segun ingrediente a eleccion
@app.route("/mejor_ing_eleccion", methods=["POST", "GET"])		# 24. Definicion ruta y metodos de transmicion de datos
def mejor_ing_eleccion():
	if request.method == "POST":												# Luego insertar criterios de busqueda
		search_ing = request.form["data"]										# Extrae input bajo el nombre "data", y lo guarda en variable "search_ing"
		search_ing = search_ing.split(",")										# Busca cada "," y corta la variable formando un arreglo
		for n in range(len(search_ing)):										# Recorre cada componente del arreglo
			search_ing[n] = search_ing[n].strip()								# Elimina espacios en extremos de componente

		found_sand = []															# Creacion arreglo para almacenar id de coincidencias

		if search_ing == ['']:													# En caso de que el input de usuario sea nulo
			return redirect(url_for("resultados", search = search_ing, found =found_sand))	# Redirecciona a archivo "resultados" en directorio "template", junto con los datos finales
		else:																	# En caso de que el input sea distinto a nulo
			for t in range(len(ings)):											# Recorre numero de ingredientes 
				for l in range(len(ings[t])):									# Recorre numero de sanguche
					if (search_ing[0] in str(ings[t][l])):                     	# Caso 1:Completamente igual
						found_sand.append(l)
					elif (search_ing[0].upper() in str(ings[t][l])):           	# Caso 2: Todo en mayuscula
						found_sand.append(l)
					elif (search_ing[0].lower() in str(ings[t][l])):           	# Caso 3: Todo en minuscula
						found_sand.append(l)
					elif (search_ing[0].title() in str(ings[t][l])):           	# Caso 4: Primeras letra de cada palabra en mayuscula
						found_sand.append(l)
					elif (search_ing[0].capitalize() in str(ings[t][l])):      	# Caso 5: Primera letra de frase en mayuscula
						found_sand.append(l)
			return redirect(url_for("resultados", search = search_ing, found =found_sand))	# Redirecciona a archivo "resultados" en directorio "template", junto con los datos finales
	else:																		# Primera entrada de pagina
		return render_template("ing_choice.html")								# Direcciona a archivo "crealo_en_casa" en directorio "template"

# 25. Pagina Mejor sanguche segun comuna a eleccion
@app.route("/mejor_com_eleccion", methods=["POST", "GET"])		# 26. Definicion ruta y metodos de transmicion de datos
def mejor_com_eleccion():
	if request.method == "POST":												# Luego insertar criterios de busqueda
		search_com = request.form["data"]										# Extrae input bajo el nombre "data", y lo guarda en variable "search_ing"
		search_com = search_com.split(",")										# Busca cada "," y corta la variable formando un arreglo
		for n in range(len(search_com)):										# Recorre cada componente del arreglo
			search_com[n] = search_com[n].strip()								# Elimina espacios en extremos de componente

		found_sand = []															# Creacion arreglo para almacenar id de coincidencias
		
		if search_com == ['']:													# En caso de que el input de usuario sea nulo
			return redirect(url_for("resultados", search = search_com, found =found_sand))	# Redirecciona a pagina "resultados", junto con los datos finales
		else:																	# En caso de que el input sea distinto a nulo
			for t in range(len(comunas)):										# Recorre numero de comunas
				if (search_com[0] in str(comunas[t])):                     		# Caso 1:Completamente igual
					found_sand.append(t)
				elif (search_com[0].upper() in str(comunas[t])):           		# Caso 2: Todo en mayuscula
					found_sand.append(t)
				elif (search_com[0].lower() in str(comunas[t])):           		# Caso 3: Todo en minuscula
					found_sand.append(t)
				elif (search_com[0].title() in str(comunas[t])):           		# Caso 4: Primeras letra de cada palabra en mayuscula
					found_sand.append(t)
				elif (search_com[0].capitalize() in str(comunas[t])):      		# Caso 5: Primera letra de frase en mayuscula
					found_sand.append(t)
			return redirect(url_for("resultados", search = search_com, found =found_sand))	# Redirecciona a pagina "resultados", junto con los datos finales
	else:																		# Primera entrada de pagina
		return render_template("com_choice.html")								# Direcciona a archivo "crealo_en_casa" en directorio "template"

# 27. Pagina en la que se muestran resultados de busquedas
@app.route("/<search><found>", methods=["POST", "GET"])			# 28. Definicion ruta y metodos de transmicion de datos
def resultados(search, found):
	if request.method == "POST":												# Luego de seleccionar boton
		return redirect(url_for("home_search"))									# Redirecciona a pagina "home_search"
	else:																		# Primera entrada de pagina
		if (search == "[]"):													# En caso de que el input de usuario sea nulo
		    return "<h1>ERROR</h1><br><p>Debe agregar un dato a la busqueda</p>"	# Mensaje de error
		else:																	# En caso de que el input sea distinto a nulo
			data = search.lower()												# Transformar datos de variable (al traspasar datos de una pagina a otra, estos pierden el formato y se transforman en una solo string)
			data = data.replace("'", "")										# Remplazo de "'" (comilla simple) por un valor nulo
			data = data.replace("[", "")										# Remplazo de "[" por un valor nulo
			data = data.replace("]", "-")										# Remplazo de "]" por "-" (guion)

			found_str = "" 														# Creacion de string
			search_input = []													# Creacion de arreglo
			separation = False													# Creacion de variable booleana que permite saber cuando separar valores
			for n in range(len(data)):											# Recorrido de string "data"
				if (separation == True):										# En el caso de reconocer la separacion como verdadera
					found_str = found_str + data[n]								# Agrega el componente de "data" a string "found_str"
				elif (data[n] == "-"):											# En el caso de reconocer "-" (guion)
					separation = True											# Se establece el valor de "separacion" como verdadero
				elif separation == False:										# En el caso de reconocer la separacion como falsa
					search_input.append(data[n])								# Se agrega componente de "data" a arreglo "search_input"
			found_str = found_str.replace(' ', '')								# Remplazo de " " (espacio) por un valor nulo
			found_str = found_str + ','											# Agregar "," (coma) al final de string
			number = ""															# Creacion string
			found_id = []														# Creacion arreglo con coincidencia final de id sanguches
			if found_str == ',':												# En el caso de que "found_str" haya sido nulo y por lo tanto ahora solo posea una coma
				found_id = []													# Se establece "found_id" como nulo# 
			else:																
				for g in range(len(found_str)):									# Recorrido de string 
					if found_str[g] == ",":										# Al momento de encontrar una coma
						found_id.append(int(number))							# Se agrega el string "number" al arreglo
						number = ""												# Se reestablece el string "number" como nulo
					else:														# En el caso de no se una coma el componente
						number = number + found_str[g]							# Se agrega el componente al string
			best_sand = 0														# Creacion variable numerica
			best_id = []														# Creacion arreglo
			for f in found_id:													# Recorrido de arreglo "found_id"
				if (valoraciones[f] == ''):										# Si uno de los sanguches no posee valoracion
					continue													# Se continua al siguiente id
				elif (int(valoraciones[f]) > int(best_sand)):					# En el caso de que una valoracion de un sanguche sea mayor a la mejor valoracion registrada
					best_sand = valoraciones[f]									# Se reestablece el valor de "best_sand" para tener la mejor valoracion entre las coincidencias
			for f in found_id:													# Recorrido de arreglo "found_id"
				if (valoraciones[f] == best_sand):								# En el caso de encontrar una coincidencia entre las valoraciones de sanguches (resultados) y el mejor valore registrado
					best_id.append(f)											# Se registra el id del sanguche como uno de los mejores en "best_id"

			return render_template("results.html", search_input = search_input, found_id = found_id, type_data = type_data, len_td = len(type_data), ings = ings, len_in = len(ings), best_id = best_id, print_data = print_data)	# 

# 29. Implementacion de Aplicacion Web
if __name__ == "__main__":
	app.run(debug = True)										# 30. Ejecutar y actualizar automaticamente al realizar cambios en el codigo

# ---------------------------------------------------- Made by CevittoG ---------------------------------------------------- #