
"""
Module       : B8IT105 - Programming for Big Data
Assignment   : CA1 - Scrape website graphics cards to CSV.
Description  : Class to scrape the website graphic cards.
Student Code : 10541255
Student Name : Alyosha Pulle
"""

import requests
from bs4 import BeautifulSoup

class TomsHardwareGraphicsCards:
    def __init__(self):
        response = self.__request_web_page()
        soup = BeautifulSoup(response.content, features="html.parser")
        article_table = soup.find('div', class_='articletable')
        self.__scrape_table_column_headers(article_table)
        self.__scrape_table_rows(article_table)

    ### Accessors ###
    
    def get_data_source(self):
        return self.__url
        
    def get_table_column_headers(self):
        return self.__table_column_headers

    def get_table_rows(self):
        return self.__table_rows

    ### Methods ###

    def write_csv(self, file_name):
    # Write the output to a csv
        csv_file = open(file_name, 'w')
        csv_file.write(','.join(self.get_table_column_headers()) + '\n')
        for table_row in self.get_table_rows():
            csv_file.write(','.join(table_row) + '\n')
        csv_file.close()

    ### Private Methods
    
    def __request_web_page(self):
        # Read the webpage and get the response.
        headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
            'Sec-Fetch-Dest': 'document',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Accept-Language': 'en-US,en;q=0.9',
        }
        self.__url = 'https://www.tomshardware.com/reviews/gpu-hierarchy,4388.html'
        return requests.get(self.__url, headers=headers)

    def __scrape_table_column_headers(self, article_table):
        # Read the table column headers.
        # Also gives the missing card name column a heading of Card Name.
        COL_CARD_NAME = 0
        self.__table_column_headers = []
        for index, header in enumerate(article_table.find_all('th')):
            if index == COL_CARD_NAME:
                self.__table_column_headers.append('Card Name')
            else:
                self.__table_column_headers.append(header.text)
       
    def __get_column_link(self, column):
        # Extract the URL from column if exists.
        try:
            return column.a['href']
        except:
            return ''
    
    def __scrape_table_row(self, table_row):
        # Iterate the columns to get each column value.
        # For the Buy column get the 'a' element 'href' attribute URL.
        COL_BUY = 6
        row_values = []
        for index, column in enumerate(table_row.contents):
            if index == COL_BUY:
                row_values.append(self.__get_column_link(column))
            else:
                row_values.append(column.text)
        return row_values
    
    def __scrape_table_rows(self, article_table):
        # Iterate the table rows to get the information on each graphics card.
        self.__table_rows = []
        for table_row in article_table.tbody.find_all('tr'):
            self.__table_rows.append(self.__scrape_table_row(table_row))

