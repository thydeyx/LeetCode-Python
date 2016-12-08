# -*- coding:utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import Selector
from soufang.items import SoufangItem
from scrapy.http import Request
import threading


class SoufangSpider(CrawlSpider):

    name = 'soufang'
    allowed_domains = ['fang.com']
    start_urls = ["http://newhouse.fang.com/house/s/"]
    q = threading.Lock()
    #rules = [Rule(LinkExtractor(allow='http://[a-z]+\.fang\.com/?ctm=1'), 'parse_bj', follow=True)]


    def parse(self, response):
        sel = Selector(response)
        filename = "body"
        with open(filename, "wb") as f:
            f.write(response.body)

        urls = sel.xpath('//li/div/div/a/@href').extract()
        print "urls", urls, len(urls)
        page_num = 0

        for url in urls:
            print url
            try:
                request = Request(url, callback=self.parse_detail)
                self.q.acquire()
                page_num += 1
                request.meta['num'] = page_num
                self.q.release()
                yield request
            except Exception as e:
                log_text = "ERROR:" + url


    def parse_detail(self, response):

        sel = Selector(response)
        soufang = SoufangItem()
        page_num = response.meta['num']
        filename = "./page/peking" + str(page_num)

        soufang["url"] = response.url
        print "#" * 30
        print response.url
        print page_num
        print "#" * 30

       # print response.body
       # print "$" * 30

        title = sel.xpath('//div[@id="daohang"]/div/dl/dd/div/h1/a/text()').extract()
        if len(title) == 0:
            title = sel.xpath('//title/text()').extract()[0]
            title = title.strip().split("-")
            if len(title) != 0:
                print title[0].strip()
        else:
            title = title[0].strip()
            print title
        """
        with open(filename, "wb") as f:
            f.write(response.body)
        """

    def parse_bj(self, response):

        soufang = SoufangItem()
        soufang["url"] = response.url
        """
        soufang["url"] = response.url.split("/").split(".")[0]

        filename = response.url
        with open(filename, 'wb') as f:
            f.write(response.body)
        """
        """
        for item in response.xpath("//div[@class='nlc_details']"):

            soufang['position'] =
            soufang['avg_money'] =
            soufang['residence'] =

            soufang['residence'] = item.xpath("a/text()")
        """

        return soufang