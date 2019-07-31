# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy
from scrapy.loader.processors import Join, MapCompose, TakeFirst
from w3lib.html import remove_tags

def precio_celular(precio_entero, precio_decimal):
    precio_total = precio_entero + "." +precio_decimal
    return precio_total
    #numero_precio_total = float(precio_total)
	#return numero_precio_total
	
class ProductoCelular(scrapy.Item):
    titulo = scrapy.Field(
        input_processor = MapCompose(remove_tags), 
        output_processor = TakeFirst(), 
        )
  
    ventas = scrapy.Field(
        input_processor = MapCompose(remove_tags), 
        output_processor = TakeFirst(), 
        )
    
    precio_entero  = scrapy.Field(
        input_processor = MapCompose(remove_tags), 
        output_processor = TakeFirst(), 
        )

    precio_decimal  = scrapy.Field(
    input_processor = MapCompose(remove_tags), 
    output_processor = TakeFirst(), 
    )
    precio = scrapy.Field()
  




    