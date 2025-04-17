
def show_connectivity_count(header, data):
    """
    This function receives the dataset of connectivities separated by header and data and
    returns a dictionary with each connectivity name as a key and the number 
    of cities with that connectivity as value
    """
    # creo variables auxiliares con solo las columnas con los nombres de las conectividades
    header_aux = header[4:13]
    data_aux = [element[4:13] for element in data]

    # agrega los nombres de las conectividades como clave y les asigna el valor 0 
    connectivity_dict = {}
    for k in header_aux:
        connectivity_dict[k] = 0

    # si la ciudad posee la conectividad, se le suma 1 a la misma
    for row in data_aux:
        for e in range(len(row)): # uso range() para usar los numeros como indices
            if row[e] == 'SI':
                connectivity_dict[header_aux[e]] += 1
    
    return connectivity_dict


def create_provinces_list(data):
    """
        This function returns the unique values taken from the 
        column name "provincia" in the connectivity dataset
    """
    provinces = [] 
    
    # crea una lista con los valores unicos de la columna "provincia"
    for row in data:
        if row[0] not in provinces:
            provinces.append(row[0])
    
    return provinces

def top_optic_fiber_province(data):
    """
    This function receives the dataset of connectivities and
    creates a list with all the provinces with "fibra óptica" in all their cities
    """
    # crea lista de provincias sin repeticiones
    provinces = create_provinces_list(data)
    
    # Filtra las provincias eliminandolas de la lista previamente creada si una de sus ciudades no posee fibra optica
    for row in data:
        if row[7] == "NO":
            if row[0] in provinces:
                provinces.remove(row[0])

    return provinces

def remove_accents(string): # al sacarle tildes al dataset ya no se utiliza esta funcion
    """
    This function receives a string and return the same without accent marks
    """
    
    a,b = 'áéíóúü','aeiouu'
    trans = str.maketrans(a,b) #agregar mayusculas

    string = string.translate(trans)
    string = string.upper()

    return string

def get_capital_connectivity(data_connectivity, data_cities): 
    """
    This function receives the dataset of connectivities and the dataset of cities and
    creates a list with province, city and connectivity status

    """
    capital_connectivity=[]

    # crea una lista de provincias con sus capitales
    for row in data_cities:
        if row[6] == "admin":
            capital_connectivity.append([row[5].lower(), row[0].lower()]) # provincia, ciudad
    
    # si la provincia con su capital esta en el dataset conectividades, le agrega si posee o no conectividad
    for row in data_connectivity:
        for element in capital_connectivity:
            if [row[0].lower(), row[2].lower()] == element: 
                element.append(row[16]) # SI o NO posee conectividad
                
    # agrega "conectividad desconocida" a las provincias que el dataset conectividades no conoce su ciudad
    for element in capital_connectivity:
        if len(element) == 2:
            element.append("conectividad desconocida")
            


    return capital_connectivity


