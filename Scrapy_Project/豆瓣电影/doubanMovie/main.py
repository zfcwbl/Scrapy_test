from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

'''通过这个文件启动爬虫，可以进行调试'''
if __name__=='__main__':
    process=CrawlerProcess(get_project_settings())
    process.crawl('doubanmovie')
    process.start()

