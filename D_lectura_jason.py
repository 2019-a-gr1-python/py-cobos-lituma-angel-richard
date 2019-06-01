# -*- coding: utf-8 -*-
"""
Created on Wed May 22 08:33:51 2019

@author: Richard
"""

import json
import pandas as pd
import os

path = '/Users/Richard/Documents/GitHub/py-cobos-lituma-angel-richard/data/artworks'
archivo = '/a/000/a00001-1035.json'
path_archivo = path + archivo

with open(path_archivo) as text_json:
    contenido_json = json.load(text_json)
    print(type(contenido_json))
    print(contenido_json)
    
    registro_df = []
    llaves = ['id', 'all_artist', 'title', 'medium', 
          'dateText', 'acquisitioYear','height', 
          'width', 'units' ]
    
    for llave in llaves:
        valor = contenido_json[llave]
        registro_df.append(valor)
        
    registro_df_tupla = tuple(registro_df_lista)
    serie = tuple(registrodf)
    
    print(serie)
    print(registro_df_tupla)
    df_chiquito = pd.DataFrame([registro_df_tupla])
    df_chiquito_t = pd.DataFrame([registro_df_tupla])
    




def leer_json(pathl, llaves):
    with opne(path_archivo) as texto_json:
        contenido_json = json.load(texto_json)
    registro_df_lista = []
    for llave in llaves:
        valor = contenido_json[llave]
        
        
