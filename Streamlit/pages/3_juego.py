
import streamlit as st # type: ignore
import pandas as pd # type: ignore
from pathlib import Path
from Functions import tools_registro
from Functions import tools_generales
from Functions import tools_juego as t
from Functions import tools_ranking as tr
from datetime import datetime

#Configuro la pagina de Juego
st.set_page_config(
    page_title="Juego",
    page_icon="🎮",
    layout="wide",
)

st.markdown(
    """
    <h1 style="text-align: center;">
        <span style="color: #FF4500;">P</span>
        <span style="color: #FFD700;">y</span>
        <span style="color: #32CD32;">T</span>
        <span style="color: #87CEEB;">r</span>
        <span style="color: #FF69B4;">i</span>
        <span style="color: #FFA500;">v</span>
        <span style="color: #6A5ACD;">i</span>
        <span style="color: #FF6347;">a 🕹️</span>
    </h1>
    """,
    unsafe_allow_html=True
    )


fr_json = Path('..')/"Streamlit"/"Data_base"/"Users_records.json"
users = pd.read_json(fr_json, orient="records")

gr_json = Path('..')/"Streamlit"/"Data_base"/"Game_record.json"
data_json = tools_generales.read_json(gr_json)

if 'game_state' not in st.session_state:
    st.session_state['game_state'] = {
        "state" : "INICIO",
        "nombre_mail": None,
        "tema" : None,
        "dificultad": None,
        "respuestas_correctas" : 0,
        "score" : 0,
        "delta" : None
    }

if 'answers' not in st.session_state:
    st.session_state['answers'] = {
        "questions" : [],
        "real_answers" : [],
        "user_answers" : [],
        "options": []
    }

if st.session_state.game_state['state'] == "INICIO":
    with st.form('inicio'):
        nombre_mail = st.selectbox("**Usuario:**", users["nombre_mail"].values, index = None, placeholder = 'Seleccionar')
        dataset = st.selectbox("**Temática:**", ("lagos", "aeropuertos", "conectividad", "censo"), index = None, placeholder = 'Seleccionar')
        dificultad = st.selectbox("**Dificultad:**", ("facil", "media", "dificil"), index = None, placeholder = 'Seleccionar')
        st.warning('Si todavia no tienes usuario, puedes crearlo haciendo click en "Registrarse"')
        col1, col2 = st.columns([1,1]) 
        with col1:
            jugar = st.form_submit_button('Jugar', use_container_width=True)
        with col2:
            registrarse = st.form_submit_button('Registrarse', use_container_width=True)
    if jugar:
        if nombre_mail and dataset and dificultad:
            st.session_state.game_state['state'] = "NUEVO"
            st.session_state.game_state['nombre_mail'] = nombre_mail
            st.session_state.game_state['tema'] = dataset
            st.session_state.game_state['dificultad'] = dificultad
            
            while len(st.session_state.answers['questions']) < 5:
                question, answer, options = t.process_thematic(dataset)

                if question not in st.session_state.answers['questions']:
                    st.session_state.answers['questions'].append(question)
                    st.session_state.answers['real_answers'].append(answer)
                    st.session_state.answers['options'].append(options)
            st.rerun()
        else:
            st.error(f'Completar todos los campos!', icon="🚨")
    elif registrarse:
        st.switch_page("pages/4_formulario_de_registro.py")

elif st.session_state.game_state['state'] == "NUEVO":
    with st.form(key="preguntas"):
        for i in range(0, 5):
            c = st.container(border=True)
            c.write(f"Pregunta #{i+1}") 
            match st.session_state.game_state['dificultad']:
                case "facil":
                        st.session_state.game_state['delta'] = 1
                        c.write(st.session_state.answers['questions'][i])
                        respuesta = c.radio("Selecciona la respuesta:" ,st.session_state.answers['options'][i], key=f"a{i}",index=None) 

                case "media":
                    st.session_state.game_state['delta'] = 1.5
                    c.write(st.session_state.answers['questions'][i])
                    clue = t.generate_clue(st.session_state.answers['real_answers'][i])
                    c.write(f"Pista: {clue}")
                    respuesta = c.text_input("respuesta:", key=f"a{i}")

                case "dificil":
                    st.session_state.game_state['delta'] = 2
                    c.write(st.session_state.answers['questions'][i])
                    respuesta = c.text_input("respuesta:", key=f"a{i}")
        responder = st.form_submit_button("Responder")
    if responder:
        st.session_state.answers['user_answers'] = [st.session_state.a0, st.session_state.a1, st.session_state.a2, st.session_state.a3, st.session_state.a4]
        
        for i in range(0, 5):
            if st.session_state.answers['user_answers'][i]:
                if str(st.session_state.answers['real_answers'][i]).lower() == str(st.session_state.answers['user_answers'][i]).lower():
                    st.session_state.game_state['respuestas_correctas'] += 1
        st.session_state.game_state['state'] = "MOSTRAR_PUNTAJE"

        # Creo el diccionario para Game_record a partir de toda la informacion de la sesion
        user_info = users.loc[users['nombre_mail'] == st.session_state.game_state['nombre_mail']].values

        st.session_state.game_state['score'] = st.session_state.game_state['respuestas_correctas']*st.session_state.game_state['delta']

        game_record = {"usuario": user_info[0][0],
                    "mail": user_info[0][2],
                    "genero": user_info[0][5], 
                    "fecha_de_juego": datetime.now().strftime('%Y-%m-%d'),
                    "hora_de_juego": datetime.now().strftime('%H:%M:%S'), 
                    "respuestas_correctas": st.session_state.game_state['respuestas_correctas'],
                    "dificultad": st.session_state.game_state['dificultad'], 
                    "tematica": st.session_state.game_state['tema'], 
                    "puntos": st.session_state.game_state['score'] }
        
        # Guardo la informacion nueva (ultimo puntaje en Users_records y el nuevo diccionario en Game_record)
        # Game_record
        data_updated_json = tools_registro.add_data(data_json, game_record)
        tools_generales.write_json(gr_json, data_updated_json)
        # Users_records
        users.loc[users['nombre_mail'] == st.session_state.game_state['nombre_mail'], 'score'] =  st.session_state.game_state['score']
        users.to_json(fr_json, orient="records")

        st.rerun()

elif st.session_state.game_state['state'] == "MOSTRAR_PUNTAJE":
    
    user_info = users.loc[users['nombre_mail'] == st.session_state.game_state['nombre_mail']].values

    c1 = st.container(border=True)
    c1.write(f"**La cantidad de respuestas correctas es:**  {st.session_state.game_state['respuestas_correctas']}")
    c1.write(f"**El puntaje es:**  {st.session_state.game_state['score']}")
    c1.write(f"**La posicion en el ranking es:** {tr.show_position(user_info[0][2])}")
    
    with st.container(border=True):
        for i in range(0, 5):
            with st.container(border=True):
                st.write(f"**Pregunta #{i+1}**")
                st.write(st.session_state.answers['questions'][i])
                st.write("***Respuesta correcta:***")
                st.write(st.session_state.answers['real_answers'][i])
                st.write("***Tu respuesta:***")
                if st.session_state.answers['user_answers'][i]:
                    if str(st.session_state.answers['real_answers'][i]).lower() == str(st.session_state.answers['user_answers'][i]).lower():
                        st.success(st.session_state.answers['user_answers'][i])
                    else:
                        st.error(st.session_state.answers['user_answers'][i])
                else:
                    st.error('')
    del st.session_state.answers
    del st.session_state.game_state
    
    if st.button("Volver al inicio", use_container_width=True):
        # Reinicio la sesion y vuelvo a la pagina de inicio de juegos
        st.rerun()
    st.write("**Ranking:**")
    st.dataframe(tr.show_ranking(), hide_index=True)

