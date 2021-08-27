from typing import Generator
import unittest
import os
import sys
sys.path.append(os.path.abspath('./Leadbook/spiders'))
from company_index import CompanyIndexSpider
from scrapy.http import Request, Response, HtmlResponse
class TestLeadbookSpider(unittest.TestCase):
    spider = None

    def setUp(self):
        self.spider = CompanyIndexSpider()

    def test_parse_for_entry_page(self):
        items = self.spider.parse(self.get_fake_response_from_file('tests/sample_htmls/entry_page.html',
                                'http://www.adapt.io/directory/industry/telecommunications/A-1/'))

        items = list(items)
        expected = self.get_expected_output()

        self.assertEqual(26, len(items))
        for exp, found in zip(expected, items):
            self.assertIsInstance(found, Request)
            self.assertEqual(exp, found.url)

    
    
    def get_fake_response_from_file(self, file_name, url):
        request = Request(url=url)

        file_name = os.path.abspath(file_name)
        with open(file_name, 'r') as f:
            file_content = f.read()

        response = HtmlResponse(url, body=file_content, encoding='utf-8', request=request)                
        return response

    def get_expected_output(self):
        return [
            'https://www.adapt.io/directory/industry/telecommunications/A-1',
            'https://www.adapt.io/directory/industry/telecommunications/B-1',
            'https://www.adapt.io/directory/industry/telecommunications/C-1',
            'https://www.adapt.io/directory/industry/telecommunications/D-1',
            'https://www.adapt.io/directory/industry/telecommunications/E-1',
            'https://www.adapt.io/directory/industry/telecommunications/F-1',
            'https://www.adapt.io/directory/industry/telecommunications/G-1',
            'https://www.adapt.io/directory/industry/telecommunications/H-1',
            'https://www.adapt.io/directory/industry/telecommunications/I-1',
            'https://www.adapt.io/directory/industry/telecommunications/J-1',
            'https://www.adapt.io/directory/industry/telecommunications/K-1',
            'https://www.adapt.io/directory/industry/telecommunications/L-1',
            'https://www.adapt.io/directory/industry/telecommunications/M-1',
            'https://www.adapt.io/directory/industry/telecommunications/N-1',
            'https://www.adapt.io/directory/industry/telecommunications/O-1',
            'https://www.adapt.io/directory/industry/telecommunications/P-1',
            'https://www.adapt.io/directory/industry/telecommunications/Q-1',
            'https://www.adapt.io/directory/industry/telecommunications/R-1',
            'https://www.adapt.io/directory/industry/telecommunications/S-1',
            'https://www.adapt.io/directory/industry/telecommunications/T-1',
            'https://www.adapt.io/directory/industry/telecommunications/U-1',
            'https://www.adapt.io/directory/industry/telecommunications/V-1',
            'https://www.adapt.io/directory/industry/telecommunications/W-1',
            'https://www.adapt.io/directory/industry/telecommunications/X-1',
            'https://www.adapt.io/directory/industry/telecommunications/Y-1',
            'https://www.adapt.io/directory/industry/telecommunications/Z-1',
        ]

    def test_parse_for_company_index(self):
        items = self.spider.parse_company_index(self.get_fake_response_from_file('tests/sample_htmls/entry_page.html',
                                 'http://www.adapt.io/directory/industry/telecommunications/A-1/'))

        items = list(items)
        self.assertEqual(99, len(items))
        
        data = items[:49]
        for found in data:
            self.assertIsInstance(found, dict)
            self.assertEqual('company_index', found['record_type'])
        self.assertEqual('A + Communications and Security', data[0]['company_name'])
        self.assertEqual('https://www.adapt.io/company/a--communications-and-security', data[0]['source_url'])
        
        company_urls_to_follow = items[49:98]
        for found in company_urls_to_follow:
            self.assertIsInstance(found, Request)
        self.assertEqual('https://www.adapt.io/company/a--communications-and-security', company_urls_to_follow[0].url)

        follow_url = items[-1]
        
        self.assertIsInstance(follow_url, Request)
        self.assertEqual('https://www.adapt.io/directory/industry/telecommunications/A-2', follow_url.url)


    def test_parse_for_company_index_no_next(self):

        items = self.spider.parse_company_index(self.get_fake_response_from_file('tests/sample_htmls/A-9.html',
                                'http://www.adapt.io/directory/industry/telecommunications/A-9/'))

        items = list(items)
        self.assertEqual(18, len(items))

        data = items[:9]
        for found in data:
            self.assertIsInstance(found, dict)
            self.assertEqual('company_index', found['record_type'])
        self.assertEqual('Award Solutions', data[0]['company_name'])
        self.assertEqual('https://www.adapt.io/company/award-solutions', data[0]['source_url'])
        
        company_urls_to_follow = items[9:]
        for found in company_urls_to_follow:
            self.assertIsInstance(found, Request)
        self.assertEqual('https://www.adapt.io/company/azercosmos-ojsco', company_urls_to_follow[-1].url)


    def test_parse_for_company_details(self):
        items = self.spider.parse_company_index(self.get_fake_response_from_file('tests/sample_htmls/A+.html',
                                'https://www.adapt.io/company/a--communications-and-security'))

        self.assertIsInstance(items, Generator)


if __name__ == '__main__':
    unittest.main()