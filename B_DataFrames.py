# -*- coding: utf-8 -*-
"""
Created on Wed May 22 07:54:04 2019

@author: Richard
"""
import numpy as np
import pandas as pd

arr_rand = np.random.randint(0,10,6).reshape(2,3)

df = pd.DataFrame(arr_rand, columns = ['Estatura (cm)', 'Peso (gr)', 'Edad (anios)'],
                                       index=('Angel', 'Richard' )
                                       )

df['Edad (anios)'] ['Angel']


df = pd.DataFrame(arr_rand, columns = ['Estatura (cm)', 'Peso (gr)', 'Edad (anios)'],
                                       index=('13', '14' )
                                       )

df['Edad (anios)'] ['13']


df2 = pd.DataFrame(arr_rand)
df2.columns = ['Estatura ()cm', 'Peso (gr)', 'Edad (anios)']

df2.index['Angel', 'Richard']

df3 = pd.DataFrame(arr_rand)

df3[0] # no es el indice

df2['Estatura (cm)'][0]



