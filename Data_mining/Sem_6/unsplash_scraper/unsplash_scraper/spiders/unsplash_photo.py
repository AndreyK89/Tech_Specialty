import scrapy


class UnsplashPhotoSpider(scrapy.Spider):
    name = 'unsplash_photo'
    allowed_domains = ['www.unsplash.com']
    start_urls = ['http://www.unsplash.com/']

    def parse(self, response):
        pass
