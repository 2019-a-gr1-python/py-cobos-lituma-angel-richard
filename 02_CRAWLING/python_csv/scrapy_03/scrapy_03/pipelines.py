# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem

class FiltrarSoloCapsulas(object):
    def process_item(self, item, spider):
        titulo = item['titulo']
        if ('liquid' not in titulo):
            raise DropItem('No tiene la palabra liquid en el titulo')
        else:
            return item

class TransformarTitulosMinusculas(object):
    def process_item(self, item, spider):
        item['titulo'] = item['titulo'].lower()
        return item 
        
