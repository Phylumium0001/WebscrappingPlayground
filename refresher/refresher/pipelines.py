# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class RefresherPipeline:
    def process_item(self, item, spider):
        item['exterior_color'] = item['exterior_color'].strip().replace("\r\n","")
        item['name'] = item['price'].strip().replace("\r\n","")
        item["odometer"] = item["odometer"].strip().replace("\r\n","")
        item["transmission"] = item["transmission"].strip().replace("\r\n","")
        return item
