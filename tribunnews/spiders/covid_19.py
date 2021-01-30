import scrapy
from tribunnews.items import TribunnewsItem

class Covid19Spider(scrapy.Spider):
    name = 'covid-19'
    allowed_domains = ['tribunnews.com']
    start_urls = ['https://www.tribunnews.com/tag/covid-19?page=1']


    def parse(self, response)   
        pg = response.xpath('//*[@class="ptb15"]')

        for i in pg:
            links = i.xpath('.//a/@href').extract_first()+"?page=all"
            absolute_next_url = response.urljoin(links)
            yield scrapy.Request(absolute_next_url, callback=self.parse_page)
            
        page_number= 45-len(response.url)
        next_page_url = response.url[0:cek_len] + str(int(response.url[cek_len:]) +1)
        absolute_next_page_url= response.urljoin(next_page_url)
        
        
        yield scrapy.Request(absolute_next_page_url)
        

    def parse_page(self, response):
        items = TribunnewsItem()
        title = response.xpath('//*[@class="f50 black2 f400 crimson"]/text()').extract_first()
        time = response.xpath('//*[@class="mt10"]/time/text()').extract_first()
        content_array = response.xpath('//*[@class="side-article txt-article"]/p/text()').extract()

        content=""
        for i in range(len(content_array)):
            content += content_array[i]+' '

        print(content)
        tag_array = response.xpath('//*[@class="tagcloud3"]/a/text()').extract()
        tag=""
        for i in range(len(tag_array)):
               tag += tag_array[i]+', '
        items['link'] = response.url
        items['title'] = title
        items['time'] = time
        items['content'] = content
        items['tag'] = tag

        yield items
        return
        