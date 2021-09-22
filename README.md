# complexscraper-mongodb-unittest

**Scraping**
An website was scraped using scrapy. First the all the website url was collected, then the data from those websites were scraped recursively.

**Storing**
The scraped data was then saved in json format. The data was stored in MongoDB database.

**Testing and Validation**
Unittesting was used to test the spider code. Then json data file was validated to check if the schema is valid.

**How to run**

Open folder 'Solution' in VS code

Run the following commands if necessary:

Install scrapy if not instlled by running: pip Install scrapy
Install pymongo by running: pip install pymongo
Install json if not installed: pip install json
Install jsonschema if not installed: pip install jsonschema

Run this command to start scraping: scrapy company_index
Run this command to run the test code(on windows):  python .\tests\test_leadbook_spider.py
Run this command to run the validator code(on windows):python .\tests\validator.py

