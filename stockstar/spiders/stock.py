# -*- coding: utf-8 -*-
import scrapy

from ..items import StockstarItem,StockstarItemLoader

class StockSpider(scrapy.Spider):
    name = 'stock'
    # allowed_domains = ['quote.stockstar.com']
    start_urls = ['http://quote.stockstar.com/stock/industry_I_0_0_1.html']

    def parse(self, response):
        page = int(response.url.split("_")[-1].split(".")[0])
        item_nodes = response.css('#datalist tr')
        # company_links = response.css('#datalist tr td:nth-child(1) a::attr(href)')
        for item_node in item_nodes:
            company_link = 'http:' + item_node.css('td:nth-child(1) a::attr(href)').get()
            # scrapy.Request(url=company_link, meta={'item': StockstarItem()}, callback=self.parse_company)

            # item_loader = StockstarItemLoader(item=StockstarItem(),selector=item_node)
            #
            # item_loader.add_css("code", "td:nth-child(1) a::text")
            # item_loader.add_css("abbr", "td:nth-child(2) a::text")
            # item_loader.add_css("cir_val", "td:nth-child(3)::text")
            # item_loader.add_css("tot_val", "td:nth-child(4)::text")
            # item_loader.add_css("cir_cap", "td:nth-child(5)::text")
            # item_loader.add_css("tot_cap", "td:nth-child(6)::text")
            item = StockstarItem()
            code = "a"+item_node.css("td:nth-child(1) a::text").get()
            item['code'] = code
            item['abbr'] = item_node.css("td:nth-child(2) a::text").get()
            item['cir_val'] = item_node.css("td:nth-child(3)::text").get()
            item['tot_val'] = item_node.css("td:nth-child(4)::text").get()
            item['cir_cap'] = item_node.css("td:nth-child(5)::text").get()
            item['tot_cap'] = item_node.css("td:nth-child(6)::text").get()
            yield scrapy.Request(url=company_link, meta={'item': item}, callback=self.parse_company)
            # stock_item = item_loader.load_item()
            # yield stock_item
        if item_nodes:
            next_page = page+1
            next_url = response.url.replace("{0}.html".format(page),"{0}.html".format(next_page))
            yield scrapy.Request(url=next_url,callback=self.parse)
        # for company_link in company_links:
        #     yield scrapy.Request(url=company_link,meta={'item':StockstarItem},callback=self.parse_company)

    def parse_company(self, response):
        # item_loader = response.meta['item_loader']
        # item_loader['selector'] = response.text
        # response.xpath('//div[@class="title"]/div/ul/li/text()').getall()
        # item_loader.add_xpath("main_scope", "//div[@class='lr bg']/div/ul/li/text()")
        # stock_item = item_loader.load_item()
        item = response.meta['item']
        main_scope = response.xpath('//div[@class="lr bg"]/div/ul/li/text()').getall()

        # print("main_scope=    \n")
        # print(main_scope)
        item['main_scope'] = main_scope
        item['net_profit'] = response.xpath('//div[@class="con cwfx_wrap"]/div[3]/table/tr[8]/td[2]/text()').get()
        yield item


    # def get_company(self):
    #     yield scrapy.Request()

