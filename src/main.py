from bs4 import BeautifulSoup
import requests
import re


if __name__ == "__main__":
    target = "https://www.vultr.com/products/cloud-compute/#pricing"
    response = requests.get(target)
    soup = BeautifulSoup(response.text, "html.parser")

    table = soup.find("div", attrs=({"data-animation-options": "type:pricingTable;customInit: true;"}))
    rows = table.find_all("div", attrs=({"class":"pt__row-content"}))
    for cel in rows:
        print(cel.find_all("strong"))