def jurisdicciones_situciacion_calle(header,data):
    """This function calculates the porcentage of the first 5 jurisdictions"""
    listJurisdiccion=[]

    indice_nombreJ=header.index("Jurisdiccion")
    indice_porcentaje=header.index("Porcentaje de la población en situacion de calle")

    for row in data:
        if row[indice_nombreJ]!="Total del pais":
            nombreJ=row[indice_nombreJ]
            if(row[indice_porcentaje].isdigit()):
                porcentaje=float(row[indice_porcentaje])*100
                listJurisdiccion.append((nombreJ,porcentaje))
                
    #Ordeno la lista de mayor a menor pero por porcentaje
    listJurisdiccion.sort(key=lambda x:x[1],reverse=True)
    #Solo me quedo con los primeros 5
    listaJ=listJurisdiccion[:5]
    return listaJ

def mostrar_tipos_conectividades(header):
    """This function shows the different types of connectivities"""
    listaTipos=[]
    index_inicio=header.index("ADSL")
    index_final=header.index("4G")
    for col in header[index_inicio:index_final+1]:
        listaTipos.append(col)
    return listaTipos

def obtener_jurisdiccion(header,data):
    """This function calculates the maximum gap between men and women in your jurisdiction"""
    #Busco la posicion de cada encabezado que necesito
    index_jurisdiccion=header.index("Jurisdiccion")
    index_total_varones=header.index("Varones Total de poblacion")
    index_total_mujeres=header.index("Mujeres Total de poblacion")

    #Recorro el data_Set para calcular la brecha maxima y la jurisdiccion
    max_brecha=0
    max_jurisdiccion=None
    for row in data:
        nombre_jurisdiccion=row[index_jurisdiccion].strip()
        if nombre_jurisdiccion != "Total del pais":
            cantidad_brecha=abs(int(row[index_total_varones])-int(row[index_total_mujeres]))

            if cantidad_brecha>max_brecha:
                max_jurisdiccion=nombre_jurisdiccion
                max_brecha=cantidad_brecha
        else:
            continue
    return max_jurisdiccion,max_brecha