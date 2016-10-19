import scrapy

class QuotesSpider(scrapy.Spider):
	name = "quotes"
	start_urls = []
	for i in range(1,11):
		url = 'http://quotes.toscrape.com/page/' + str(i) + '/'
		start_urls.append(url)
	
	def parse(self, response):
		page = response.url.split("/")[-2]
		filename = 'quotes-%s.html'%page
		with open(filename, 'wb') as f:
			f.write(response.body)