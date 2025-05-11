import scrapy
from kallofem_scraper.items import KallofemItem

class KallofemSpider(scrapy.Spider):
    name = "kallofem"
    allowed_domains = ["kallofem.hu"]
    start_urls = ["https://kallofem.hu/shop/group/keriteselemek"]

    def parse(self, response):
        products = response.css("button.product-cart")
        for product in products:
            item = KallofemItem()
            item["product_name"] = product.attrib.get("data-product_name", "").strip()
            item["price"] = product.attrib.get("data-product_price", "").strip()
            img_url = product.attrib.get("data-product_image", "").strip()
            item["image_url"] = response.urljoin(img_url) if img_url else ""
            yield item

        # Pagination (if needed, update selector after checking site nav)
        next_page = response.css("a.next::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
            # Handle subcategories (if any)
        subcategories = response.css("div.category-item a::attr(href)").getall()
        for subcategory in subcategories:
            yield response.follow(subcategory, callback=self.parse)