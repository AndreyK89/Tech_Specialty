import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class UnsplashSpider(CrawlSpider):
    name = 'unsplash_photo'
    allowed_domains = ['unsplash.com']
    start_urls = ['https://unsplash.com/']

    rules = (
        Rule(LinkExtractor(allow=r'/photos/[a-z0-9\-]+'), callback='parse_photo', follow=True),
        Rule(LinkExtractor(allow=r'/categories/[a-z0-9\-]+'), follow=True),
    )

    def parse_photo(self, response):
        yield {
            'image_url': response.css('img.w-full::attr(src)').get(),
            'title': response.css('h1.text-4xl::text').get(),
            'category': response.css('a.block.text-sm.font-medium.text-gray-500::text').get(),
        }


class UnsplashItem(scrapy.Item):
    image_url = scrapy.Field()
    title = scrapy.Field()
    category = scrapy.Field()


ITEM_PIPELINES = {
    'scrapy.pipelines.images.ImagesPipeline': 1,
}


import csv
from scrapy.pipelines.images import ImagesPipeline

class UnsplashPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        return f'{request.meta["title"]}.jpg'

    def get_media_requests(self, item, info):
        yield scrapy.Request(item['image_url'], meta={'title': item['title'], 'category': item['category']})

    def item_completed(self, results, item, info):
        with open('all_photos.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([item['image_url'], results[0][1]['path'], item['title'], item['category']])


    def save_image(self, response):
        # Получаем имя файла изображения
        filename = response.url.split('/')[-1]
        # Сохраняем изображение в папку images
        with open(f'images/{filename}', 'wb') as f:
            f.write(response.body)
