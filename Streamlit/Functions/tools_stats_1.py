import pandas as pd
from plotly import graph_objects as go
from pathlib import Path
from datetime import datetime, timedelta
import streamlit as st
import re

def get_games_data ():
    """This function returns a data frame with the information in the games json file"""
    file_route= Path('..')/'Streamlit'/'Data_base'/'Game_record.json'
    return pd.read_json(file_route, orient='records')


def get_users_data ():
    """This function returns a data frame with the information in the users json file"""
    file_route= Path('..')/'Streamlit'/'Data_base'/'Users_records.json'
    return pd.read_json(file_route,orient='records')


#Funcionalidades inciso 1
def pie_gender_graph():
    """This function return a pie graph that shows the percentage of games played by gender """
    df=get_games_data()

    #Me quedo con los usuarios unicos
    df_filtered= df.drop_duplicates(subset='mail')

    #Me quedo con una serie con el genero y la cantidad de partidas por genero
    data_graph=df_filtered.genero.value_counts()
    
    #Paleta de coleres para el grafico
    colours=['#2ECC71','#2E4053','#DC7633']

    #Creo el grafico
    fig= go.Figure(data=[go.Pie(labels=data_graph.index,values=data_graph.values,marker=dict(colors=colours))])
    fig.update_layout(width=600,height=600)
    
    return fig


#Funcionalidades inciso 2
def games_higher_average ():
    """This function returns a pie graph that shows the percentage of games with points below and above the average """
    df= get_games_data()

    #Me quedo con el promedio de los puntos
    average= df.puntos.mean()
    average= round(average,2)

    #Creo una nueva categoria dentro del dataframe
    df['categoria']=df.puntos.apply(lambda x: 'Mayor que el promedio' if x> average else 'Menor que el promedio')

    #Me quedo con los datos a graficar
    quantity_per_category= df['categoria'].value_counts()

    #Paleta de colores para el grafico
    colurs=['#8E44AD ','#E74C3C']

    #Creo el grafico
    fig=go.Figure(data=[go.Pie(labels=quantity_per_category.index,values=quantity_per_category.values,marker=dict(colors=colurs))])
    fig.update_layout(width=600,height=600)

    return average, fig


#Funcionalidades inciso 3
def get_day_name (day_str):
    """This function recive a date and retur the name of the day"""
    weeks_day={0: 'Lunes',
               1: 'Martes',
               2: 'Miercoles',
               3: 'Jueves',
               4: 'Viernes',
               5: 'Sabado',
               6: 'Domingo'}
    
    day_dt=datetime.strptime(day_str,"%Y-%m-%d")

    return weeks_day[day_dt.weekday()]


def games_per_day ():
    """This function returns a bar graph that shows the number of games per day"""
    
    #Extraigo los datos del archivo 
    df= get_games_data()
    
    #Creo una lista con los dias
    days= ['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']

    #Se crea una nueva columna en el data frame con el nombre del dia en cada partida
    df['Dia']=df['fecha_de_juego'].apply(get_day_name)
    
    #Me quedo con los datos para graficar
    graph_values= df.Dia.value_counts()
    graph_values=graph_values.reindex(days,fill_value=0)

    #Creo el grafio
    fig= go.Figure(data=[go.Bar(x=graph_values.index,y=graph_values.values)])
    fig.update_layout(xaxis_title='Dias',yaxis_title='Cantidad de partidas jugadas',width=800,height=600)

    return fig


#Funcionalidades inciso 4
def get_month(month):
    match month:
        case 1:
            return 'Enero'
        case 2:
            return 'Febrero'
        case 3:
            return 'Marzo'
        case 4:
            return 'Abril'
        case 5:
            return 'Mayo'
        case 6:
            return 'Junio'
        case 7: 
            return 'Julio'
        case 8: 
            return 'Agosto'
        case 9:
            return 'Septiembre'
        case 10:
            return 'Octubre'
        case 11: 
            return 'Noviembre'
        case 12: 
            return 'Diciembre'

def average_correct_questions(lower,higher):
    """This function returns a bar graph showing the percentage of correct answers per month between two dates passed by parameter"""

    months=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']

    df=get_games_data()
    
    #convierto las fechas pasadas por parametro a un objeto datetime
    lower= pd.to_datetime(lower)
    higher= pd.to_datetime(higher)

    #convierto todas las fechas del dataset a un objeto datetime
    df['fecha_de_juego']=pd.to_datetime(df['fecha_de_juego'])

    df_filtered= df[df['fecha_de_juego'].between(lower,higher)]

    #Checkear antes de probar los nombres de los atributos
    
    #Creo una nueva columna con el nombre del mes
    df_filtered['mes']=df_filtered['fecha_de_juego'].dt.month
    
    df_filtered['mes']=df_filtered['mes'].apply(get_month)

    df_filtered['mes']= pd.Categorical(df_filtered['mes'],categories=months,ordered=True)

    monthly_summary=df_filtered.groupby('mes')['respuestas_correctas'].mean().reset_index()
    
    fig=go.Figure(data=[go.Bar(x=monthly_summary['mes'],y=monthly_summary['respuestas_correctas'])])
    fig.update_layout(xaxis_title='Mes',yaxis_title='Promedio de respuestas correctas por mes',width=800,height=600)
    
    return fig


#Funcionalidades inciso 5
def top_ten_scorer (lower,higher):
    """This function returns the top ten scorer in a range of two dates passed by parameter """

    df=get_games_data()

    lower = pd.to_datetime(lower)
    higher= pd.to_datetime(higher)
    df['fecha_de_juego']=pd.to_datetime(df['fecha_de_juego'])

    df_filtered=df[df['fecha_de_juego'].between(lower,higher)]

    df_filtered= df_filtered.sort_values(by='puntos',ascending=False)
    
    df_filtered['puntos']=df_filtered['puntos'].round(2)

    top_ten= df_filtered[['usuario', 'mail', 'fecha_de_juego', 'puntos']].head(10)

    #Retorno los 10 primeros lugares para luego graficarlos en una tabla de streamlit
    return top_ten


#Funcionalidades inciso 6
def most_difficult_topic_ranking ():
    """This function returns the most difficult topic bassed on more incorrect answers"""

    df=get_games_data()

    df_filtered= df.groupby(['tematica','dificultad']).agg({'respuestas_correctas':'sum'}).reset_index()

    df_sorted= df_filtered.sort_values(by='respuestas_correctas', ascending=True)

    #Cambio el nombre de las columnas
    df_sorted.columns=['Temática','Dificultad','Respuestas correctas']

    return df_sorted


#Funcionalidades inciso 7
def select_user(i):
    """This function return a user from de users data frame"""

    df= get_users_data()

    user= st.selectbox(f"**Usuario {i}:**",df['nombre_mail'].values, index = None, placeholder = 'Seleccionar')

    return user

def extract_user (user):
    """This function return the mail form the user"""

    patron= r'\(([^)]+)\)'

    res= re.search(patron,user)

    if res:
        return res.group(1)

def user_coparation_graph(user1,user2):
    """This function returns a line graph that compares 2 users games over time"""

    df=get_games_data()

    #Extraigo los mails de los usuarios seleccionados
    user1=extract_user(user1)
    user2=extract_user(user2)

    #Convierto todas las fechas a tipo de dato datetime
    df['fecha_de_juego']=pd.to_datetime(df['fecha_de_juego'])

    #Me quedo con las partidas de los usuarios seleccionados
    users=[user1,user2]
    df_filtered= df[df['mail'].isin(users)]

    #Ordeno los datos por fecha
    df_filtered=df_filtered.sort_values(by='fecha_de_juego')

    #Me quedo con la primer fecha relevante
    min_date= df_filtered['fecha_de_juego'].min()

    #Creo el grafico comparando los puntos de los usuarios
    fig= go.Figure()

    for user in users:
        user_data= df_filtered[df_filtered['mail']==user]
        fig.add_trace(go.Scatter(x=user_data['fecha_de_juego'], y=user_data['puntos'], mode='lines+markers',name=user))

    #Configuro el diseno del grafico
    fig.update_layout(
        title='Evolucion del puntaje de los usuarios a lo largo del tiempo',
        xaxis_title='Fecha',
        yaxis_title='Puntaje',
        legend_title='Usuario',
        template='plotly',
        xaxis=dict(range=[min_date,df['fecha_de_juego'].max()])
    )

    return fig

#Funcionalidades inciso 8
def gender_most_knowleadge_topic ():
    """This function returns the topics in which greater knowledge is demonstrated by gender"""

    df=get_games_data()

    #Agrupo los datos por genero y tematica y sumo las respuestas correctas dentro de cada grupo
    df_group= df.groupby(['genero','tematica']).agg({'respuestas_correctas':'sum'}).reset_index()

    #Devuelve los indices de las filas donde se encuetra el valor maximo de respuestas correctas y .loc() selecciona las filas con los indices retornados
    df_max_gender= df_group.loc[df_group.groupby('genero')['respuestas_correctas'].idxmax()]

    #Cambio el nombre de las columnas para que se imprima de una manera correcta
    df_max_gender.columns=['Genero','Temática','Respuestas corectas']

    return df_max_gender


#Funcionalidades inciso 9
def difficult_stats():
    """This function returns the average, and the times each difficulty was chosen"""  
    df=get_games_data()

    #Creo un nuevo data frame agrupado por dificultad y se le generan 2 columnas con el promedio de puntos y una con la cantidad de veces que se jugo la misma
    df_stats= df.groupby('dificultad').agg(puntaje_promedio=('puntos', 'mean'), veces_elegida=('puntos','size')).reset_index()

    #Redondeo a 2 decimales el valor del promedio
    df_stats['puntaje_promedio']= df_stats['puntaje_promedio'].round(2)

    #Cambio el nombre de las columnas para que se imprima bien
    df_stats.columns=['Dificultad', 'Puntaje promedio', 'Veces elegida']

    return df_stats


#Funcionalidades inciso 10
def users_in_row ():
    """This function return all the users who played a game and get at least 1 point in the last 7 days"""

    df=get_games_data()

    #Me quedo con las fechas en las que debo filtrar los datos y convierto a objetos datetime
    higher= datetime.today()
    higher=pd.to_datetime(higher)

    lower= higher - timedelta(days=6)
    lower= pd.to_datetime(lower)

    #Convierto todas las fechas del data frame a objetos datetime
    df['fecha_de_juego']=pd.to_datetime(df['fecha_de_juego'])

    #filtro los datos en un nuevo data frame
    df_filtered= df[df['fecha_de_juego'].between(lower,higher)]
    df_filtered= df_filtered[df_filtered['puntos']>0]

    #Me quedo con las columnas que quiero mostrar unicamente
    df_users= df_filtered[['usuario', 'mail', 'fecha_de_juego']]

    #Cambio los nombres de las columnas para una correcta visualizacion
    df_users.columns=['Usuario','Mail', 'Fecha de juego (yy/mm/dd)']

    return df_users