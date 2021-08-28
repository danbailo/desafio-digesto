from bs4 import BeautifulSoup
import requests

if __name__ == "__main__":
    target = "https://www.vultr.com/products/cloud-compute/#pricing"
    response = requests.get(target)
    soup = BeautifulSoup(response.text, "html.parser")
    data = []

    table = soup.find("div", attrs=({"data-animation-options": "type:pricingTable;customInit: true;"}))
    rows = table.find_all("div", attrs=({"class":"pt__row-content"}))
    for cel in rows:
        storage, cpu, memory, bandwidth, price = cel.find_all("strong")
        data.append((storage.text, cpu.text, memory.text, bandwidth.text, price.text))

    print(data)