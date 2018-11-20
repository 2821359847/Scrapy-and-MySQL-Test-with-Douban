# -*- coding: utf-8 -*-
import pymysql
from douban.settings import mysql_i, mysql_u, mysql_p, mysql_d, mysql_t

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanPipeline(object):
    def __init__(self):
        ip = mysql_i
        username = mysql_u
        password = mysql_p
        database = mysql_d
        table = mysql_t

        self.db = pymysql.connect(ip ,username, password, database)
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        sql = "INSERT INTO DOUBAN(SERI, NAME, INTR, STAR, EVAL, DESR) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')".format(\
        item["movie_seri"], item["movie_name"], item["movie_into"], item["movie_star"], item["movie_eval"], item["movie_desc"])
        
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
        except:
            # 如果发生错误则回滚
            self.db.rollback()

        return item
