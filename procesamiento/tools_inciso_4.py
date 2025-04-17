
def replace_value(data, old_value, new_value ):
    """
        This function has three parameters
            data: list of list
            old_value: list of values to replace
            new_value: value by which it will be replaced
        In each row, it replaces the old values for the new value.
    """
    for row in range(len(data)):
        for elem in range(len(data[row])):
            if data[row][elem] in old_value:
                data[row][elem] = new_value

def generate_column_homeless_percentage(header, data):
    """
        This function receives the dataset separated by header and data.
        Then generates a new column with the total homeless percentage and adds
        to each row the percentage indicated.
    """
    header.append("Porcentaje de la población en situacion de calle")

    total_population_index = header.index('Total de poblacion')
    total_homeless_index = header.index('Poblacion en situacion de calle(²)')
    
    for row in data:
        percentage =(int(row[total_homeless_index]) / int(row[total_population_index])) * 100
        # redondea con 3 numeros despues de la coma 
        percentage = str(round(percentage, 3))
        if row[total_homeless_index] != '0': 
            row.append(percentage)
        else:
            row.append('missing data')
        


def replace_missing_data (df):
    """ 
    This function receives a dataset and replaces "missing data" with an none value
    """

    df_copy= df.copy()

    df_copy['Porcentaje de la población en situacion de calle'] = df_copy['Porcentaje de la población en situacion de calle'].replace('missing data', None)


    return df_copy