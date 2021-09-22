# complexscraper-mongodb-unittest

### Scraping:

An website is scraped using scrapy. First the all the website urls are collected, then the data from those websites are scraped recursively.


### Storing:

The scraped data is then saved in json format. The data is also stored in MongoDB database.


### Testing and Validation:

Unit testing is used to test the spider code. Then json data files are validated to check if the schemas are valid.


### How to run:

Open folder 'Solution' in VS code

Run the following commands if necessary:

Install scrapy if not instlled by running: pip Install scrapy
Install pymongo by running: pip install pymongo
Install json if not installed: pip install json
Install jsonschema if not installed: pip install jsonschema

Run this command to start scraping: scrapy company_index
Run this command to run the test code(on windows):  python .\tests\test_leadbook_spider.py
Run this command to run the validator code(on windows):python .\tests\validator.py

