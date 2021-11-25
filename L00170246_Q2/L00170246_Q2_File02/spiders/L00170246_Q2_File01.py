"""
#
# File          :   L00170167_Q2_File_1.py
# Created       :
# Author        :   Pierce O'Neill
# Version       :   1.0.0
# Licensing     :   (C) 2021 Pierce O'Neill LYIT
#                   Available under GNU Public License (GPL)
# Description   :   Question 3 - Create an SSH Connection to the VM
#
"""
import scrapy


class L00170246Q2Spider(scrapy.Spider):
    name = 'L00170246_Q2_File02'
    allowed_domains = ['www.lyit.ie']
    start_urls = ['https://www.lyit.ie/']

# Find in the Title of the LKIT Page and returning the text in the CSV file
    def parse(self, response):
        name = response.xpath("//title/text()").getall()

        yield {
            'title': name
        }

# Find any H3 elements of the LKIT Page and returning the text in the CSV file
    def parse(self, response):
        name = response.xpath("//h3/text()").getall()

        yield {
            'h3': name
        }

# Find the areas of study offered by LKIT and return it in the csv file
    def parse(self, response):
        name = response.xpath("//option/text()").getall()

        yield {
            'option': name
        }