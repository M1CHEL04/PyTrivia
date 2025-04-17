def generate_column_Elevation_name (header, data):
    """This function receives the header and data. And generates a column with a quantitative value"""
    header.append("elevation_name")
    index_elevation_ft=header.index('elevation_ft')
    for row in data:
        if(row[index_elevation_ft].isdigit()):
            match int(row[index_elevation_ft]):
                case elevation if elevation <=103:
                    row.append("bajo")
                case elevation if (elevation > 103 and elevation <= 903):
                    row.append("medio")
                case elevation if (elevation > 903):
                    row.append("alto")
        else:
            row.append("-")
    return header, data


def generate_column_prov_name (header_airport,data_airport,header_ar,data_ar):
    """This funcion add a column in the file with province where the airport is located"""
    header_airport.append("prov_name")
    index_airport_city=header_airport.index('municipality')
    for row in data_airport:
        row.append(search_prov(row[index_airport_city],header_ar,data_ar))
    return header_airport,data_airport

def search_prov (city,header_ar,data_ar):
    """This function returs the province wherte the city passed by parameter is located"""
    index_ar_city= header_ar.index('city')
    index_ar_prov= header_ar.index('admin_name')
    for row in data_ar:
        if row[index_ar_city].lower() == city.lower():
            return row[index_ar_prov]
    return("prov_not_found")

def replace_province (df):
    """This function receives the airport data frame and removes the words "Province" and "Autunomus City" """
    
    df_copy= df.copy()

    df_copy.region_name = df_copy.region_name.str.replace('Province','')
    df_copy.region_name = df_copy.region_name.str.replace('(Autonomous City)','')

    return df_copy