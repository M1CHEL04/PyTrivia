import streamlit as st 
from Functions import tools_stats_1 as tool
import datetime
from Functions import tools_generales

tools_generales.reset_game()

#Configuro la pagina de estadisticas
st.set_page_config(
    page_title="Estadisticas",
    page_icon="📊",
    layout="wide",
)

st.write('# Estadisticas 📉')
st.write('* #### En esta pestaña se podran ver diferentes estadisticas. Algunas sobre el desempeño de los jugadores y la informacion de los jugadores')


#Inciso 1
st.write ('## Porcentaje de los genero que han jugado al menos una partida ##')
try:
    st.plotly_chart(tool.pie_gender_graph())
except (AttributeError,KeyError):
    st.error('### No hay suficiente información para realizar el grafico ###')

#Inciso 2
st.write('## Porcentaje de partidas con puntuacion mayor o menor al promedio actual ##')
try:
    average,fig2= tool.games_higher_average()
    st.write(f"* ##### El promedio actual de puntos por partida es de {average} puntos. ")
    st.plotly_chart(fig2)
except (AttributeError,KeyError):
    st.error('### No hay suficiente información para realizar el grafico ###')

#Inciso 3
st.write('## Cantidad de partidas jugadas por cada dia de la semana ##')
try:
    st.plotly_chart(tool.games_per_day())
except (AttributeError,KeyError):
    st.error('### No hay suficiente información para realizar el grafico ###')

#Inciso 4
st.write ('## Promedio de preguntas acertadas en un rango de dos fechas')
st.write('* ##### A continuacion ingrese las dos fechas solicitadas')
today= datetime.datetime.today()
min_year= datetime.date(today.year-120,1,1)

with st.form("Formulario inciso 4"):
    lower= st.date_input('fecha menor:',value=None,max_value=today,min_value=min_year)
    if lower:
        lower= lower.strftime("%Y-%m-%d")
    
    higher= st.date_input('fecha mayor:',value=None,max_value=today,min_value=min_year)
    if higher:
        higher= higher.strftime("%Y-%m-%d")
    
    submit= st.form_submit_button('Submit')

    if submit:
        if lower == None or higher == None:
            st.error('🚨 Todos los campos son obligatorios')
        else:
            try:
                st.plotly_chart(tool.average_correct_questions(lower,higher))
            except (AttributeError,KeyError):
                st.error('### No hay suficiente información para realizar el grafico ###')

#Inciso 5
st.write ('## Top 10 usuarios con mayor puntuación entre dos fechas')
st.write('* ##### A continuación ingrese las dos fechas solicitadas')
with st.form("Formulario inciso 5"):
    lower= st.date_input('fecha menor:',value=None,max_value=today,min_value=min_year)
    if lower:
        lower= lower.strftime("%Y-%m-%d")
    
    higher= st.date_input('fecha mayor:',value=None,max_value=today,min_value=min_year)
    if higher:
        higher= higher.strftime("%Y-%m-%d")
    
    submit= st.form_submit_button('Submit')

    if submit:
        if lower == None or higher == None:
            st.error('🚨 Todos los campos son obligatorios')
        else:
            try:
                df=tool.top_ten_scorer(lower,higher)
                st.markdown(df.style.hide(axis="index").to_html(), unsafe_allow_html=True)
            except (AttributeError,KeyError):
                st.error('### No hay suficiente información para realizar el grafico ###')

#Inciso 6
st.write('## Top temáticas mas dificiles')
st.write('* Este criterio se basa en que temática tuvo menos respuestas correctas')
try:
    df=tool.most_difficult_topic_ranking()
    st.markdown(df.style.hide(axis="index").to_html(), unsafe_allow_html=True)
except (AttributeError,KeyError):
    st.error('### No hay suficiente información para realizar el grafico ###')

#Inciso 7
st.write('## Comparacion del puntaje de dos usuarios a traves del tiempo ##')
st.write('* A continuación elija los usuarios que se desean comparar')

with st.form('Formulario inciso 7'):
    
    user1=tool.select_user(1)
    user2=tool.select_user(2)

    submit = st.form_submit_button('Submit')

    if(submit):
        if user1 == None or user2 == None:
            st.error('🚨 Todos los campos son obligatorios')
        else:
            try:
                st.plotly_chart(tool.user_coparation_graph(user1,user2))
            except (AttributeError,KeyError):
                st.error('### No hay suficiente información para realizar el grafico ###')

#Inciso 8
st.write('## Tematica con mayor conocimiento por genero ##')
st.write('* Para mostrar estos datos nos basamos en cual tematica tiene mayor cantidad de respuestas correctas por cada genero')
try:
    df=tool.gender_most_knowleadge_topic()
    st.markdown(df.style.hide(axis="index").to_html(), unsafe_allow_html=True)
except (AttributeError,KeyError):
    st.error('### No hay suficiente información para realizar el grafico ###')

#Inciso 9
st.write('## Estadisticas de cada dificultad ##')
st.write('##### A continuacion se mostrara el puntaje promedio para cada una y la cantidad de veces que se eligio')
try:
    df=tool.difficult_stats()
    st.markdown(df.style.hide(axis="index").to_html(), unsafe_allow_html=True)
except (AttributeError,KeyError):
    st.error('### No hay suficiente información para realizar el grafico ###')

#Inciso 10
st.write('## En racha ##')
st.write('##### A continuación se mostrara una lista de usuarios con al menos un punto en los ultimos 7 dias')
try:
    df=tool.users_in_row()
    st.markdown(df.style.hide(axis="index").to_html(), unsafe_allow_html=True)
except(AttributeError,KeyError):
    st.error('### No hay suficiente información para realizar el grafico ###')