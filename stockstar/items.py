# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst

class StockstarItemLoader(ItemLoader):
    default_output_processor = TakeFirst()
class StockstarItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    code = scrapy.Field()  # 代码
    abbr = scrapy.Field()  # 简称
    # last_trade = scrapy.Field()  # 最新价
    # chg_ratio = scrapy.Field()  # 涨跌幅
    # chg_amt = scrapy.Field()    # 涨跌额
    # chg_ratio_5min = scrapy.Field()     # 5分钟涨幅
    # volumn = scrapy.Field()     # 成交量
    # turn_over = scrapy.Field()   # 成交额
    cir_val = scrapy.Field()  # 流通市值
    tot_val = scrapy.Field()    # 总市值
    cir_cap = scrapy.Field()    # 流通股本
    tot_cap = scrapy.Field()    # 总股本
    main_scope = scrapy.Field()  # 主营范围
    net_profit = scrapy.Field()   #净利润（万元）
