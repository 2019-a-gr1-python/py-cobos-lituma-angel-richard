import scrapy
from scrapy.spiders import CrawlSpider, Rule 
from scrapy.linkextractors import LinkExtractor


class AraniaCrawlOnu(CrawlSpider):
    # Heredado conservar nombre
    name = 'crawl_onu'  
    allowed_domains = ['books.toscrape.com']
    #allowed_domains = ['un.org'] # Heredado conservar nombre
    # Heredado conservar nombre
    start_urls = ['http://books.toscrape.com/catalogue/category/books/mystery_3/index.html']
    #start_urls = ['https://www.un.org/en/sections/about-un/funds-programmes-specialized-agencies-and-others/index.html']
    
    regla_uno = (Rule(LinkExtractor(), callback = 'parse_page'),)
    
    url_segmento_restringido = (
        'ar/sections', 
        'zh/sections', 
        'ru/sections'
    )
    #url_segmento_permitido = ('funds-programmes-specialized-agencies-and-others')
    url_segmento_permitido = ('mystery_3', 'fantasy_19')

    regla_dos = (Rule(LinkExtractor(allow_domains = allowed_domains, 
                        allow = url_segmento_permitido), 
                        callback = 'parse_page'),)

    regla_tres = (Rule(LinkExtractor(allow_domains = allowed_domains, 
                        allow = url_segmento_permitido,
                        deny = url_segmento_restringido ),
                        callback = 'parse_page'),)




    rules = regla_dos   
    def parse_page(self, response):
        lista_libros = response.css('article.product_pod > h3 > a::attr(title)').extract()

        for libro in lista_libros:
            with open ('libros.txt', 'a+') as archivo:
                archivo.write(libro+ '\n')


    