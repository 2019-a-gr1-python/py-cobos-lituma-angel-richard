# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 14:40:56 2019

@author: Richard
"""

import os
import sqlite3
import pandas as pd

path_guardado = '/Users/Richard/Documents/GitHub/py-cobos-lituma-angel-richard/03_Pandas/data/csv/artwork_data.pickle'
df_completo_pickle = pd.read_pickle(path_guardado)
df = df_completo_pickle.iloc[49980:50019, :].copy()
df.to_excel('ejemplo_basico_excel.xlsx')
df.to_excel('ejemplo_basico_excel1.xlsx', index = False)
columnas = ['artist', 'title', 'year']
df.to_excel('columnas.xlsx', columns = columnas)


writer = pd.ExcelWriter('multiples_worksheet.xlsx', engine = 'xlsxwriter')
df.to_excel(writer, sheet_name = 'Preview')
df.to_excel(writer, sheet_name = 'Preview Dos', index = False)
df.to_excel(writer, sheet_name = 'Preview Tres', columns = columnas)
writer.save()

artistas_contados = df_completo_pickle['artist'].value_counts() 

writer = pd.ExcelWriter('colores.xlsx', engine = 'xlsxwriter')

artistas_contados.to_excel(writer, sheet_name = 'Artistas Contados')

hoja_artistas = writer.sheets['Artistas Contados']

rango_celdas = 'B2.B{}'.format(len(artistas_contados.index))

formato = {'type': '2_color_scale',
           'min_value': '10', 
           'min_type': 'percentile', 
           'max_value':'99', 
           'max_type':'percentile'}
hoja_artistas.conditional_format(rango_celdas, formato)

writer.save()

######################################sSQL#######################################

with sqlite3.connect('bdd_python.db') as conexion:
    df.to_sql('tabla', conexion)





######################################JSON######################################
    
df.to_json('artistas.json')
df.to_json('artistas_orientado_tabla.json', orient = 'table')
