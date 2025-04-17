import streamlit as st
from streamlit_lottie import st_lottie
from Functions import tools_generales

tools_generales.reset_game()

#Configuro la pagina de inicio 
st.set_page_config(
    page_title="PyTrivia",
    page_icon="https://cdn-icons-png.flaticon.com/512/3400/3400510.png",
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
        <span style="color: #FF6347;">a 🏠</span>
    </h1>
    """,
    unsafe_allow_html=True
    )

# Breve descripción del juego
st.markdown("""
    ## En este juego encontrarás una serie de **preguntas** para evaluar tus conocimientos sobre áreas específicas... ¿Crees que estás listo para ser el mejor conocedor?
""")
st.divider()

lottie_file="https://lottie.host/f80545fc-ebb3-4240-b2e5-4409e364f3fe/2k5JHxClsu.json"

lottie=st_lottie(tools_generales.load_lottieurl(lottie_file))

st.divider()

# Explicación del funcionamiento del parámetro dificultad
st.markdown('<h2 style="color:#FFD700;">Datos Necesarios para Comenzar a Jugar 📋</h2>', unsafe_allow_html=True)
st.markdown("""
    - **Usuario**: Regístrate o inicia sesión con tu nombre de usuario.
    - **Dataset**: Elige el dataset sobre el que quieres responder preguntas (lagos, aeropuertos, conectividad, censo).
    - **Dificultad**: Selecciona el nivel de dificultad (fácil, media, difícil).
    """)
st.markdown('<h2 style="color:#FF4500;">Funcionamiento del Parámetro de Dificultad 🎯</h2>', unsafe_allow_html=True)
st.markdown("""
    - **Dificultad difícil**: No se brindan ayudas adicionales.
    - **Dificultad media**: Se muestran la cantidad de letras algunas palabras.
    - **Dificultad fácil**: Se ofrecen tres opciones de respuesta, una de las cuales es correcta.
""")

st.divider()
st.markdown('<h2 style="color:#87CEEB;">Instrucciones Básicas 📝</h2>', unsafe_allow_html=True)
st.markdown("""
1. Ve a la sección de **Formulario de Registro** para crear tu cuenta.
2. En la página de **Juegos**, selecciona tu nombre de usuario, dataset y dificultad.
3. Responde a las preguntas relacionadas segun el dataset.
4. Al finalizar, revisa tus respuestas y tu puntaje.
""")
st.markdown('<h2 style="color:#FF69B4;">Tips y Trucos 💡</h2>', unsafe_allow_html=True)
st.markdown("""
- Lee bien las preguntas antes de responder.
- Busca bien la informacion en la seccion de **Conociendo nuestros datos**.
- ¡Diviértete y aprende algo nuevo cada vez que juegas!
""")


st.markdown('<h2 style="color:#FF4500;">¡¿ ESTAS LISTO !?</h2>', unsafe_allow_html=True)
col1, col2 ,col3= st.columns(3)
with col1:
    if st.button("¡Comienza a Jugar! 🎮"):
        st.switch_page("pages/3_juego.py")

with col2:
    if st.button("Regístrate ✍️"):
        st.switch_page("pages/4_formulario_de_registro.py")

with col3:
    if st.button("¡Buscar informacion!💡"):
        st.switch_page("pages/2_conociendo_nuestros_datos.py")
