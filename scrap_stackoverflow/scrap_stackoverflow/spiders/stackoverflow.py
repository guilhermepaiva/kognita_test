import scrapy
from scrap_stackoverflow.items import QuestionItem

class StackoverflowSpider(scrapy.Spider):
    name = 'stackoverflow'
    allowed_domains = ['stackoverflow.com']
    start_urls = ['https://stackoverflow.com/questions/tagged/python/']


    def parse(self, response):
        for href in response.css('.question-summary h3 a::attr(href)'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_question)

    def parse_question(self, response):
        question_item = QuestionItem()
        
        question_item['title'] = response.xpath('//*[@id="question-header"]/h1/a/text()').extract()[0]
        question_item['text'] = ''.join(response.css('.question .post-layout .post-text p::text').extract())
        
        question_item['author'] = response.css('.owner .user-details a::text').extract_first()
        question_item['date'] = response.css('.user-action-time span::attr(title)').extract_first()
        question_item['tags'] = response.css('.question .post-tag::text').extract()
       
        yield question_item
        
