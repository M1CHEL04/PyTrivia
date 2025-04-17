def sup_size(header, data):
    """ This function receives a header and the data, and adds a column in which the data
      is classified according to its area in km2"""

    index_surface = header.index("Superficie (km²)")

    for row in data:
        # Obtengo y convierto a int el valor de la superficie.
        index_sup_size = header.index("Sup Tamaño")
        sup_km2 = int((row[index_surface]))
        size = ""

        match sup_km2:
            case sup_km2 if sup_km2 <= 17:
                size = "chico"
            case sup_km2 if 17 < sup_km2 <= 59:
                size = "medio"
            case sup_km2 if sup_km2 > 59:
                size = "grande"
        
        row[index_sup_size] = size
    return data

def gms_to_decimal(coord):
    """ This function converts the values of a gms coordinate to a decimal value"""
    # Obtengo las partes de las coordenadas, para convertirla en decimal.
    parts = coord.split('°')
    degrees = float(parts[0])
    minutes = float(parts[1].split('\'')[0])
    seconds = float(parts[1].split('\'')[1].split('\"')[0])
    direction = parts[1].split('\"')[1].strip()

    value_decimal = degrees + minutes / 60 + seconds / 3600

    ## Si la direccion de la coordenada es "S" o "W", multiplico por -1, para covertir el valor a negativo.
    if direction == 'S' or direction == 'O':
        value_decimal *= -1
    
    return value_decimal


def conv_gms_gd(lat_str,long_str):
    """ This function returns two decimal values"""
    latitude = gms_to_decimal(lat_str)
    longitude = gms_to_decimal(long_str)
    return latitude, longitude


def mod_coordinates(header, data):
    """ This function converts the values of a coordinate from gms to gd and
      adds the values in their respective columns."""

    index_coordinates = header.index("Coordenadas")

    for row in data:
        coord = str(row[index_coordinates])
        coord_parts = coord.split(" ")
        # Obtengo el valor resultante para la latitud
        lat_str = coord_parts[0]
        # Obtengo el valor resultante para la longitud
        long_str = coord_parts[1]

        coords_mod = conv_gms_gd(lat_str,long_str)

        #Me guardo los valores que retornaron modificados, al aplicar la funcion "conv_gms_gd"
        latitude = coords_mod[0]
        longitude = coords_mod[1]

        # Agrego los valores a las columnas correspondientes.
        row[header.index("latitud")] = latitude
        row[header.index("longitud")] = longitude

    return data
