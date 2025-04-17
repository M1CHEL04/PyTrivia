# En este .py estan desarrolladas la funciones "mas generales", por ejemplo la lectura y escritura de archivos

import json
import requests
import streamlit as st

def read_json(path):
    """This function receives the loctaion of the file and returns a variable with the content of this file"""
    with open(path, 'r', encoding="UTF-8") as file:
        data= json.load(file)
    return data

def write_json(path,data):
    """This function write the data in the file passed by parameter"""
    with open(path,'w',encoding="UTF-8") as file:
        json.dump(data,file)

def load_lottieurl(url):
    #cargo el lottie con el url que me traigo por parametro y retorno el json
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

def reset_game():
    if "answers" in st.session_state:
        del st.session_state.answers
    if "game_state" in st.session_state:
        del st.session_state.game_state