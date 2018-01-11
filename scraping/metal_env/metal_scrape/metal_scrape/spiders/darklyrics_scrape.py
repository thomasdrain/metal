import csv
import scrapy
from scrapy.selector import Selector

class darklyrics_songs(scrapy.Spider):
	name = 'darklyrics_songs'
	download_delay = 5
	randomize_download_delay = 2.5
	start_urls = ['http://www.darklyrics.com/a.html']
	pages_scraped = 0
	
	# Create alphabet list of uppercase letters
	alphabet = []
	for letter in range(65, 91):
    	alphabet.append(chr(letter))

	def parse(self, response):

		# Scrape the album page for each band
		for href in response.xpath('FILL ME IN... EACH BAND URL').extract():
			band_url = response.urljoin(href)
			#print(url)
			yield scrapy.Request(band_url, callback = self.parse_albums_page)
	
		# FILL IN THE XPATH
		nextpage = response.xpath('').extract_first()
		# Check this condition doesn't return the previous URL
		if nextpage is not None:
			#print("Businesses scraped: " + str(self.pages_scraped))
			#print(response.xpath('//nav[@class = "pagination"]/nav[@class = "pagination"]/a/@href').extract_first())
			yield scrapy.Request(response.urljoin(nextpage), callback = self.parse_albums_page)
	
	
	def parse_albums_page(self, response):
		albums = {}
		# FOR EXAMPLE......
		albums['darklyrics_url'] =            response.request.url
		albums['album_name'] =           response.xpath('//h1[@class = "listing-details__title"]/span[@itemprop = "name"]/text()').extract()

		# Somewhere I need this...
		yield scrapy.Request(response.urljoin(nextpage), callback = self.parse_songs)

		return albums

	def parse_songs(self, response):
		songs = {}
		# FOR EXAMPLE......
		songs['darklyrics_url'] =            response.request.url
		songs['song_name'] =           response.xpath('//h1[@class = "listing-details__title"]/span[@itemprop = "name"]/text()').extract()
		return songs		