# kallofem_scraper/settings.py
BOT_NAME = "kallofem_scraper"

SPIDER_MODULES = ["kallofem_scraper.spiders"]
NEWSPIDER_MODULE = "kallofem_scraper.spiders"

# Obey robots.txt (set to False for this task, but check legality)
ROBOTSTXT_OBEY = False

# User agent to mimic a browser
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

# Request headers (optional but helpful)
DEFAULT_REQUEST_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en",
    "User-Agent": USER_AGENT,
}

# Enable JSON export
FEED_FORMAT = "json"
FEED_URI = "products.json"

# Download delay to avoid overloading the server
DOWNLOAD_DELAY = 2

# Retry settings to handle dropped/failed requests
RETRY_ENABLED = True
RETRY_TIMES = 5  # Retry up to 5 times for failed requests
RETRY_HTTP_CODES = [500, 502, 503, 504, 522, 524, 408, 429]

DNS_TIMEOUT = 15

AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1
AUTOTHROTTLE_MAX_DELAY = 10
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0

DOWNLOADER_CLIENT_TLS_METHOD = "TLSv1.2"
DOWNLOADER_CLIENTCONTEXTFACTORY = 'scrapy.core.downloader.contextfactory.BrowserLikeContextFactory'


# Timeout settings
DOWNLOAD_TIMEOUT = 30

# Pipeline
ITEM_PIPELINES = {
    'kallofem_scraper.pipelines.KallofemScraperPipeline': 1,
}

# Logging
LOG_LEVEL = 'INFO'  # Change to 'DEBUG' if you want verbose logs
