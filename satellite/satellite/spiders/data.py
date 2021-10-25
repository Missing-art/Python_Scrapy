import scrapy
#创建爬虫工程的指令：scrapy startproject xxxxname
#在工程文件中，创建爬虫文件的指令 scrapy gensipder name www.xxxxx.com
#执行爬虫文件指令：scrapy crawl 爬虫文件名

#在运行之前，要在setting文件中更改，robot协议改成false，然后加上 LOG_LEVEL=“ERROR”

class DataSpider(scrapy.Spider):
    #爬虫文件的名称：就是爬虫源文件的唯一标识
    name = 'data'
    #允许的域名：用来限定start_urls列表中哪些url可以进行请求发送
    #allowed_domains = ['www.xxxxx.com']
    #起始的url列表：该列表中存放的url会被scrapy自动进行请求发送
    start_urls = ['file:///H:/GNSS数据处理/刘正/北斗星通/第一批/225/华测自动化检测报告-GPS.html']
    #定义一个通用的url模板
    

    #在这个里面并不好用，一般来说都是靠递归来实现循环
    model_url = []
    types = ['GPS','GLO','GAL']
    for number in [25,26,27,28,29,30,31]:
        for i in types:
            url = f'file:///H:/GNSS数据处理/刘正/北斗星通/第一批/2{number}/华测自动化检测报告-{i}.html'
            model_url.append(url)
    print(len(model_url))
    #用作数据解析，请求成功后对应的响应对象
    def parse(self, response):
        # 这里要注意一个小细节，xpath是没有办法访问tbody的，所以我们要在tbody的部分使用 // 直接进入tbody内部进行数据爬取
#        div_list = response.xpath('/html/body/div/div/div')
#       check = div_list[1].xpath('./table//tr[3]/td[2]/text()').extract_first()
      #  print(check)
        for new_url in self.model_url:
            print(new_url)
            #利用回调函数，这里相当于一个循环设置，而回调的函数是由自己定义的方法，用于解析网页获取数据
            yield scrapy.Request(url=new_url,callback=self.parse_model)
#        if self.num < 32:
#           new_url = format(self.url%self.num)
#           print(new_url)
#        yield scrapy.Request(url=new_url,callback=self.parse)

    def parse_model(self,response):

        #这边是基于终端指令的存储
            #指令： scrapy crawl filename -o '文件保存的路径及格式'（'./data.csv'）
        dics=[]
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

        dic={
            "角度":angle,
            "日期":date.split(" ")[0],
            "检验":check,
            "系统":system[0:3],
            "利用率":utilization_rate.strip('%'),
            "周跳变":weekJumpRatio,
            "跳变":jump,
            "MP1":mp1,
            "MP2":mp2,
            "MP3":mp3,
            "MP4":mp4,
            "MP5":mp5,
            "SNR(L1/B1/E1)":l1,
            "SNR(L2/B2/G2/E5a)":l2,
            "SNR(L5/B3/G3/E5b)":l5,
            "SNR(E5)":e5,
            "SNR(E6)":e6,
        }
        dics.append(dic)
        return dics

           
    
            

               

            

            
        
