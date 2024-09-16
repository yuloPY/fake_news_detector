import scrapy

class CnnNewsSpider(scrapy.Spider):
    name = "cnn_news"
    allowed_domains = ["edition.cnn.com"]
    start_urls = ["https://edition.cnn.com/2024/09/16/us/gilgo-beach-killings-asian-doe/index.html"]

    custom_settings = {
        'ROBOTSTXT_OBEY': False,
        'FEEDS':{
            r'C:your_directory\fake_news_detector\article_cnn.csv':{
                'format':'csv',
                'encoding':'utf8',
                'overwrite':True
            }
        }
    }

    def parse(self, response):
        
        paragraphs = response.css('p.paragraph.inline-placeholder.vossi-paragraph-primary-core-light::text').getall()
        
       
        full_text = ' '.join(paragraphs)
        
       
        yield {
            'article_text': full_text
        }
