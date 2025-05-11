# kallofem_scraper/settings.py
BOT_NAME = "kallofem_scraper"

SPIDER_MODULES = ["kallofem_scraper.spiders"]
NEWSPIDER_MODULE = "kallofem_scraper.spiders"

# Obey robots.txt (set to False for this task, but check legality)
ROBOTSTXT_OBEY = False

# User agent to mimic a browser
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

# Enable JSON export
FEED_FORMAT = "json"
FEED_URI = "products.json"

# Download delay to avoid overloading the server
DOWNLOAD_DELAY = 2