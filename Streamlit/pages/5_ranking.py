import streamlit as st
from streamlit_lottie import st_lottie
from Functions import tools_generales,tools_ranking

tools_generales.reset_game()

#Configuro la pagina de Ranking
st.set_page_config(
    page_title="Ranking",
    page_icon="🏆",
    layout="wide",
)
lottie_file ="https://lottie.host/a00541ac-072a-4336-9f1f-3e5dc31939f4/1NGHW0F3AY.json"

st.title("Ranking🏆")
# hago una columna como para mostrar el ranking y el lottie
with st.container():
    left_column, right_column= st.columns((2))
    with left_column:
        st.subheader("Ranking de los 15 mejores resultados")
        ranking = tools_ranking.show_ranking()
        st.dataframe(ranking, hide_index=True)
    with right_column:
        st_lottie(tools_generales.load_lottieurl(lottie_file))
