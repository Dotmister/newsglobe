__author__ = 'alexandrecornet'

import csv
from newsglobe_uploader import DB_Handler

class Parser:

    def __init__(self):
        dataBase = open('countries_new.csv', 'rb')
        reader = csv.reader(dataBase)
        self.table = {}
        for country in reader:
            for city in country:
                if city!='':
                    self.table[city.lower()]=country[0].lower()

    def process(self, news):
        news['countries'] = []

        title = news['title'].split(' ')
        summary = news['summary'].split(' ')

        for string in [title, summary]:
            for word in string:
                if  word.lower() in self.table.keys():
                    news['countries'].append(self.table[word.lower()])
        if news['countries']:
            country_count = {}
            for country in news['countries']:

                if not country_count.has_key(country):
                    country_count[country] = 1
                else:
                    country_count[country] += 1


            max = 0
            for country in country_count:
                if country_count[country] > max:
                    to_add = country
                    max = country_count[country]

            handler = DB_Handler()

            timestamp =news['timestamp']
            link = news['link']
            source = news['source']
            title = news['title']
            print country
            print news['source']
            handler.insert_country(to_add, timestamp, link, source, title)