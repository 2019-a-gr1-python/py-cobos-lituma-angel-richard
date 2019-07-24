# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 14:54:24 2019

@author: Richard
"""

import numpy as np
import pandas as pd

arr_rand = np.random.randint(0, 10, 6).reshape(2, 3)
df = pd.DataFrame(arr_rand, columns=['Estatura (cm)', 'Peso (gr)', 'Edad (anios)'], 
index=['Richard', 'Angel'])

df['Estatura (cm)']['Richard']

df = pd.DataFrame(arr_rand, columns=['Estatura (cm)', 'Peso (gr)', 'Edad (anios)'], 
index=['13', '14'])


df2 = pd.DataFrame(arr_rand)
df2.columns = ['Estatura (cm)', 'Peso (gr)', 'Edad (anios)']
df2.index = ['Angel', 'Richard']
df3 = pd.DataFrame(arr_rand)

df3[1] #  es el indice de  la variable de la columna 
df2['Estatura (cm)'] # nombre de la columna
type(df2['Estatura (cm)'])

df2['Estatura (cm)'][0]
































































