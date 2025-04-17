
import streamlit as st # type: ignore

#Para poder acceder correctamente a la ruta de los archivos es necesario usar la funcion Path de la libreria pathlib
from pathlib import Path

import datetime

#Para poder leer y escribir archivos desarrollamos funciones generales.
#Se dearrollaron funcion para la carga, busqueda y actualizacion de informacion dentro del archivo. 
from Functions import  tools_generales, tools_registro

tools_generales.reset_game()

#Configuro la pagina de Formulario de registro
st.set_page_config(
    page_title="Registro",
    page_icon="📝",
    layout="wide",
)

json_path = Path('..')/"Streamlit"/"Data_base"/"Users_records.json"

today = datetime.datetime.today()
min_year = datetime.date(today.year-120, 1, 1)

data_json = tools_generales.read_json(json_path)

st.write("# Formulario de registro ✍️")
st.write("* Complete todos los datos solicitados. Recuerde que todos los campos son obligatorios")

with st.form("Formulario de registro"):
    username = st.text_input("Nombre de Usuario:") 

    name = st.text_input("Nombre Completo:")

    mail = st.text_input("Mail:")

    birthday = st.date_input("Fecha de nacimiento:", value=None, max_value = today, min_value = min_year)
    if birthday:
        birthday = birthday.strftime("%Y-%m-%d")

    gender = st.selectbox('Genero:', ['masculino', 'femenino', 'otro'],index = None, placeholder = 'Seleccioná una opción')

    submit = st.form_submit_button('Submit')
    
    user_data = {
                'nombre_de_usuario':username, 
                'nombre_completo':name, 
                'mail':mail, 
                'nombre_mail':f"{name} ({mail})",
                'fecha_de_nacimiento':birthday, 
                'genero':gender,
                'score':0
            }
    
    if submit:
        for key in user_data: 
            if user_data[key] == '' or user_data[key] == None:
                key_modif = key.replace('_', ' ')
                st.error(f'El campo {key_modif} esta incompleto', icon="🚨")
        
        if '' in user_data.values() and None in user_data.values():
            st.write('No se pudieron cargar los datos.')
        else:
            #buscamos si el mail ingresado se encunetra en nuestros usuarios cargados
            index = tools_registro.search_email(data_json, user_data)
            if index == -1:
                #Al retonar -1, sabemos que no se encuentra cargado y lo agregamos dentro del archivo.
                data_updated_json = tools_registro.add_data(data_json, user_data)
                tools_generales.write_json(json_path, data_updated_json)
                st.write("Se ha agregado exitosamente la informacion")
            else:
                #Al retorna un numero distinto a -1, sabemos que es el indice donde se encuentra, por lo tanto actualizamos su informacion.
                data_updated_json = tools_registro.update_data(data_json, user_data, index)
                tools_generales.write_json(json_path, data_updated_json)
                st.write("Se ha actualizado exitosamente la informacion")
        
        #st.write(data_json) #descomentar para ver como se va modificando el json en la misma pagina
