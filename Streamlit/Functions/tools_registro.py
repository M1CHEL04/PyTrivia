#En este archivo .py se realizan todas las funciones necesarias para el correcto funcionamiento la pagina de registro

def update_data(data_json,dict_update,index):
    """This function update an specific dictionary indicated in the parameters"""
    data_json[index]=dict_update
    return data_json
    
def add_data(data_json,dict_add):
    """This function add the dictionary at the end of the json file"""
    data_json.append(dict_add)
    return data_json

def search_email(data_json,input_data):
    """
    This function receives the data enetered by the user and looks if the enetered email had been
    previously registered. If the email is found returns the index of the dictionary that contains 
    this email. Else return -1.  
    """
    for index, dictionary in enumerate(data_json):
        if dictionary["mail"] == input_data["mail"]:
            #Si el mail de algun diccionario es igual al que estoy buscando, retorno el indice de la lista.
            return index
    #Si no encuentro ningun mail que coincida, retorno -1.
    return -1