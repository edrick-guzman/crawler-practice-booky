import scrapy

from .. import items

class BookyMakatiEatCrawler(scrapy.Spider):
    name = 'booky-eat-makati-spider'
    start_urls = ['https://ph.phonebooky.com/playlist/eat-area/pasay/']


    def parse(self, response):
        SET_SELECTOR = ".standard"
        class_set = response.css(SET_SELECTOR)
        EXPERIENCE_URL_SELECTOR = "meta::attr(content)"


        for experience in class_set.css(EXPERIENCE_URL_SELECTOR):
            
            if str(experience.extract()).__contains__('restaurant'):
                yield scrapy.Request(experience.extract(), callback=self.parse_experience)
    
    def parse_experience(self, response):
        
        NAME = response.css('h1 ::text').extract_first()
        ADDRESS = response.css('p.listing-address span::text').extract_first()
        CATEGORY = response.css('p#listing-category::text').extract()
        CURR_URL = response.request.url
        LATITUDE = str(response.css('meta[itemprop = "latitude"]::attr(content)').extract_first())
        LONGITUDE = str(response.css('meta[itemprop = "longitude"]::attr(content)').extract_first())
        if len(response.xpath('//div[@class="ribbon-body"]//text()').extract()) > 0:
            try: 
                DEAL = str(response.xpath('//div[@class="ribbon-body"]//text()').extract_first().encode('utf-8')) + ' ' + str(response.xpath('//div[@class="ribbon-body"]//text()')[1].extract().encode('utf-8'))
            except:
                DEAL = "N/A"
                
            IMAGE_URL = str(response.xpath('//*[@id="offer-item"]/li/a/meta[@itemprop="image"]/@content').extract_first())
        else: 
            DEAL = 'N/A'
            IMAGE_URL = 'N/A'

        
        item = items.BookyMakatiEatCrawlerItem()

        item['URL'] = CURR_URL
        item['Name'] = NAME
        item['Category'] = CATEGORY
        item['Address'] = ADDRESS
        item['Coordinates'] = LATITUDE + ',' + LONGITUDE
        item['Deal'] = DEAL
        item['Image_url'] = IMAGE_URL

        yield item




