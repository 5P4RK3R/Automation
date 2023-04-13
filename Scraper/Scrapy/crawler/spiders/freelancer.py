import scrapy
import time
from traceback import format_exc
# from ..item import CrawlerItem
from ..items import FreelancerItem
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class FreelancerSpider(scrapy.Spider):
    name = 'freelancer'
    allowed_domains = ['freelancer.com']
    # allowed_domains = ['https://www.freelancer.com']
    start_urls = ['https://www.freelancer.com/jobs']

    def parse(self, response):
        try:
            # jobs = response.css('div.JobSearchCard-item')
            for job in response.css('div.JobSearchCard-item'):
                il = ItemLoader(item = FreelancerItem(),selector = job)

                il.add_css('title','a.JobSearchCard-primary-heading-link::text')
                il.add_css('desc','p.JobSearchCard-primary-description::text')
                # il.add_css('skills','span.ProjectTable-skills::text')
                # il.add_css('started','td.started-col::text')
                # il.add_css('entries','td.bids-col::text')
                il.add_css('price','div.JobSearchCard-secondary-price::text')

                yield il.load_item()
                # price = job.css('div.JobSearchCard-secondary-price::text')
                # title = job.css('a.JobSearchCard-primary-heading-link::text')
                # desc = job.css('p.JobSearchCard-primary-description::text')
                # skills = job.css('span.ProjectTable-skills a::attr(href)')
                # entries = job.css('div.bids-col-inner::text')
                # started = job.css('td.started-col::text')
                # yield {
                #     'title': title.get().strip() if title else "",
                #     'desc': desc.get().strip() if desc else "",
                #     'price': price.get().strip() if price else "",
                #     # 'skills': skills.get().strip() if skills else "",
                #     # 'entries': entries.get().strip() if entries else "",
                #     # 'started': started.get().strip() if started else "",
                # }

            # total_pages = int(response.css('#bottom-pagination a:last-child::attr(href)').get().strip('jobs/'))
            next_page = response.css('#bottom-pagination a:nth-last-child(2)::attr(href)').get()
            # next_page = int(response.css('#bottom-pagination a:nth-last-child(2)::attr(href)').get().strip('jobs/'))
            # page = int(response.css('ul.Breadcrumbs-list li:last-child span::text').get())
            # print("31test",next_page)
            # self.logger.info(f"31test,{total_pages},{next_page},{page}, {page is not total_pages}")
            # self.logger.info(f"total_pages {total_pages}")   
            if next_page is not None:
                self.logger.info("---------------Next Page------------")
                self.logger.info(response)
                self.logger.info(f"next_page {next_page}")
                next_page = response.urljoin(f"https://www.freelancer.com{next_page}")
                self.logger.info(f"next_page {next_page}")
                yield response.follow(next_page,callback = self.parse)     
            # if page is not total_pages:
            #     self.logger.info("---------------Next Page------------")
            #     self.logger.info(f"next_page {next_page}")
            #     next_page = response.urljoin(f"https://www.freelancer.com{next_page}")
            #     self.logger.info(f"next_page {next_page}")
            #     yield response.follow(next_page,callback = self.parse)
                # yield scrapy.Request(next_page, callback = self.parse)
        except:
            print(format_exc())
            self.logger.error(format_exc())

# class FreelanceSpider(CrawlSpider):
#     name = 'freelance'
#     allowed_domains = ['https://www.freelancer.com']
#     start_urls = ['https://www.freelancer.com/jobs']

#     rules = (
#         Rule(LinkExtractor(allow="jobs"),callback='parse_item'),
#     )
#     def parse_item(self, response):
#         try:
#             jobs = response.css('div.JobSearchCard-item')
#             for job in jobs:
#                 # il = itemLoader(item = CrawlerItem(),selector = job)

#                 # il.add_css('title','a.JobSearchCard-primary-heading-link::text')
#                 # il.add_css('desc','p.JobSearchCard-primary-description::text')
#                 # il.add_css('price','div.JobSearchCard-secondary-price::text')

#                 # yield il.load_item()
#                 price = job.css('div.JobSearchCard-secondary-price::text')
#                 title = job.css('a.JobSearchCard-primary-heading-link::text')
#                 desc = job.css('p.JobSearchCard-primary-description::text')
#                 yield {
#                     'title': title.get().strip() if title else "",
#                     'desc': desc.get().strip() if desc else "",
#                     'price': price.get().strip() if price else ""
#                 }

#             total_pages = int(response.css('#bottom-pagination a:last-child::attr(href)').get().strip('jobs/'))
#             next_page = response.css('#bottom-pagination a:nth-last-child(2)::attr(href)').get()
#             # next_page = int(response.css('#bottom-pagination a:nth-last-child(2)::attr(href)').get().strip('jobs/'))
#             page = int(response.css('ul.Breadcrumbs-list li:last-child span::text').get())
#             # print("31test",next_page)
#             self.logger.info(f"31test,{total_pages},{next_page},{page}, {page is not total_pages}")
#             self.logger.info(f"total_pages {total_pages}")   
#             if next_page is not None:
#                 self.logger.info("---------------Next Page------------")
#                 self.logger.info(response)
#                 self.logger.info(f"next_page {next_page}")
#                 next_page = response.urljoin(f"https://www.freelancer.com{next_page}")
#                 self.logger.info(f"next_page {next_page}")
#                 yield response.follow(next_page,callback = self.parse)     
#             # if page is not total_pages:
#             #     self.logger.info("---------------Next Page------------")
#             #     self.logger.info(f"next_page {next_page}")
#             #     next_page = response.urljoin(f"https://www.freelancer.com{next_page}")
#             #     self.logger.info(f"next_page {next_page}")
#             #     yield response.follow(next_page,callback = self.parse)
#                 # yield scrapy.Request(next_page, callback = self.parse)
#         except:
#             print(format_exc())

