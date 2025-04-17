def reemplazar_caracter(data):
    """This function replaces '--' for 'NO'"""
    for row in data:
        for cell in range(len(row)):
            if(row[cell]=='--'):
                row[cell]='NO'
    return data

def generar_columna(header,data):
    """This function generates a column and modifies it"""
    header.append("posee_conectividad")
    index_inicio=header.index("ADSL")
    index_final=header.index("4G")
    indices=[]
    for col in header[index_inicio:index_final+1]:
        index=header.index(col)
        indices.append(index)

    #Itero sobre cada fila para modificar el valor de 'posee conectividad'
    for row in data:
        todas_son_NO=True
        #Verifico cada indice
        for cell in indices:
            if row[cell] != 'NO' :
               todas_son_NO=False
               break
        if todas_son_NO:
            row.append("NO")
        else:
            row.append("SI")
    return header,data
    