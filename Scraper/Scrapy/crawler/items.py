# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst, Join
from w3lib.html import remove_tags
from datetime import datetime, timedelta
import re
from dateutil.relativedelta import relativedelta


# Get the current date and time
current_datetime = datetime.now()

def get_digit(text):
    return re.findall(r': \d+',str(text))

def get_period(text):
    
    period = stripText(text).split(" ")[1]
    period = stripText(period)
    digit = int(stripText(text).split(" ")[0])
    print("texttest3",period,digit)
    if period == "weeks" or period == "week":
        period = current_datetime - timedelta(weeks=digit)
    if period == "month" or period == "months":
        period = current_datetime - relativedelta(months=digit)
    if period == "day" or period == "days":
        period = current_datetime - relativedelta(days=digit)
    if period == "hour" or period == "hours":
        period = current_datetime - relativedelta(hours=digit)

    return period
 


def stripText(text):
    return text.strip()
def joinText(text):
    return text.join()
def splitText(text):
    return text.split(":")[1]
def replaceText(text):
    return text.replace("Remote,","")

def splitComma(text):
    return text.split(",")[0]

def get_last_text(text):
    res = text.split("at")
    return res[len(res)-1]

class FreelancerItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field(input_processor = MapCompose(remove_tags,stripText),output_processor = TakeFirst())
    # link = scrapy.Field(input_processor = MapCompose(remove_tags,stripText),output_processor = TakeFirst())
    # raw_description = scrapy.Field(input_processor = MapCompose(remove_tags,stripText),output_processor = TakeFirst())
    price = scrapy.Field(input_processor = MapCompose(remove_tags,stripText),output_processor = TakeFirst())
    location = scrapy.Field(input_processor = MapCompose(remove_tags,stripText),output_processor = TakeFirst())
    description = scrapy.Field(input_processor = MapCompose(remove_tags,stripText),output_processor = TakeFirst())
    skills = scrapy.Field(input_processor = MapCompose(remove_tags,stripText),output_processor = TakeFirst())
    # skills = scrapy.Field(input_processor = MapCompose(remove_tags,stripText),output_processor = Join())
    # started = scrapy.Field(input_processor = MapCompose(remove_tags,stripText),output_processor = TakeFirst())
    # entries = scrapy.Field(input_processor = MapCompose(remove_tags,stripText),output_processor = TakeFirst())
    # pass

class RemoteItem(scrapy.Item):
    title = scrapy.Field(input_processor = MapCompose(remove_tags,stripText),output_processor = TakeFirst())
    company = scrapy.Field(input_processor = MapCompose(remove_tags,get_last_text,stripText),output_processor = TakeFirst())
    period = scrapy.Field(input_processor = MapCompose(remove_tags,stripText,get_period),output_processor = TakeFirst())
    category = scrapy.Field(input_processor = MapCompose(remove_tags),output_processor = TakeFirst())
    location = scrapy.Field(input_processor = MapCompose(remove_tags,splitText,replaceText,stripText),output_processor = TakeFirst())
    work_type = scrapy.Field(input_processor = MapCompose(remove_tags,splitText,splitComma,stripText),output_processor = TakeFirst())
    description = scrapy.Field(input_processor = MapCompose(remove_tags,stripText),output_processor = TakeFirst())
    raw_description = scrapy.Field(input_processor = MapCompose(stripText),output_processor = TakeFirst())
    raw_job_info = scrapy.Field(input_processor = MapCompose(stripText),output_processor = TakeFirst())
