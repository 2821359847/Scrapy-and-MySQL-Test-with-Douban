# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem

class DoubanSpiderSpider(scrapy.Spider):
    # 爬虫名
    name = 'douban_spider'
    # 允许的域名
    allowed_domains = ['movie.douban.com']
    # 入口Url
    start_urls = ['https://movie.douban.com/top250']

    # 默认解析方法
    def parse(self, response):
        movie_list = response.xpath("//div[@class='article']//ol[@class='grid_view']/li")
        for i_item in movie_list:
            douban_item = DoubanItem()
            douban_item['movie_seri'] = i_item.xpath(".//div[@class='item']//em/text()").extract_first()
            douban_item['movie_name'] = i_item.xpath(".//div[@class='info']/div[@class='hd']/a/span[1]/text()").extract_first()
            
            content= i_item.xpath(".//div[@class='info']/div[@class='bd']/p[1]/text()").extract()
            for i in content:
                content_s = "".join(i.split())
                douban_item["movie_into"] = content_s
            
            douban_item['movie_star'] = i_item.xpath(".//span[@class='rating_num']/text()").extract_first()
            douban_item['movie_eval'] = i_item.xpath(".//div[@class='star']/span[4]/text()").extract_first()
            douban_item['movie_desc'] = i_item.xpath(".//span[@class='inq']/text()").extract_first()
            print(douban_item)
            # 将数据 yield 到 pipeline 里去
            yield douban_item
        
        # 解析下一页
        next_link = response.xpath(".//span[@class='next']/link/@href").extract()
        if next_link:
            next_link = next_link[0]
            yield scrapy.Request("https://movie.douban.com/top250" + next_link, callback=self.parse)
        
