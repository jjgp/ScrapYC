import scrapy

from scrapy.crawler import CrawlerProcess


class ItemsSpider(scrapy.Spider):
    name = 'items'
    allowed_domains = ['news.ycombinator.com']

    def start_requests(self):
        yield scrapy.Request(f"https://news.ycombinator.com/item?id={self.item_id}")  # &p=3

    def parse(self, response):
        defaults = response.xpath("//td[@class=\"default\"]")
        hnusers = defaults.xpath(".//a[@class=\"hnuser\"]/text()").getall()
        comments = defaults.xpath(".//div[@class=\"comment\"]")
        commtexts = comments.xpath(".//span[@class=\"commtext c00\"]").getall()
        for hnuser, comment in zip(hnusers, commtexts):
            yield dict(hnuser=hnuser, comment=comment)
        
        for next_page in response.xpath("//a[@class=\"morelink\"]"):
            yield response.follow(next_page, self.parse)


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(ItemsSpider, item_id=30878761)
    process.start()
