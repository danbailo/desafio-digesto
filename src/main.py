from bs4 import BeautifulSoup
import requests
from utils import print_data, save_csv, save_json
import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--print', action="store_const", const=print_data, dest="cmd")
    parser.add_argument('--save_csv', action="store_const", const=save_csv, dest="cmd")
    parser.add_argument('--save_json', action="store_const", const=save_json, dest="cmd")
    args = parser.parse_args()

    target = "https://www.vultr.com/products/cloud-compute/#pricing"
    response = requests.get(target)
    soup = BeautifulSoup(response.text, "html.parser")
    data = []

    table = soup.find("div", attrs=({"data-animation-options": "type:pricingTable;customInit: true;"}))
    rows = table.find_all("div", attrs=({"class":"pt__row-content"}))
    for cel in rows:
        storage, cpu, memory, bandwidth, price = cel.find_all("strong")
        data.append({"Storage":storage.text, "CPU":cpu.text, "Memory":memory.text, "Bandwidth":bandwidth.text, "Price/mo":price.text})

    args.cmd(data)