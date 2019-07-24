# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 23:57:02 2019

@author: Richard
"""

import numpy as np
import pandas as pd

print("Hola")

nombre = "Richard"
edad = 33

print(nombre)

lista_numeros = [1,2,3,4]
tupla_numeros = (1,2,3,4)
np_numeros = np.array((1,2,3,4))
numeros_serie_a = pd.Series(lista_numeros)
numeros_serie_b = pd.Series(tupla_numeros)
numeros_serie_c = pd.Series(np_numeros)
numeros_serie_d = pd.Series([True, False, 12, 12.3, "string", None, (), [], {"nombre":"Richard"}])


numeros_serie_a[0]

lista_ciudades = ["Ambato", "Cuenca", "Loja", "Quito"]

serie_ciudades = pd.Series(lista_ciudades, index = ["A", "C", "L", "Q"])
serie_ciudades["5"]
serie_ciudades[0]

serie_ciudades["Q"]
serie_ciudades[0]
serie_ciudades[1]
serie_ciudades[2]
serie_ciudades[3]

print(type(serie_ciudades))

valores_ciudades = {
        "Ibarra":9500, 
        "Guayaquil":10000, 
        "Quito":7000, 
        ":Loja":3000}

serie_valor_ciudad = pd.Series(valores_ciudades)
serie_valor_ciudad["Ibarra"]
serie_valor_ciudad[1]

ciudades_menores = serie_valor_ciudad< 5000
serie_ciudades_menores = serie_valor_ciudad[ciudades_menores]

serie_valor_ciudad =serie_valor_ciudad * 1.1

print(ciudades_menores)
serie_valor_ciudad["Guayaquil"] = 100

print("Lima" in serie_valor_ciudad)

np.square(serie_valor_ciudad)
np.sin(serie_valor_ciudad)

np.sin(pd.Series({}))

ciudades_uno = pd.Series({
        "Quito": 1500, 
        "Loja": 4000, 
        "Guayaquil":2000})

ciudades_dos = pd.Series({
        "Monatanita": 300, 
        "Guayaquil": 1000,
        "Quito": 200})

print(ciudades_uno * ciudades_dos)

randomico = np.random.rand(3)
serie_tres = pd.Series(randomico)
ciudades_uno.index



ciudades_unoe = pd.Series({ 
        "Loja": 4000
        })

ciudades_dose = pd.Series({
        "Monatanita": 300, 
        "Guayaquil": 1000,
        "Quito": 200})


# Unir dos series
serie_ciudad_total_concat = pd.concat([ciudades_unoe , ciudades_dose])

# Para evitar repetidos
serie_ciudad_total = pd.concat([ciudades_unoe , ciudades_dose], verify_integrity = True)
serie_ciudad_total1 = serie_ciudad_total.add(ciudades_dose)

ciudades_unoe.max()
ciudades_dose.mean()
ciudades_dose.median()
np.average(ciudades_dose)
ciudades_dose.head(1) #primer valor del indice
ciudades_dose.tail(1) #ultimo valor
ciudades_dose.sort_values(ascending = False).head(1) # Ordenar por maximo valor
ciudades_dose.sort_values(ascending = False).tail(1) # Ordenar por minimo valor


ciudades_dosej = pd.Series({
        "Monatanita": 1500, 
        "Guayaquil": 1000,
        "Quito": 800, 
        "Cuenca": 2510, 
        "Riobamba": 9810,
        "Esmeraldas": 15230})

ciudades_0_1000 = ciudades_dosej[(ciudades_dosej >= 0) & (ciudades_dosej <=1000)] * 1.05
ciudades_1000_10000 = ciudades_dosej[(ciudades_dosej >1000) & (ciudades_dosej <=10000)] * 1.10
ciudades_10000 = ciudades_dosej[(ciudades_dosej >10000)] * 1.15

resultante_ciudad1 = pd.concat([ciudades_0_1000,ciudades_1000_10000, ciudades_10000])

def calculo(valor):
    if (valor <= 1000):
        return valor * 1.05
    if (valor>1000 and valor <= 10000):
        return valor * 1.10
    if (valor > 10000):
        return valor * 1.15
    
resultante_ciudad = ciudades_dosej.map(calculo)   
ciudad_ejem = ciudades_dosej.where(ciudades_dosej >1000, ciudades_dosej * 1.05)        


pd.Series.max(ciudades_dose)
pd.Series.min(ciudades_dose)








