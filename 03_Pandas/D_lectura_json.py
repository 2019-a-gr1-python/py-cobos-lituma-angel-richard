#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 10:20:05 2019

@author: usrdel
"""

import json
import pandas as pd
import os

path = '/Users/usrdel/Documents/GitHub/py-eguez-sarzosa-vicente-adrian/03_Pandas/data/artwork'

archivo = '/a/000/a00001-1035.json'

path_archivo = path + archivo

llaves = ['id','all_artists',
          'title','medium',
          'dateText','acquisitionYear',
          'height','width','units']


def leer_json(path_archivo,llaves):
    with open(path_archivo) as texto_json:
        contenido_json = json.load(texto_json)
    registro_df_lista = []
    for llave in llaves:
        valor = contenido_json[llave]
        registro_df_lista.append(valor)
    return registro_df_lista

leer_json(path_archivo, llaves)


def leer_json_en_carpeta(directorio, llaves):
    trabajos_arte = []
    print(type(os.walk(directorio)))
    for path_raiz, lista_directorios, archivos in os.walk(directorio):
        print(path_raiz)
        print(type(path_raiz))
        print(lista_directorios)
        print(type(lista_directorios))
        print(archivos)
        print(type(archivos))
        
        for nombre_archivo in archivos:
            if nombre_archivo.endswith('json'):            
            ## logica
                directorio_archivo = os.path.join(path_raiz, nombre_archivo)
                pieza_arte = leer_json(directorio_archivo, llaves)
                trabajos_arte.append(pieza_arte)
                break
    df = pd.DataFrame.from_records(trabajos_arte, columns = llaves, index ='id')     
    return df
    
df_artworks = leer_json_en_carpeta(path, llaves)

def leer_json_en_carpeta(directorio, llaves):
    trabajos_arte = []
    print(type(os.walk(directorio)))
    for path_raiz, lista_directorios, archivos in os.walk(directorio):
        print(path_raiz)
        print(type(path_raiz))
        print(lista_directorios)
        print(type(lista_directorios))
        print(archivos)
        print(type(archivos))
        
        for nombre_archivo in archivos:
            if nombre_archivo.endswith('json'):            
            ## logica
                directorio_archivo = os.path.join(path_raiz, nombre_archivo)
                pieza_arte = leer_json(directorio_archivo, llaves)
                trabajos_arte.append(pieza_arte)
                ## sin break selecciona todos me toca entender por que
    df = pd.DataFrame.from_records(trabajos_arte, columns = llaves, index ='id')     
    return df

df_artworks = leer_json_en_carpeta(path, llaves)

##siguiente clase se vera como se puede exportar a excel json, csv

