# -*- coding: utf-8 -*-
"""
Created on Wed May 22 07:37:09 2019

@author: Richard
"""

import pandas as pd
import os

path = '/Users/Richard/Documents/GitHub/py-cobos-lituma-angel-richard/data/csv/artwork_data.csv'

df = pd.read_csv(
        path, nrows = 5, 
        usecols = ['id', 'artist'],
        engine = 'python'
        )

columnas_a_usar = ['id', 'artist', 'title', 'medium', 'year', 
                   'acquisitionYear', 'height', 'width', 'units'
        ]
df_completo = pd.read_csv (
        path, usecols = columnas_a_usar, 
        index_col = 'id'
        )

path_guardado = '/Users/Richard/Documents/GitHub/py-cobos-lituma-angel-richard/data/csv/artwork_data.pickle'
df_completo.to_pickle(path_guardado)

df_completo_pickle = pd.read_pickle(path_guardado)

df_completo.shape
