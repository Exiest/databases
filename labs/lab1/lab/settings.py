BOT_NAME = 'lab'

SPIDER_MODULES = ['lab.spiders']
NEWSPIDER_MODULE = 'lab.spiders'

CONCURRENT_REQUESTS_PER_DOMAIN = 8

EXTENSIONS = {
    'scrapy.extensions.closespider.CloseSpider': 100,
}

CLOSESPIDER_PAGECOUNT = 20
ROBOTSTXT_OBEY = False

