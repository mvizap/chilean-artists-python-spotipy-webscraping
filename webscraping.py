
import scrapy
import pandas as pd
# Import the CrawlerProcess: for running the spider
from scrapy.crawler import CrawlerProcess


# Create the Spider class
class Popular_Music_Spider(scrapy.Spider):
  name = "popular_music_spider"
  
  # start_requests method
  def start_requests(self):
    yield scrapy.Request(url = 'https://www.musicapopular.cl/page/595/?s', callback = self.parse_pages)

  # First parsing method
  def parse_pages(self, response):
    titles = response.xpath("//article/h2/a/text()").extract()
    links_to_follow = response.css(" a.nextpostslink::attr(href)").extract()
    for title in titles:
      artists.append(title)
      print(title)
    for url in links_to_follow:
      yield response.follow(url = url,
                            callback = self.parse_pages)
 

    

artists = []
# Run the Spider
process = CrawlerProcess()
process.crawl(Popular_Music_Spider)
process.start()

ws = pd.DataFrame(artists, columns=['nombre'])
ws.to_csv('data/ws.csv',index=False)
      



