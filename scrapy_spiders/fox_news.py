import scrapy

class NewsSpider(scrapy.Spider):
    name = "fox_news"
    allowed_domains = ["www.foxnews.com"]
    start_urls = [
        "https://www.foxnews.com/politics/who-ryan-wesley-routh-alleged-gunman-trump-golf-club" ## You just need to change webadress.
    ]

    custom_settings = {
        'ROBOTSTXT_OBEY': False,
        'FEEDS': {
            r'C:your_directory\fake_news_detector\article_fox.csv': {  
                'format': 'csv',      
                'encoding': 'utf8',  
                'overwrite': True     
            }
        }
    }

    def parse(self, response):
        paragraphs = response.xpath('//div[@class="article-body"]//p[not(ancestor::div[@class="article-meta"])]').xpath('string()').getall()
        article_text = ' '.join(paragraphs).strip()

        yield {
            'article_text': article_text
        }
