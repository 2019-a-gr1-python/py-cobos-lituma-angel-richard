# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import TakeFirst

def precio(precio_entero, precio_decimal):
    precio_total = precio_entero + '.'+precio_decimal
    return precio_total
    #numero_precio_total = float(precio_total)
	#return numero_precio_total
	
class CelularesItem(scrapy.Item):
    costo  = scrapy.Field(input_processor = MapCompose(precio_celular), output_processor = TakeFirst())
	nombre = scrapy.Field()
    historial = scrapy.Field()    
