# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 12:55:30 2019

@author: Richard
"""

import pandas as pd

path_guardado ='/Users/Richard/Documents/GitHub/py-cobos-lituma-angel-richard/03_Pandas/data/csv/artwork_data.pickle'

df = pd.read_pickle(path_guardado)

primero = df.loc[1035,'artist']
segundo = df.loc[1036,'units']

df.loc[0]  # Error porque no esta dentro del label indice

primero_a = df.iloc[0,1] # filas por columnas, desde la fila cero la primer columna

primero_b = df.iloc[0,:] # desde la fila cero todas

otroejemplo_b = df.iloc[3,:] # desde la tercera fila y todas las columnas

primero_c = df.iloc[0:100,2:4] # desde la fila cero, los primero 100 columnas, desde la columna 2 hasta la 4

tres_primeros = df.head(10)['width'].sort_values(ascending=False).head(3) # ordenamiento por campo 'width' siguiendo orden

tres_ultimos = df.head(10)['width'].sort_values().tail(3) # ordenamiento solo por el campo width ascendente

a = df['year'].sort_values(axis=0)

serie_validado = pd.to_numeric(df['width'], errors='coerce')


df.loc[:,'width'] = serie_validado
df.iloc[:,5] = serie_validado

diez_primeros = df['height'].sort_values(ascending=False).head(10)

diez_ultimos = df['width'].sort_values(ascending=False).tail(10)

serie_validado_height = pd.to_numeric(df['height'], errors='coerce')
df.loc[:,'height'] = serie_validado_height

area = df['height'] * df['width']

type(area)  # Serie

df['area'] = area

df = df.assign(areados = area)

df_area = df['area'].sort_values(ascending=False).head(1)

id_max_area = df['area'].idxmax()  # Label 

id_min_area = df['area'].idxmin()  # Label

registro_mas_area = df.loc[id_max_area]

registro_menor_area = df.loc[id_min_area]