import scrapy

class TripItem(scrapy.Item):
    title = scrapy.Field()
    rating = scrapy.Field()
    reviews = scrapy.Field()
    location = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    room_type = scrapy.Field()
    price = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    image_paths = scrapy.Field()