# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class QuotetuttorialPipeline:

    def __init__(self):

        self.connect()
        self.create_table()

    def process_item(self, item, spider):

        self.add_item(item)
        return item

    def connect(self):

        self.conn = sqlite3.connect('myquotes.db')
        self.curr = self.conn.cursor()

    def add_item(self,item):

        self.curr.execute("""
        insert into quotes_db values
        (?,?,?)
        """,(item['author'],','.join(item['tag']),item['quote']))

        self.conn.commit()

    def create_table(self):

        self.curr.execute(
        """
        create table IF NOT EXISTS quotes_db (
        author text,
        tag text,
        quote text
        );
         """)
        self.conn.commit()
