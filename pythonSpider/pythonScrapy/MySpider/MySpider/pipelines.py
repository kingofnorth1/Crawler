# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from openpyxl import Workbook
import pymysql
from loguru import logger

class DbSpiderPipeline:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', port=3306,
                                    user='root', password='123456',
                                    database='demo', charset='utf8mb3')
        self.cursor = self.conn.cursor()
        self.data = []

    # def open_spider(self, spider):
    #     pass

    def close_spider(self, spider):
        if len(self.data) != 0:
            self._write_data()
        self.conn.close()

    def process_item(self, item, spider):
        title = item.get('title', '')
        rank = item.get('rank', '0')
        subject = item.get('subject', '')
        self.data.append((title, rank, subject))
        if len(self.data) == 100:
            self._write_data()
        # sql = "insert into db_top_movie(title, rating, subject) values(%s, %s, %s)"
        # self.cursor.execute(sql, (title, rank, subject))
        return item

    def _write_data(self):
        sql = "insert into db_top_movie(title, rating, subject) values(%s, %s, %s)"
        self.cursor.executemany(sql, self.data)
        self.conn.commit()


class MySpiderPipeline:
    def __init__(self):
        self.wd = Workbook()
        self.ws = self.wd.active
        self.ws.title = "top250"
        self.ws.append(('标题', "评分", "主题"))

    # def open_spider(self):
    #     pass

    def close_spider(self, spider):
        self.wd.save("豆瓣电影top250.xlsx")

    def process_item(self, item, spider):
        title = item.get('title', '')
        rank = item.get('rank', '')
        subject = item.get('subject', '')
        self.ws.append((title, rank, subject))
        # self.ws.append((item['title'], item['rank'], item['subject']))
        return item
