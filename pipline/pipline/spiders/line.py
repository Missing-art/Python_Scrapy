import scrapy
from pipline.items import PiplineItem
#基于管道持久化存储的流程
    #数据解析
    #在item类中定义相关的属性
    #将解析的数据封装存储到item类型的对象中（首先要导入items中的类）
    #将item类型的对象提交给管道（piplines）进行持久化存储的操作
    #在管道类的process_item中要将其接受到的item对象中存储的数据进行持久化存储操作
    #在配置文件中开启管道

class LineSpider(scrapy.Spider):
    name = 'line'
   # allowed_domains = ['www.xxx.com']
    start_urls = ['file:///H:/GNSS数据处理/刘正/北斗星通/第一批/225/华测自动化检测报告-GPS.html']
    model_url = []
    types = ['GPS20度','GLO20度','GAL20度']
    for num in range(25,32):
          for type in types:
                url = f'file:///H:/GNSS数据处理/刘正/北斗星通/第一批/2{num}/华测自动化检测报告-{type}.html'
                model_url.append(url)

    def parse(self, response):
        for new_url in self.model_url:
              yield scrapy.Request(url=new_url,callback=self.mo_parse)
      #  content = ''.join(content)  将列表转为字符串
    def mo_parse(self,response):
        div_list = response.xpath('/html/body/div/div/div')
        check = div_list[1].xpath('./table//tr[3]/td[2]/text()').extract_first()
        date = div_list[2].xpath('./table//tr[2]/td[2]/text()').extract_first()
        system = div_list[2].xpath('./table//tr[8]/td[2]/text()').extract_first()
        angle = div_list[2].xpath('./table//tr[6]/td[2]/text()').extract_first()


        dataIntegrity_tr_list = div_list[-3].xpath('./table//tr')
        utilization_rate = dataIntegrity_tr_list[-1].xpath('./td[4]/div[1]/text()').extract_first()
        weekJumpRatio = dataIntegrity_tr_list[-1].xpath('./td[7]/text()').extract_first()
        jump = dataIntegrity_tr_list[-1].xpath('./td[6]/div[1]/text()').extract_first()

        noiseRatioInformation_tr = div_list[-1].xpath('./table//tr')
        l1 = noiseRatioInformation_tr.xpath('./td[3]/text()').extract_first()
        l2 = noiseRatioInformation_tr.xpath('./td[5]/text()').extract_first()
        l5 = noiseRatioInformation_tr.xpath('./td[7]/text()').extract_first()
        e5 = noiseRatioInformation_tr.xpath('./td[9]/text()').extract_first()
        e6 = noiseRatioInformation_tr.xpath('./td[11]/text()').extract_first()

        pseudoDistance_tr_list = div_list[3].xpath('./table//tr')
        mp1 = pseudoDistance_tr_list[-1].xpath('./td[2]/div[1]/text()').extract_first()
        mp2 = pseudoDistance_tr_list[-1].xpath('./td[5]/div[1]/text()').extract_first()
        mp3 = pseudoDistance_tr_list[-1].xpath('./td[8]/div[1]/text()').extract_first()
        mp4 = pseudoDistance_tr_list[-1].xpath('./td[11]/div[1]/text()').extract_first()
        mp5 = pseudoDistance_tr_list[-1].xpath('./td[14]/div[1]/text()').extract_first()

        if(l5 == "-"):
            l5 = 0
        if(e5 == "-"):
            e5=0
        if(e6 == "-"):
            e6=0
        if(weekJumpRatio == '99999999'):
            weekJumpRatio=999999
      #实例化一个item对象
        item = PiplineItem()
        item['check'] =check
        item['date'] = date
        item['system'] = system
        item['angle'] = angle
        item['utilization_rate'] = utilization_rate
        item['weekJumpRatio'] = weekJumpRatio
        item['jump'] = jump
        item['l1'] = l1
        item['l2'] = l2
        item['l5'] = l5
        item['e5'] = e5
        item['e6'] = e6
        item['mp1'] = mp1
        item['mp2'] = mp2
        item['mp3'] = mp3
        item['mp4'] = mp4 
        item['mp5'] = mp5
        #将item提交给管道
        yield item
