# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 序号
    movie_seri = scrapy.Field()
    # 名字
    movie_name = scrapy.Field()
    # 介绍
    movie_into = scrapy.Field()
    # 星级
    movie_star = scrapy.Field()
    # 评论数
    movie_eval = scrapy.Field()
    # 描述
    movie_desc = scrapy.Field()
