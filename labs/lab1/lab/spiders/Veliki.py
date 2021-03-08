import scrapy

xPathQueries = {
    'page_link': '//div[@class="pages"]//a/@href',
    'product': '//ul[@class="stores1"]//li',
    'price': './/div[@class="price "]/text()',
    'name': './/strong[@class="name"]/a/text()',
    'image': './/div[@class="holder kExist"]/a/img/@src',
}

class VelikiSpider(scrapy.Spider):
    name = "veliki"
    start_urls = [
        'https://veliki.com.ua/dir_velozapchasti.htm'
    ]
    allowed_domains = [
        'veliki.com.ua'
    ]
    custom_settings = {
        'CLOSESPIDER_PAGECOUNT': 0,
        'CLOSESPIDER_ITEMCOUNT': 20
    }

    def parse(self, response):
        for product in response.xpath(xPathQueries["product"]):
            yield {
                'name': ''.join(product.xpath(xPathQueries['name']).extract()),
                'img': product.xpath(xPathQueries['image']).extract(),
                'price': product.xpath(xPathQueries['price']).get()
            }
        for a in response.xpath(xPathQueries["page_link"]):
            yield response.follow(a.extract(), self.parse)
