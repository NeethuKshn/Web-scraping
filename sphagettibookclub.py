import scrapy
import os
import csv

current_dir = os.path.dirname(__file__)
url = os.path.join(current_dir, 'sphagettibookclub.html')

with open(url, encoding='utf8') as file:
    url_data = file.read()

response = scrapy.http.TextResponse(url, body=url_data, encoding='utf-8')

class SphagettibookclubSpider(scrapy.Spider):
    name = "sphagettibookclub"
    allowed_domains = ["spaghettibookclub.org"]
    start_urls = ["https://spaghettibookclub.org"]

    def parse(self, response):
        query = response.xpath('//article')
        csv_file = open('sphagetti.csv', 'w', encoding='utf8',newline='')
        writer = csv.writer(csv_file)
        writer.writerow(['Book', 'Author', 'Reviewed By'])

        for article in query.xpath('div'):
            book = article.xpath('hgroup/h2/a/text()').extract()[0]
            author = article.xpath('hgroup/h3/span/strong/text()').extract()[0]
            reviewer = article.xpath('div/h3/strong/text()').extract()[0]
            writer.writerow([book, author, reviewer])

        csv_file.close()
        pass

