# -*- coding: utf-8 -*-
import json
import codecs
# 以Json的形式存储
class JsonWithEncodingCnblogsPipeline(object):
    def __init__(self):
        self.file = codecs.open('douban.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()

# 将数据存储到mysql数据库
# from twisted.enterprise import adbapi
# import MySQLdb
# import MySQLdb.cursors
#
# class MySQLStorePipeline(object):
#     # 数据库参数
#     def __init__(self):
#         dbargs = dict(
#             host='127.0.0.1',
#             db='数据库名',
#             user='root',
#             passwd='root',
#             cursorclass=MySQLdb.cursors.DictCursor,
#             charset='utf8',
#             use_unicode=True
#         )
#         self.dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)
#
#     '''
#     The default pipeline invoke function
#     '''
#
#     def process_item(self, item, spider):
#         res = self.dbpool.runInteraction(self.insert_into_table, item)
#         return item
#
#     # 插入的表，此表需要事先建好
#     def insert_into_table(self, conn, item):
#         conn.execute('insert into douban(rank,title,rate,qute,link) values(%s,%s,%s,%s,%s)', (
#             item['rank'][0],
#             item['title'][0],
#             item['rate'][0],
#             item['quote'][0],
#             item['link'][0])
#                      )