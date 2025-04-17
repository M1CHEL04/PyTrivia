## Funciones para resolver el inciso 4 de consulta.
def generate_list_lowers(data_censo,index_Jurisdiccion,index_poblacion,value):
    """
    This function creates a list with the names of the provinces, which have a population less 
    than the value passed as parameter (value).
    """

    list_provinces = []

    for row in data_censo:
        if int(row[index_poblacion]) < value:
            if not (row[index_Jurisdiccion]) in list_provinces:
                if (row[index_Jurisdiccion].lower() != "total del pais"):
                    list_provinces.append(row[index_Jurisdiccion])

    return list_provinces

def generate_list_highers(data_censo,index_Jurisdiccion,index_poblacion,value):
    """
    This function creates a list with the names of the provinces, which have a population greater than the value passed as parameter (value).
    """

    list_provinces = []

    for row in data_censo:
        if int(row[index_poblacion]) > value:
            if not (row[index_Jurisdiccion]) in list_provinces:
                if (row[index_Jurisdiccion].lower() != "total del pais"):
                    list_provinces.append(row[index_Jurisdiccion])
    
    return list_provinces

def nom_prov_private (header_censo,data_censo, value):
    """ 
    This function is private to the 'prov_name' function.
    Returns a list with the names of the provinces, according to the search criteria
    entered by the user.
    """

    #Obtengo los indices de los datos a utilizar
    index_Jurisdiction = header_censo.index("Jurisdiccion")
    index_population = header_censo.index("Total de poblacion")

    critery = input("Ingrese el criterio de busqueda (menor o mayor)").lower()
    while(True):
        if (critery == "mayor" or critery == "menor"):
            break
        else:
            critery = input("Error al ingreso. Por favor ingrese menor o mayor").lower()

    match critery:
        case critery if critery == "menor":
            return generate_list_lowers(data_censo,index_Jurisdiction,index_population,value)
        case critery if critery == "mayor":
            return generate_list_highers(data_censo,index_Jurisdiction,index_population,value)



def nom_prov (header_censo,data_censo):
    """ This function returns a list, with the names of the provinces with a 
    smaller or larger population than the value entered by the user. """
    
    value = (input("Ingrese un valor de poblacion."))
    while(True):
        if value.isdigit():
            value=int(value)
            break
        else:
            value= input("Error al ingreso. Por favor ingrese nuevamente el valor de la poblacion.")

    list_provinces = nom_prov_private(header_censo,data_censo,value)

    return list_provinces


def nom_airports (header_air,data_air,list_provs):
    """ This function returns a list with the names of the airports that are in the provinces passed as a parameter"""
    
    ## Obtengo los indices de los datos a utilizar.
    index_name = header_air.index("name")
    index_prov_name = header_air.index("prov_name")

    list_airports = []

    for row in data_air:
        if row[index_prov_name] in list_provs:
            list_airports.append(row[index_name])
    
    return list_airports


def nom_lakes (header_lagos,data_lagos,list_provs):
    """
    This function returns a list with the names of the lakes that are in the processed provinces
    """
    index_nombre = header_lagos.index("Nombre")
    index_ubicacion = header_lagos.index("Ubicacion")

    list_lakes = []

    for row in data_lagos:
        if row[index_ubicacion] in list_provs:
            list_lakes.append(row[index_nombre])
    
    return list_lakes


def types_conection (header_tc,data_tc,list_provs):
    """ This function returns a dictionary of lists, where the keys are the names of the provinces
     and the lists are the different types of connectivity that the processed provinces have."""

    list_provs = remove_accents(list_provs)

    dict_prov = generate_dict(list_provs)

    list_index_tc = index_type_conection(header_tc)

    return types_conection_private(header_tc,data_tc,dict_prov,list_index_tc)

def index_type_conection(header_tc):
    """ 
    This function is private to the 'types_connection' function.
    This function returns a list with the indices of the columns of the connectivity types 
    that the .csv file has
    """
    list_index = []

    index_adsl = header_tc.index("ADSL")
    index_cablemodem = header_tc.index("CABLEMODEM")
    index_dialup = header_tc.index("DIALUP")
    index_fibraop = header_tc.index("FIBRAOPTICA")
    index_satelital = header_tc.index("SATELITAL")
    index_wireless = header_tc.index("WIRELESS")
    index_telfijo = header_tc.index("TELEFONIAFIJA")
    index_3g = header_tc.index("3G")
    index_4g = header_tc.index("4G")

    list_index.append(index_adsl)
    list_index.append(index_cablemodem)
    list_index.append(index_dialup)
    list_index.append(index_fibraop)
    list_index.append(index_satelital)
    list_index.append(index_wireless)
    list_index.append(index_telfijo)
    list_index.append(index_3g)
    list_index.append(index_4g)

    return list_index


def types_conection_private(header_tc,data_tc,dict_prov,list_index_tc):
    """
    This function is private to the 'types_connection' function.
    This function returns the list dictionary, where each list belongs to a province, 
    with the names of the connectivity types that each province has.
    """
    index_prov = header_tc.index("Provincia")

    for row in data_tc:
        if row[index_prov].lower() in dict_prov:
            for i in list_index_tc:
                if row[i] == "SI":
                    if not header_tc[i] in dict_prov[row[index_prov].lower()]:
                        dict_prov[row[index_prov].lower()].append(header_tc[i])

    return dict_prov


def generate_dict (list_provs):
    """ This function receives a list and returns a dictionary of lists, where the keys take 
    the values of the list (parameter) as their name."""
    dict_prov = {}

    for prov in list_provs:
        prov = prov.lower()
        dict_prov[prov] = []
    
    return dict_prov

def remove_accents(list_provs):
    """ This function receives a list of strings, removes the accents from the strings contained in the list and returns said list."""
    for i, province in enumerate(list_provs):
        province = remove_accents_private(province)
        list_provs[i] = province
    
    return list_provs

def remove_accents_private(word):
    """ 
    Private function of the 'remove_accents' function.
    This function removes accents from a word.
    """
    # Define un diccionario de caracteres acentuados y sus equivalentes sin acento
    replacements = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U'
    }

    # Utiliza una expresión regular para buscar los caracteres acentuados y reemplazarlos
    for accentuated, without_accent in replacements.items():
        word = word.replace(accentuated, without_accent)

    return word

##Funciones para resolver el inciso 5 de consulta.
def ret_capitals(header_ar,data_ar):
    """
    This function is private to the 'get_airports_capitales' function.
    Returns a list with the names of the capitals of each province.
    """

    index_cap = header_ar.index("capital")
    index_city = header_ar.index("city")

    list_capitals = []
    for row in data_ar:
        if(str(row[index_cap]) == "admin"):
            city_name = str(row[index_city])
            if not city_name in list_capitals:
                list_capitals.append(city_name)
    
    return list_capitals

def ret_airports(header_airport,data_airport,list_capitals):
    """
    This function is private to the 'get_airports_capitales' function.
    Returns a list with the names of the airports that are in the capitals passed as a parameter (list_capitales).
    """

    index_name = header_airport.index("name")
    index_municipality = header_airport.index("municipality")

    list_airports = []

    for row in data_airport:
        if(row[index_municipality]) in list_capitals:
            if not(row[index_name]) in list_airports:
                list_airports.append(row[index_name])
    
    return list_airports

def obtener_airports_capitales(header_ar,data_ar,header_airport,data_airport):
    """
    This function returns a list with the names of the airports that are located in the capitals
    of each province.
    """

    list_capitales = ret_capitals(header_ar,data_ar)
    list_airports = ret_airports(header_airport,data_airport,list_capitales)

    return list_airports

#Funciones para resolver el inciso 6 de consulta.
def lakes_sup(header,data):
    """This function returns a list, with the names of the lakes that are classified as small, 
    medium, large, according to the surface entered."""

    sup_input = input(f"Ingrese el tamaño de la superficie.(chico,medio,grande)").lower()
    while True:
        if(sup_input == "chico" or sup_input == "medio" or sup_input == "grande"):
            break
        else: 
            sup_input = input(f"Error al ingresar el dato, por favor ingrese nuevamente el tamaño de la superficie.(chico,medio,grande)").lower()
    list_lakes = get_lakes(header,data,sup_input)

    return list_lakes



def get_lakes(header,data,sup_input):
    """ 
    This function is private to the lakes_sup function.
    This function returns a list with the name of the lakes, according to the surface passed
    by parameter.
    """
    index_Sup_size = header.index("Sup Tamaño")
    index_name = header.index("Nombre")
    list_lakes = []

    for row in data:
        if(row[index_Sup_size] == sup_input):
            list_lakes.append(row[index_name])
    
    return list_lakes