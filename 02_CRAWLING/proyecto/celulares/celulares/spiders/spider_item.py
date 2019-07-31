import scrapy
from celulares.items import ProductoCelular
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst

class AraniaProyecto(scrapy.Spider):
    name = 'arania_celular'

    def start_requests(self):
        urls = ['https://celulares.mercadolibre.com.ec/celulares-smartphones/_ItemTypeID_N']
        for url in urls:
            yield scrapy.Request(url = url)

    def parse(self, response):
        celulares = response.css('div.item__info.item--hide-right-col') 
        for celular in celulares:
            existe_celular = len(celular.css('div.item__price')) 
            if (existe_celular > 0):
                
                producto_loader= ItemLoader(item = ProductoCelular(), selector = celular)
                #precio_entero = celular.css('span.price__fraction')
                #precio_decimal = celular.css('span.price__decimals')

                producto_loader.default_output_processor= TakeFirst()

                producto_loader.add_css('ventas','div.item__condition')
                producto_loader.add_css('precio', 'span.price__fraction' )
                producto_loader.add_css('titulo', 'span.main-title')

                producto_loader.add_css('precio_entero', 'span.price__fraction')
                producto_loader.add_css('precio_decimal', 'span.price__decimals')
                #print(precio_entero)
                #print(precio_decimal)
                
                
                yield producto_loader.load_item()
                #print(titulo.extract_first())
                #print(url.extract_first())