import scrapy
from ..items import RefresherItem

class RspiderSpider(scrapy.Spider):
    name = "rSpider"
    # allowed_domains = ["jiji.com"]
    # start_urls = ["https://jiji.com.gh/computer-monitors"]
    # allowed_domains = ["https://www.olgomotors.co.nz"]
    start_urls = ["https://www.olgomotors.co.nz/vehicles?Make=&Text=&PriceFrom=0&PriceTo=0&YearFrom=0&YearTo=0&Transmission=&BodyStyle=&Dealership=&SortOption=0&Page=1&EngineSizeFrom=0&EngineSizeTo=0&OdometerFrom=0&OdometerTo=0&Model=&VehicleType=Used&IgnoreContext=&ExtColor1=&DoorNo=&FuelType1=&SearchType="]

    def parse(self, response):
        # Get urls on page
        relative_urls = response.css("div.cell-photo a::attr(href)").getall()
        for url in relative_urls:
            absolute_url = response.urljoin(url)
            yield response.follow(absolute_url, callback=self.parse_car)
        

        
    def parse_car(self, response):
        item = RefresherItem()

        # # Get the Cars
        # cars = response.css("li.vehicle")
        # for car in cars:
            # Get the Car's URL
        item["car_url"] = response.css("a::attr(href)").get()
        
        item["name"] = response.css("div.title h1::text").get()
        item["year"] = response.css("div.title h1::text").get().split()[0]

        item["price"] = response.css("span.price::text").get()

        # Specs bar
        data = response.css("div.title-price-wrap+div div.row")
        for spec in data:
            if spec.css("div.title::text").get()  == "Body":
                # 4 Door, Sedan
                item["body"] = spec.css("div.title+div.columns::text").get().split(",")[0]

            # Odometer
            elif (spec.css("div.title::text").get() == "Odometer"):
                item["odometer"] = spec.css("div.title+div.columns::text").get()

            # Interior Color
            elif (spec.css("div.title::text").get() == "Ext Colour"):
                item["interior_color"] = spec.css("div.title+div.columns::text").get()

            # Exterior Color
            elif (spec.css("div.title::text").get() == "Int Colour"):
                item["exterior_color"] = spec.css("div.title+div.columns::text").get()
                
                # Engine size
            elif (spec.css("div.title::text").get() == "Engine Size"):
                item["engine"] = spec.css("div.title+div.columns::text").get()

                # Fuel
            elif (spec.css("div.title::text").get() == "Fuel Type"):
                item["fuel"] = spec.css("div.title+div.columns::text").get()

                # Transmission
            elif (spec.css("div.title::text").get() == "Transmission"):
                item["transmission"] = spec.css("div.title+div.columns::text").get()
            
            # engine_size = 
        yield item

