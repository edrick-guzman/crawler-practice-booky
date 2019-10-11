# -*- coding: utf-8 -*-
import csv
import scrapy
import datetime

from scrapy.exporters import CsvItemExporter
from datetime import datetime
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class BookyMakatiEatCrawlerPipeline(object):
    def process_item(self, item, spider):
        return item

class CsvWriterPipeline(object):
    def open_spider(self, spider):
        dt_string = datetime.now().strftime("%Y%m%d%H%M%S")
        self.file = open('nookall_booky_crawler'+ dt_string +'.csv', 'w+b')

        self.export_fields = ['Name', 'URL', 'Category', 'Address', 'Coordinates', 'Deal', 'Image_url']
        self.exporter = CsvItemExporter(self.file, fields_to_export=self.export_fields, quoting=csv.QUOTE_ALL)
        self.exporter.start_exporting()
    
    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

