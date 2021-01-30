# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import mysql.connector
from tribunnews.items import TribunnewsItem


class TribunnewsPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            passwd = '',
            database = 'tugasakhir'
        )
        self.curr= self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS tribunnews""")
        self.curr.execute("""create table tribunnews(
                                title varchar(255) NOT NULL PRIMARY KEY,
                                url text,
                                time text,
                                content text,
                                tag text)
                          """)

    def process_item(self,item,spider):
        self.store_db(item)
        return item

    #maaf kalau ada duplplikasi data
    def store_db(self,item):
        self.curr.execute("""insert into tribunnews
             select * from (select %s,%s,%s,%s,%s ) AS tmp 
             where not exists (
                 select title from kompas where title = %s
             ) LIMIT 1;""",(
            item['title'],
            item['link'],
            item['time'],
            item['content'],
            item['tag'] ,
            item['title']
        ))
        

        self.conn.commit()
