import scrapy

xPathQueries = {
    'image': '//img/@src',
    'text': '//*[not(self::script) and not(self::style)]/text()',
    'link': '//a/@href'
}

def notEmpty(str):
    return len(str) > 0

class RidnaUaSpider(scrapy.Spider):
    name = "ridnaua"
    custom_settings = {
        'ITEM_PIPELINES': {
            'lab.pipelines.Lab1Pipeline': 300,
        }
    }
    start_urls = [
        'https://ridna.ua'
    ]
    allowed_domains = [
        'ridna.ua'
    ]

    def parse(self, response):        
        text = filter(notEmpty, map(lambda str: str.strip(), [text.extract() for text in response.xpath(xPathQueries["text"])]))
        images = map(lambda url: ((response.url + url) if url.startswith('/') else url), [img_src.extract() for img_src in response.xpath(xPathQueries["image"])])
        page = response.url
        yield {
            'text': text,
            'images': images,
            'url': page
        }
        for next_page in response.xpath(xPathQueries['link']):
            yield response.follow(next_page.extract(), self.parse)
