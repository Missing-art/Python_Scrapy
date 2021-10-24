import scrapy


class DataSpider(scrapy.Spider):
    name = 'data'
    #allowed_domains = ['www.xxxxx.com']
    start_urls = ['file:///H:/GNSS数据处理/刘正/北斗星通/第一批/225/华测自动化检测报告-GPS.html']
    #定义一个通用的url模板
    url = 'file:///H:/GNSS数据处理/刘正/北斗星通/第一批/%d/华测自动化检测报告-%s.html'
    num = 255
    def parse(self, response):
        # 这里要注意一个小细节，xpath是没有办法访问tbody的，所以我们要在tbody的部分使用 // 直接进入tbody内部进行数据爬取
        div_list = response.xpath('/html/body/div/div/div')
        check = div_list[1].xpath('./table//tr[3]/td[2]/text()').extract_first()
        print(check)
    
            

               

            

            
        
