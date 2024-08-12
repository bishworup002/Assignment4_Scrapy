# Settings for Scrapy
BOT_NAME = 'scrapy_trip'
SPIDER_MODULES = ['scrapy_trip.spiders']
NEWSPIDER_MODULE = 'scrapy_trip.spiders'

# Enable the Images Pipeline
ITEM_PIPELINES = {
    'scrapy_trip.pipelines.TripPipeline': 300,
    'scrapy_trip.pipelines.TripImagesPipeline': 1,
}

IMAGES_STORE = 'images'

# PostgreSQL Database Configuration
DATABASE = {
    'drivername': 'postgresql',
    'host': 'localhost',
    'port': '5433',
    'username': 'postgres',
    'password': 'p@stgress',
    'database': 'trip'
}


ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

DOWNLOAD_DELAY = 3

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Enable and configure the AutoThrottle extension (disabled by default)
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0

# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG = False

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
FEED_EXPORT_ENCODING = 'utf-8'