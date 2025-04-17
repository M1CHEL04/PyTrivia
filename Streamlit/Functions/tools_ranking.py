from pathlib import Path
import pandas as pd
import streamlit as st


def show_ranking():
    json_file_path = Path('..')/'Streamlit'/'Data_base'/'Users_records.json'
    # Leer datos del JSON
    users_data = pd.read_json(json_file_path, orient='records')
    # Ordenar por puntaje y tomar los primeros 15
    top_users = users_data.sort_values(by='score', ascending=False).head(15)
    # Restablecer el índice para que las posiciones sean correctas
    top_users.reset_index(drop=True, inplace=True)
    # Crear una columna de posiciones
    top_users['Posicion'] = top_users.index + 1
    # Mostrar el DataFrame con la columna de posiciones y otros datos
    top_users = top_users[['Posicion', 'nombre_de_usuario', 'mail', 'score']]

    return top_users

def show_position(mail):
    """
    This function recieves an user mail and returns its position in the ranking
    """
    ranking = show_ranking()
    data = ranking.loc[ranking['mail'] == mail]
    return data["Posicion"].values[0]
    