import pandas as pd
from pathlib import Path
from plotly import graph_objects as go
import folium
from folium.plugins import MarkerCluster

def get_airports_data():
    """This funcion returns a dataframe of airports dataset"""
    file_route=Path('..')/'Datasets_Modificados'/'ar-airports_modificado.csv'
    return pd.read_csv(file_route)

def get_lakes_data():
    """This function returns a dataframe of lakes dataset"""
    file_route=Path('..')/'Datasets_Modificados'/'lagos_arg_MODIF.csv'
    return pd.read_csv(file_route)

def get_airports_colurs(elevation_name):
    """This function returns the colour according to the elevation name"""
    match elevation_name:
        case 'bajo':
            return 'blue'
        case 'medio':
            return 'green'
        case 'alto':
            return 'red'

def create_airports_map ():
    """This function create a map with the Argentinian airports"""

    #Seteo los atributos para ver los limites geograficos de argentina
    attr= ('&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> '
            'contributors, &copy; <a href="https://cartodb.com/attributions">CartoDB</a>'
            )
    tiles= 'https://wms.ign.gob.ar/geoserver/gwc/service/tms/1.0.0/capabaseargenmap@EPSG%3A3857@png/{z}/{x}/{-y}.png'

    #me quedo con el dataFrame de aeropuertos
    df=get_airports_data()

    #Creo la base del mapa
    Map=folium.Map(
        location=(df.latitude_deg.mean(),df.longitude_deg.mean()),
        control_scale=True,
        zoom_start=4,
        name='es',
        tiles=tiles,
        attr=attr
    )

    #Utilizo un marker cluster para agrupar todos los aeropuertos
    marker_cluster=MarkerCluster().add_to(Map)

    #Agrego todos los aeropuertos al mapa
    for index, row in df.iterrows():
        folium.Marker([row['latitude_deg'], row['longitude_deg']],
                      popup=row['name'],
                      icon=folium.Icon(color=get_airports_colurs(row['elevation_name']))
                      ).add_to(marker_cluster)
    return Map

def create_airpots_bar_graph ():
    """This function creat a bar graph with the number of airports type"""
    df= get_airports_data()

    #cuento todos los tipos de aeropuertos
    types_count= df.type.value_counts()

    fig=go.Figure(data=[go.Bar(x=types_count.index,y=types_count.values)])
    fig.update_layout(title={'text':'Cantidad de los diferentes tipos de aeropuertos','font':{'size':34}},xaxis_title='Tipos de aeropuertos',yaxis_title='Cantidad',width=800,height=600)

    return fig

def clean_labels(label):
    """This is a private function. Its function is clean the labels of the processed series"""
    if(label == '-'):
        return "Información desconocida"
    else:
        return label

def create_elevation_pie():
    """This function create a pie chart with de percentages of the airport height ranges"""

    df=get_airports_data()
    df.elevation_name=df.elevation_name.apply(clean_labels)

    elevation_series=df.elevation_name.value_counts()

    #creo una lista con los colores que quiero que se imprima el grafico
    colours=['#f49097','#dfb2f4','#f5e960',"#55d6c2"]

    #creo el grafico
    fig=go.Figure(data=[go.Pie(labels=elevation_series.index,values=elevation_series.values,marker=dict(colors=colours))])
    fig.update_layout(width=600,height=600)

    return fig

def get_colour_lake (size):
    """This function returns the colour according to surface size"""
    match size:
        case 'chico':
            return 'blue'
        case 'medio':
            return 'green'
        case 'grande':
            return 'red'

def create_lakes_map ():
    """This function create a map with the Argentinian lakes"""
    attr= ('&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> '
            'contributors, &copy; <a href="https://cartodb.com/attributions">CartoDB</a>'
            )
    tiles= 'https://wms.ign.gob.ar/geoserver/gwc/service/tms/1.0.0/capabaseargenmap@EPSG%3A3857@png/{z}/{x}/{-y}.png'
    
    df=get_lakes_data()

    Map=folium.Map(
        location=(-45.5, -60.346857),
        control_scale=True,
        zoom_start=5,
        name='es',
        tiles=tiles,
        attr=attr
    )

    for index, row in df.iterrows():
        folium.Marker([row['latitud'], row['longitud']],
                      popup=row['Nombre'],
                      icon=folium.Icon(color=get_colour_lake(row['Sup Tamaño']))
                      ).add_to(Map)
    return Map


def create_lakes_size_pie():
    """This function create a pie graph with the percentaje of the lakes sizes"""
    #leo el archivo
    df=get_lakes_data()
    #extraigo la informacion de las superficies de los lagos y me quedo con un serie
    lake_sizes=df['Sup Tamaño'].value_counts()

    #creo la paleta de colores con la que quiero que se imprima mi grafico
    colours=['#f696af','#aa77c3','5d58d7']

    #creo el grafico
    fig=go.Figure(data=[go.Pie(labels=lake_sizes.index,values=lake_sizes.values,marker=dict(colors=colours))])
    fig.update_layout(width=600,height=600)

    return fig

def lakes_province ():
    """This function return a list with the provinces that have a lake in them"""
    df=get_lakes_data()

    province_list=df.Ubicacion.unique().tolist()

    return province_list

def create_lakes_by_province_ghraph (provinces=None):
    """This function create a bar graph with the number of lakes per province"""
    #leo el archivo
    df=get_lakes_data()

    #Veo la condicion si tengo mostrar los datos completos o solo de una provincia
    if(provinces):
        #Encontre una provincia
        filtered_df=df[df['Ubicacion'].isin(provinces)]
    else:
        filtered_df=df

    #extraigo los datos necesarios
    lakes_by_province=filtered_df.Ubicacion.value_counts()

    #creo el grafico de barras
    fig=go.Figure(data=[go.Bar(x=lakes_by_province.index,y=lakes_by_province.values)])
    fig.update_layout(xaxis_title='Provincia',yaxis_title='Cantidad de lagos',width=800,height=600)
    
    return fig