"""
    Concurren Futees:
    Two Main class: 
        Excutor class - manages all threads and workload 
        Future class - creates a little instance and then manages the data coming back


with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(function, arg) # main 
    
"""


import pandas as pd
import requests
from bs4 import BeautifulSoup
import concurrent.futures
from csv import reader

urls = []
titles = []

with open('bookslinks.csv', 'r') as f:
        csv_reader = reader(f)
        urls.extend(row[0] for row in csv_reader)

def transform(url):
    r = requests.get(str(url))
    soup = BeautifulSoup(r.content, 'html.parser')
    title = soup.find('h1').text
    titles.append(title)
    print(title)
    return

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(transform, urls) # main 

print(len(titles))
df = pd.DataFrame(titles)
df.to_csv('concurrent-titles.csv', index=False)
print('Complete.')

