def list_airport_types (header,data):
    """This function returns all the airports types"""
    index_type=header.index('type')
    list=[]
    for row in data:
        if row[index_type] != '':
            if not(row[index_type] in list):
                list.append(row[index_type])
    return list

def enter_elevation_name(header,data):
    """This function asks the user to enter "low" , "medium" or "high" and returns the airports with that height name"""
    name= (input("Ingresa bajo, medio o alto para listar los aeropuertos con dicho nombre de altitud")).lower()
    while(True):
        if(name == "bajo" or name == "medio" or name == "alto"):
            break
        else:
            name = (input("Error al ingreso. Ingresa bajo, medio o alto para listar los aeropuertos con dicho nombre de altitud")).lower()
    list= search_airports(header,data,name)
    return list

#esta es una funcion interna y desarollada para su ejecucion dentro de la funcion "enter_elevation_name"
def search_airports(header,data,name):
    """This function returns all the airports with the height name passed by parameter"""
    index_elevation_name=header.index('elevation_name')
    index_name=header.index('name')
    list=[]
    for row in data:
        if row[index_elevation_name] == name:
            #controlo que no lo haya agregado anterirormente, dado que puede estar repetido dicho aeropuerto en el dataset.
            if not(row[index_name]in list):
                list.append(row[index_name])
            else:
                continue
        else:
            continue
    return list

def enter_elevation_num(header,data):
    """This function asks the user to enter "higher" or "lower" and a height value in meters 
    and returns the appropriated airports"""
    key_word= input("Ingrese mayor o menor").lower()
    while(True):
        if (key_word == "mayor" or key_word == "menor"):
            break
        else:
            key_word= input("Error al ingreso. Por favor ingrese mayor o menor").lower()
    elevation= input("ingrese una altura en metros que desee listar los aeropuertos con mayor o menor altura que dicho valor")
    while(True):
        if elevation.isdigit():
            #hago la conversion de unidades, dado que me ingresan la altura en metros y en mis datos la altura esta en pies.
            elevation_ft= int(int(elevation) * 3.28024)
            break
        else:
            elevation= input("Error al ingreso. Porfavor ingrese nuevamente la altura en metros que desea listar los aeropuertos.")
    return elevation_list(header,data,elevation_ft,key_word)

#esta es una funcion interna y desarollada para su ejecucion dentro de la funcion "enter_elevation_num"
def elevation_list (header,data,elevation,key_word):
    """This function decides whether to return airports higher or lower than the height passed by parameter"""
    index_elevation_ft=header.index('elevation_ft')
    index_name=header.index('name')
    if (key_word == "mayor"):
        return higher_elevation(header,data,elevation,index_elevation_ft,index_name)
    else:
        return lower_elevation(header,data,elevation,index_elevation_ft,index_name)

#esta es una funcion interna y desarollada para su ejecucion dentro de la funcion "elevation_list"
def higher_elevation (header,data,elevation,index_elevation_ft,index_name):
    """This function add the airports with height grater than the given one to a list"""
    list=[]
    for row in data:
        if (row[index_elevation_ft].isdigit()):
            if (int(row[index_elevation_ft])) > elevation:
                #controlo que no lo haya agregado anterirormente, dado que puede estar repetido dicho aeropuerto en el dataset.
                if not(row[index_name] in list):
                    list.append(row[index_name])
            else:
                continue
        else:
            continue
    return list

#esta es una funcion interna y desarollada para su ejecucion dentro de la funcion "elevation_list"
def lower_elevation (header,data,elevation,index_elevation_ft,index_name):
    """This function add the airports with height less than the given one to list"""
    list=[]
    for row in data:
        if(row[index_elevation_ft].isdigit()):
            if(int(row[index_elevation_ft]) < elevation):
                #controlo que no lo haya agregado anterirormente, dado que puede estar repetido dicho aeropuerto en el dataset.
                if not(row[index_name] in list):
                    list.append(row[index_name])
            else:
                continue
        else:
            continue
    return list