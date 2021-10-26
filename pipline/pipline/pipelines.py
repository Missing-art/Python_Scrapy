# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv

class PiplinePipeline:
    #重写父类的一个方法，该方法只在开始爬虫的时候被调用一次
    def open_spider(self,spider):
        print("开始爬虫")
        #打开数据写入的文件
        self.file = open('./data.csv','w',encoding='utf-8',newline='')
        #设置数据写入的格式
        self.csvwriter = csv.writer(self.file)
        self.csvwriter.writerow(['检验','日期'])
        
    #    self.csvwriter.writerow(['检验','日期'])
    #专门用来处理item对象
    #该方法用来接受爬虫文件提交过来的item对象
    #该方法每接受到一个item就要被调用一次
    def process_item(self, item, spider):
        #获取到数据
        check = item['check']
        date = item['date']
        self.csvwriter.writerow([item['check'],item['date'].split(' ')[0]])
        return item
    def close_spider(self,spider):
        print("爬虫结束")
        self.file.close()
