from pathlib import Path
import pandas as pd # type: ignore
import random

def process_thematic(thematic):
    """This function will process the theme chosen by the user. Which will invoke another function to generate questions about said topic."""
    match thematic:
        case thematic if thematic == "lagos":
            question,answer,options = generate_questions_lakes()
        case thematic if thematic == "aeropuertos":
            question,answer,options = generate_questions_air()
        case thematic if thematic == "conectividad":
            question,answer,options = generate_questions_conec()
        case thematic if thematic == "censo":
            question,answer,options = generate_questions_census()
    
    return question,answer,options


def choose_attributes_lakes(df_lakes):
    """This function is used internally in generate_question_lakes. Returns a list with the value of the chosen attributes, from a random row of the dataset."""
    #Lista de los nombres de las columnas que van a ser los atributos.
    attributes = ['Nombre', 'Ubicacion', 'Superficie (km²)', 'Sup Tamaño']

    random_row = df_lakes.sample(n=1)

    selected_attributes = [random_row.iloc[0][attr] for attr in attributes]

    return selected_attributes


def generate_questions_lakes():
    """This function generates the questions about the lake dataset. returns the question, the correct option and a list with incorrect options for the easy difficulty."""
    file_path = Path('..')/"Datasets_Modificados"/"lagos_arg_MODIF.csv"

    df_lakes = pd.read_csv(file_path)

    attributes = choose_attributes_lakes(df_lakes)

    case = random.randint(0,3)

    match case:
        case 0:
            question = f"""
                   - Ubicacion: {attributes[1]}
                   - Superficie (km²): {str(attributes[2])}
                   - Superficie Tamaño: {str(attributes[3])}
                   - Nombre: ??
                   """ 
            correct_answer = attributes[0]
            column = 'Nombre'
        case 1:
            question = f"""
                   - Nombre: {attributes[0]}
                   - Superficie (km²): {str(attributes[2])}
                   - Superficie Tamaño: {str(attributes[3])}
                   - Ubicacion: ??
                   """ 
            correct_answer = attributes[1]
            column = 'Ubicacion'
        case 2:
            question = f"""
                   - Nombre: {attributes[0]}
                   - Ubicacion: {attributes[1]}
                   - Superficie Tamaño: {str(attributes[3])}
                   - Superficie (km²): ??
                   """ 
            correct_answer = str(attributes[2])
            column = 'Superficie (km²)'
        case 3:
            question = f"""
                   - Nombre: {attributes[0]}
                   - Ubicacion: {attributes[1]}
                   - Superficie (km²): {str(attributes[2])}
                   - Superficie Tamaño: ??
                   """ 
            correct_answer = str(attributes[3])
            column = 'Sup Tamaño'
    
     # Obtener todas las opciones posibles en la columna seleccionada
    all_options = df_lakes[column].unique()
    
    # Filtrar opciones diferentes a la respuesta correcta
    incorrect_options = [option for option in all_options if option != correct_answer]
    
    # Elegir aleatoriamente dos opciones incorrectas únicas
    incorrect_options = random.sample(incorrect_options, k=min(2, len(incorrect_options)))

    options = incorrect_options + [correct_answer]
    random.shuffle(options)
    
    return question, correct_answer, options


def choose_attributes_air(df_air):
    """This function is used internally in generate_questions_air. Returns a list with the value of the chosen attributes, from a random row of the dataset."""
    
    attributes = ['type', 'name', 'elevation_name', 'region_name']

    random_row = df_air.sample(n=1)

    selected_attributes = [random_row.iloc[0][attr] for attr in attributes]

    return selected_attributes


def generate_questions_air():
    """This function generates the questions about the airport dataset. returns the question, the correct option and a list with incorrect options for the easy difficulty."""

    file_path = Path('..')/"Datasets_Modificados"/"ar-airports_modificado.csv"

    df_air = pd.read_csv(file_path)

    attributes = choose_attributes_air(df_air)

    case = random.randint(0,3)

    match case:
        case 0:
            question = f"""
                   - Nombre: {attributes[1]}
                   - Elevacion: {str(attributes[2])}
                   - Provincia: {attributes[3]}
                   - Tipo: ??
                   """
            correct_answer = attributes[0]
            column = 'type'
        case 1:
            question = f"""
                   - Provincia: {attributes[3]}
                   - Elevacion: {str(attributes[2])}
                   - Tipo: {attributes[0]}
                   - Nombre: ??
                   """ 
            correct_answer = attributes[1]
            column = 'name'
        case 2:
            question = f"""
                   - Nombre: {attributes[1]}
                   - Provincia: {attributes[3]}
                   - Tipo: {attributes[0]}
                   - Elevacion: ??
                   """
            correct_answer = str(attributes[2])
            column = 'elevation_name'
        case 3:
            question = f"""
                   - Nombre: {attributes[1]}
                   - Elevacion: {str(attributes[2])}
                   - Tipo: {attributes[0]}
                   - Provincia: ??
                   """
            correct_answer = attributes[3]
            column = 'region_name'
    
     # Obtener todas las opciones posibles en la columna seleccionada
    all_options = df_air[column].unique()
    
    # Filtrar opciones diferentes a la respuesta correcta
    incorrect_options = [option for option in all_options if option != correct_answer]
    
    # Elegir aleatoriamente dos opciones incorrectas únicas
    incorrect_options = random.sample(incorrect_options, k=min(2, len(incorrect_options)))

    options = incorrect_options + [correct_answer]
    random.shuffle(options)
    
    return question, correct_answer, options


def choose_attributes_conec(df_conec):
    """This function is used internally in generate_questions_conec. Returns a list with the value of the chosen attributes, from a random row of the dataset."""

    attributes = ['Provincia', 'Localidad','Poblacion', 'posee_conectividad']

    random_row = df_conec.sample(n=1)

    selected_attributes = [random_row.iloc[0][attr] for attr in attributes]

    return selected_attributes


def generate_questions_conec():
    """This function generates the questions about the connectivity dataset. returns the question, the correct option and a list with incorrect options for the easy difficulty."""

    file_path = Path('..') / "Datasets_Modificados" / "Conectividad_Internet_modificado.csv"

    df_conec = pd.read_csv(file_path)

    attributes = choose_attributes_conec(df_conec)

    case = random.randint(0, 3)

    match case:
        case 0:
            question = f"""
                   - Poblacion: {str(attributes[2])}
                   - Localidad: {attributes[1]}
                   - Posee Conectividad: {attributes[3]} 
                   - Provincia: ??
                   """
            correct_answer = attributes[0]
            column = 'Provincia'
        case 1:
            question = f"""
                   - Provincia: {attributes[0]}
                   - Poblacion: {str(attributes[2])}
                   - Posee Conectividad: {attributes[3]} 
                   - Localidad: ??
                   """
            correct_answer = attributes[1]
            column = 'Localidad'
        case 2:
            question = f"""
                    - Provincia: {attributes[0]}
                    - Localidad: {attributes[1]}
                    - Posee Conectividad: {attributes[3]} 
                    - Poblacion: ??
                    """
            correct_answer = (str(attributes[2]))
            column = 'Poblacion'
        case 3:
            question = f"""
                    - Provincia: {attributes[0]}
                    - Localidad: {attributes[1]}
                    - Poblacion: {str(attributes[2])}
                    - Posee Conectividad: ??
                    """
            correct_answer = attributes[3]
            column = 'posee_conectividad'

    # Obtener todas las opciones posibles en la columna seleccionada
    all_options = df_conec[column].unique()
    
    # Filtrar opciones diferentes a la respuesta correcta
    incorrect_options = [option for option in all_options if option != correct_answer]
    
    # Elegir aleatoriamente dos opciones incorrectas únicas
    incorrect_options = random.sample(incorrect_options, k=min(2, len(incorrect_options)))

    options = incorrect_options + [correct_answer]
    random.shuffle(options)
    
    return question, correct_answer, options

def choose_attributes_census(df_census):
    """This function is used internally in generate_questions_census. Returns a list with the value of the chosen attributes, from a random row of the dataset."""

    attributes = ['Jurisdiccion', 'Total de poblacion', 'Poblacion en situacion de calle(²)', 'Porcentaje de la población en situacion de calle']
    
    random_row = df_census.sample(n=1)

    selected_attributes = [random_row.iloc[0][attr] for attr in attributes]

    return selected_attributes


def generate_questions_census():
    """This function generates the questions about the census dataset. returns the question, the correct option and a list with incorrect options for the easy difficulty."""

    file_path = Path('..') / "Datasets_Modificados" / "c2022_tp_c_resumen_adaptadoMODIF.csv"

    df_census = pd.read_csv(file_path)

    df_census = df_census.dropna(subset=['Jurisdiccion', 'Total de poblacion', 'Poblacion en situacion de calle(²)', 'Porcentaje de la población en situacion de calle']) # saca las filas con valores nulos en las columnas seleccionadas

    attributes = choose_attributes_census(df_census)

    case = random.randint(0, 3)

    match case:
        case 0:
            question = f"""
                    - Total Poblacion: {str(attributes[1])}
                    - Porcentaje de la población en situacion de calle: {str(round(attributes[3], 3))}
                    - Poblacion en situacion de calle: {str(attributes[2])}
                    - Jurisdiccion: ??
                    """
            correct_answer = attributes[0]
            column = 'Jurisdiccion'
        case 1:
            question = f"""
                    - Jurisdiccion: {attributes[0]}
                    - Porcentaje de la población en situacion de calle: {str(round(attributes[3], 3))}
                    - Poblacion en situacion de calle: {str(attributes[2])}
                    - Total Poblacion: ??
                    """
            correct_answer = str(attributes[1])
            column = 'Total de poblacion'
        case 2:
            question = f"""
                    - Jurisdiccion: {attributes[0]}
                    - Total Poblacion: {str(attributes[1])}
                    - Poblacion en situacion de calle: {str(attributes[2])}
                    - Porcentaje de la población en situacion de calle: ??
                    """
            correct_answer = str(round(attributes[3], 3))
            column = 'Porcentaje de la población en situacion de calle'
        case 3:
            question = f"""
                    - Jurisdiccion: {attributes[0]}
                    - Total Poblacion: {str(attributes[1])}
                    - Porcentaje de la población en situacion de calle: {str(round(attributes[3], 3))}
                    - Poblacion en situacion de calle: ??
                    """
            correct_answer = str(attributes[2])
            column = 'Poblacion en situacion de calle(²)'

     # Obtener todas las opciones posibles en la columna seleccionada
    all_options = df_census[column].unique()
    
    # Filtrar opciones diferentes a la respuesta correcta
    incorrect_options = [option for option in all_options if option != correct_answer]
    
    # Elegir aleatoriamente dos opciones incorrectas únicas
    incorrect_options = random.sample(incorrect_options, k=min(2, len(incorrect_options)))

    options = incorrect_options + [correct_answer]
    random.shuffle(options)

    return question, correct_answer, options


def generate_clue(answer):
    """This function returns the track for the medium difficulty. Where a random letter is shown for the length of the answer and is completed with '-'"""

    letters = list(str(answer))  # Convertir la respuesta en una lista de caracteres
    non_space_indices = [i for i, char in enumerate(letters) if char != ' ']  # Indices de letras que no son espacios
    
    # Seleccionar una letra aleatoria
    if non_space_indices:  # Verificar que hay letras para seleccionar
        random_index = random.choice(non_space_indices)
        selected_letter = letters[random_index]

        # Crear la cadena de pistas con la letra seleccionada en las posiciones correctas
        line = ''.join(char if char == selected_letter else '-' if char != ' ' else ' ' for char in letters)
    return line