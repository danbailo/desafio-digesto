import re
import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def rmv_hexadecimal_char(string):
    """ Remove caracteres hexadecimais de uma string """
    return re.sub(r'[^\x00-\x7f]',r'', string)


class Scraper:
    def __init__(self):
        """ Classe responsável por inicializar os scrapers """
        
        # Atributo para armazenar os dados coletados de forma individual para cada scraper
        self.data = {}
        self.data["VULTR"] = []
        self.data["DIGITAL_OCEAN"] = []
        self.data["HOSTGATOR"] = []

    def vultr(self):
        """ Scraper 1 - Método responsável por coletar dados da primeira página algo - Vultr """
        target = "https://www.vultr.com/products/cloud-compute/#pricing"

        # Realiza o request para obter a página HTML
        response = requests.get(target)

        # Instância para realizar o parser do HTML e assim realizar a coleta dos dados
        soup = BeautifulSoup(response.text, "html.parser")

        # Tabela alvo, bloco onde contém todos os dados que serão coletados
        table = soup.find("div", attrs={"class": "pt__body js-body"})

        # Linhas da tabela
        rows = table.find_all("div", attrs={"class":"pt__row-content"})
        for cel in rows:
            # Variáveis que contém os dados são organizadas para serem armazenadas
            # no atributo de dados da classe
            storage, cpu, memory, bandwidth, price_month = cel.find_all("strong")
            self.data["VULTR"].append({
                "CPU / VCPU": cpu.text, 
                "MEMORY": memory.text, 
                "STORAGE/SSD DISK": storage.text, 
                "BANDWIDTH / TRANSFER": bandwidth.text, 
                "PRICE [ $/mo ]": price_month.text})            

    def hostgator(self):
        """ Scraper 2 - Método responsável por coletar dados da terceira página algo - HostGator """
        target = "https://www.hostgator.com/vps-hosting"        

        # Realiza o request para obter a página HTML
        response = requests.get(target)

        # Instância para realizar o parser do HTML e assim realizar a coleta dos dados
        soup = BeautifulSoup(response.text, "html.parser")

        # Container alvo, bloco onde contém todos os dados que serão coletados
        container = soup.find("section", attrs={"class":"pricing-card-container false undefined", "class": "pricing-card-container"})

        # Os cartões onde os dados estão contidos são isolados de forma individual,
        # aqui também já é o coletado o preço mensal de cada máquina
        price_cards = []
        for price_card_container in container:
            # Lista de tuplas contendo o bloco do cartão onde estão as informações da máquina e o preço da mensal da mesma
            price_cards.append((price_card_container.find("div", attrs={"class": re.compile("(pricing-card)")}),
                                price_card_container.find("p", attrs={"class":"pricing-card-price"})))

        # Após os dados serem isolados de forma estruturada, foi desenvolvido a lógica para procurar
        # os valores apenas onde existia um resultado válido. Dessa forma os dados foram
        # coletados e armazenados no atributo de dados
        for price_card in price_cards:
            result = price_card[0].find_all("li", attrs={"class":"pricing-card-list-items"})
            if result:
                ram, vcpu, storage, bandwidth = price_card[0].find_all("li", attrs={"class":"pricing-card-list-items"})
                self.data["HOSTGATOR"].append({
                    "CPU / VCPU": rmv_hexadecimal_char(vcpu.text), 
                    "MEMORY": rmv_hexadecimal_char(ram.text), 
                    "STORAGE/SSD DISK": rmv_hexadecimal_char(storage.text), 
                    "BANDWIDTH / TRANSFER": rmv_hexadecimal_char(bandwidth.text), 
                    "PRICE [ $/mo ]": rmv_hexadecimal_char(price_card[1].text)})
