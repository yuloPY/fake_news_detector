# fake_news_detector
 ## Table of Contents
 - [Introduction](#introduction)
 - [Dataset](#dataset)
 - [Model Description](#model-description)
 - [Usage](#usage)
# Introduction
This project demonstrates how to classify news articles as **fake** or **real** using a **Passive Aggressive Classifier.** The dataset used is a collection of news articles, and the classification is done by processing the text data using **TF-IDF vectorization.**

# Dataset
The dataset used is a CSV file named **[news.csv](open_model/news.csv)**,which contains four columns:
- **ID**:The ID of the news.
- **title**:The title of the news.
- **text**:The content of the news.
- **label**:The label indicating whether the article is **REAL** or **FAKE**.

# Model Description
The code implements a text classification pipeline as follows:

## Data Preprocessing:
 - Removing non-alphabetical characters.
 - Converting all text to lowercase.
 - Removing stopwords using the NLTK library.

## Feature Ectraction:
 - **TF-IDF Vectorization**:Converts text data into numerical features suitable for machine learning models.

## Classification:
 -The model uses the **PassiveAggressiveClassifier**, a linear model that works well for large-scale text data. It updates weights in response to misclassified examples in an aggressive manner.

*you can check the **[open_model.ipynb](open_model/open_model.ipynb)** file for more details.*


# Usage

The main goal of mine project is scrap the data from **[FOX News](https://www.foxnews.com/)** and **[CNN US](https://edition.cnn.com/us)** and make a prediction with my **[fake_news_detector](fake_news_detector/fake_news_detector.ipynb)** model.
(I hope that is legal.)

I will explain here how do you use it in your computer.

**1.** `pip install -r requirements.txt`

**2.** `scrapy startproject exampla_scraper`

**3.** `cd example_scraper`

**4.** `scrapy genspider example example_foxpage_or_cnnpage.com`

After these steps you must have an directory like this:


```shell
    example_scraper/
        scrapy.cfg

        example_scraper/
            __init__.py

            items.py

            middlewares.py

            pipelines.py

            settings.py
            
            spiders/
                __init__.py

                example.py
```
**5.** Open `example.py` in an IDE and you will see this.

```python
import scrapy


class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["www.domain.com"]
    start_urls = ["example_foxpage_or_cnnpage.com"]

    def parse(self, response):
        pass
```

**6.** If your page from FOX News use **[fox_news.py](scrapy_spider/fox_news.py)**.For CNN US use **[cnn_news.py](scrapy_spider/cnn_news.py)**.

**7.** After making the necessary changes start your spider with that command `scrapy crawl spider_name`.

**8.** Scraping phase is complete now you can make prediction with [fake_news_detector.ipynb](fake_news_detector/fake_news_detector.ipynb) model.
