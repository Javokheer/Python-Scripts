"""
parse table from html files and store it to CSV file
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import csv
import os


html = open("html.html").read()
soup = BeautifulSoup(html)
table = soup.find("table")
output_rows = []
for table_row in table.findAll('tr'):
    columns = table_row.findAll('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)

with open('output.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)