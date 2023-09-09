Python 3.11.5 (v3.11.5:cce6ba91b3, Aug 24 2023, 10:50:31) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import scrapy
... 
... class PhonesSpider(scrapy.Spider):
...     name = "phones"
...     start_urls = ['https://www.productdetail.com/']
... 
...     def parse(self, response):
...         for phone in response.css('div.phone'):
...             yield {
...                 'product_name': phone.css('h2::text').get(),
...                 'brand': phone.css('div.brand::text').get(),
...                 'description': phone.css('div.description::text').get(),
...                 'operating_system': phone.css('div.os::text').get(),
...                 'display_technology': phone.css('div.display::text').get(),
...                 'image_url': phone.css('img::attr(src)').get(),
...             }
...         
...         # Pagination logic (if required)
...         next_page = response.css('a.next_page::attr(href)').get()
...         if next_page is not None:
...             yield response.follow(next_page, self.parse)
