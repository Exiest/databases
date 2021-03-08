from scrapy import cmdline
cmdline.execute("scrapy crawl veliki -o files/veliki.xml -t xml".split())
