
import streamlit as st
from Functions import tools_graficos_datasets as tool
from streamlit_folium import st_folium
from Functions import tools_generales

tools_generales.reset_game()

#Configuro la pagina de Conociendo nuestros datos
st.set_page_config(
    page_title="Datos",
    page_icon="📚",
    layout="wide",
)

st.write('# Conociendo nuestros datos 🔍')
st.write('> ####  Antes de comenzar a jugar, te recomendamos ver los siguentes graficos a modo de resumen de la informacion de aeropuertos y lagos de Argentina. ####')
st.write('\n')

#Grafico 1
st.write('## Mapa de aeropuertos Argentinos ##')
st.write('\n')
st.markdown('* __Elevación baja:__ <font color="blue">Azul</font>', unsafe_allow_html=True)
st.markdown('* __Elevación media:__ <font color="green">Verde</font>', unsafe_allow_html=True)
st.markdown('* __Elevación alta:__ <font color="red">Rojo</font>', unsafe_allow_html=True)
fig=tool.create_airports_map()
st_folium(fig,width=800)

#Grafico 2
fig2=tool.create_airpots_bar_graph()
st.plotly_chart(fig2)

#Grafico 3
st.write('## Porcentaje de aeropuertos segun su criterio de elevacion ##')
st.write("#### <u>Criterios de los nombres de elevacion:</u> ####",unsafe_allow_html=True)
    
st.write('* Bajo: elevación menor o igual a 31,4 metros. ')
st.write('* Medio: elevación mayor a 31.4 metros y menor o igual a  275,2 metros. ')
st.write('* Alto: elevacion mayor a 275,2 metros. ')

fig3=tool.create_elevation_pie()
st.plotly_chart(fig3)

#Grafico 4
st.write('## Mapa de los lagos de argentina ##')
st.write('\n')
st.markdown('* __Tamaño chico:__ <font color="blue">Azul</font>', unsafe_allow_html=True)
st.markdown('* __Tamaño medio:__ <font color="green">Verde</font>', unsafe_allow_html=True)
st.markdown('* __Tamaño grande:__ <font color="red">Rojo</font>', unsafe_allow_html=True)
fig4=tool.create_lakes_map()
st_folium(fig4,width=800)

#Grafico 5
st.write('## Porcentaje de lagos segun su criterio de tamaño ##')
st.write("#### <u>Criterios de los nombres de elevación:</u> ####",unsafe_allow_html=True)

st.write('* Chico: superficie menor o igual a 17 km²')
st.write('* Medio: superficie mayor a 17 km² y menor o igual a 59 km²')
st.write('* Grande: superfice mayor a 59 km²')

fig5=tool.create_lakes_size_pie()
st.plotly_chart(fig5)

#Grafico 6
provinces=tool.lakes_province()

st.write('# Cantidad de lagos por provincia #')
st.write('#### Selecciona las provincias que desea incluir en el grafico #### ')
provinces_selected=st.multiselect("Provincias:",options=provinces,default=provinces)

fig6=tool.create_lakes_by_province_ghraph(provinces_selected)
st.plotly_chart(fig6)
