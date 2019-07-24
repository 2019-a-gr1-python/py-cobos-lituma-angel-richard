# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 10:06:40 2019

@author: Richard
"""
import pandas as pd
import numpy as np
import os


path ='/Users/Richard/Documents/GitHub/py-cobos-lituma-angel-richard/03_Pandas/data/csv/artwork_data.csv'

df = pd.read_csv(path, nrows = 100, usecols = ['id', 'artist'], index_col = 'id')

columnas_a_usar = ['id', 'artist', 'title', 'medium', 'year', 'acquisitionYear', 'height', 'width', 'units']

df_completo = pd.read_csv(
        path, usecols = columnas_a_usar, index_col = 'id')



path_guardado ='/Users/Richard/Documents/GitHub/py-cobos-lituma-angel-richard/03_Pandas/data/csv/artwork_data.pickle'
df_completo.to_pickle(path_guardado)

df_completo.shape
