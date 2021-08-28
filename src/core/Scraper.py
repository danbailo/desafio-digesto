import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self):
        self.data = []

    def vultr(self):
        target = "https://www.vultr.com/products/cloud-compute/#pricing"
        response = requests.get(target)
        soup = BeautifulSoup(response.text, "html.parser")

        table = soup.find("div", attrs=({"data-animation-options": "type:pricingTable;customInit: true;"}))
        rows = table.find_all("div", attrs=({"class":"pt__row-content"}))
        for cel in rows:
            storage, cpu, memory, bandwidth, price = cel.find_all("strong")
            self.data.append({"Storage":storage.text, "CPU":cpu.text, "Memory":memory.text, "Bandwidth":bandwidth.text, "Price/mo":price.text})

