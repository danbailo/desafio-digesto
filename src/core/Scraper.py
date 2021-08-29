from typing import Optional
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time


class Scraper:
    def __init__(self):
        self.data = {}
        self.data["VULTR"] = []
        self.data["DIGITAL_OCEAN"] = []

    def vultr(self):
        target = "https://www.vultr.com/products/cloud-compute/#pricing"
        response = requests.get(target)
        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find("div", attrs=({"data-animation-options": "type:pricingTable;customInit: true;"}))
        rows = table.find_all("div", attrs=({"class":"pt__row-content"}))
        for cel in rows:
            storage, cpu, memory, bandwidth, price_month = cel.find_all("strong")
            self.data["VULTR"].append({
                "CPU / VCPU": cpu.text, 
                "MEMORY": memory.text, 
                "STORAGE/SSD DISK": storage.text, 
                "BANDWIDTH / TRANSFER": bandwidth.text, 
                "PRICE [ $/mo ]": price_month.text})            

    def digital_ocean(self):
        #https://www.digitalocean.com/page-data/pricing/page-data.json
        target = "https://www.digitalocean.com/pricing#droplet"

        options = Options()
        options.headless=True
        driver = webdriver.Firefox(executable_path="./geckodriver", options=options)
        driver.get(target)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="heading"]/div[2]/div[1]/a[1]/div').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="heading"]/div[2]/div/div[1]/div[2]/div[2]').click()
        target_source = driver.page_source
        driver.close()
        driver.quit()
        
        soup = BeautifulSoup(target_source, "html.parser")
        table = soup.find("table", attrs={"class":"table is-scrollable css-fssu8e is-fullwidth is-striped"}).find("tbody")
        rows = table.find_all("tr")
        for row in rows:
            memory, vcpu, transfer, ssd, price_hour, price_month, register = row.find_all("td")
            self.data["DIGITAL_OCEAN"].append({
                "CPU / VCPU": vcpu.text, 
                "MEMORY": memory.text, 
                "STORAGE/SSD DISK": ssd.text, 
                "BANDWIDTH / TRANSFER": transfer.text, 
                "PRICE [ $/mo ]": price_month.text})