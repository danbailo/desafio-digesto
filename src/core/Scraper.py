import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

import re


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

        # Tabela alvo, onde contém todos os dados que serão coletados
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

    def digital_ocean(self):
        """ Scraper 2 - Método responsável por coletar dados da segunda página algo - DigitalOcean """
        target = "https://www.digitalocean.com/pricing#droplet"

        # Configuração do Selenium
        options = Options()

        # Atributo onde faz o navegador rodar em segundo plano
        options.headless=True
        driver = webdriver.Firefox(executable_path="./geckodriver", options=options)
        driver.get(target)
        
        # "Scrolla" o cursor do navegador para até a parte final do site, para que assim o mesmo
        # carregue todo conteúdo disponível
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        # Tempo de espera implícito - necessário para que garanta que o conteúdo foi carregado
        # O tempo pode variar de acordo com a velocidade de conexão da rede
        time.sleep(1)
        
        # Procura o elemento responsável por mostrar as apresentar os dados e clica no mesmo, dessa forma
        # é possível ver o conteúdo no código fonte
        driver.find_element_by_xpath('//*[@id="heading"]/div[2]/div[1]/a[1]/div').click()

        # Tempo de espera implícito - necessário para garantir que o conteúdo após o click foi carregado
        time.sleep(1)

        # Procura o elemento responsável por mudar a forma de visualização da tabela, alterando
        # para a forma de linhas e colunas, fazendo com que fique mais simples a extração de dados
        driver.find_element_by_xpath('//*[@id="heading"]/div[2]/div/div[1]/div[2]/div[2]').click()

        # Variável que armazena o código fonte do site atual, isto é, o source que o navegador "vê".
        # Essa página é de fato a página alvo que contém os dados que serão coletados.
        target_source = driver.page_source

        # Fecha o navegador que está rodando em segundo plano
        driver.close()
        driver.quit()
        
        # Instância para realizar o parser do HTML e assim realizar a coleta dos dados
        soup = BeautifulSoup(target_source, "html.parser")

        # Tabela alvo, onde contém todos os dados que serão coletados
        table = soup.find("table", attrs={"class":"table is-scrollable css-fssu8e is-fullwidth is-striped"}).find("tbody")

        # Linhas da tabela
        rows = table.find_all("tr")
        for row in rows:
            # Dados coletados e armazenados somente os que interessam ao projeto
            memory, vcpu, transfer, ssd, price_hour, price_month, register = row.find_all("td")
            self.data["DIGITAL_OCEAN"].append({
                "CPU / VCPU": vcpu.text, 
                "MEMORY": memory.text, 
                "STORAGE/SSD DISK": ssd.text, 
                "BANDWIDTH / TRANSFER": transfer.text, 
                "PRICE [ $/mo ]": price_month.text})

    def hostgator(self):
        """ Scraper 3 - Método responsável por coletar dados da terceira página algo - HostGator """

        target = "https://www.hostgator.com/vps-hosting"
        response = requests.get(target)
        soup = BeautifulSoup(response.text, "html.parser")
        container = soup.find("section", attrs={"class":"pricing-card-container false undefined", "class": "pricing-card-container"})

        price_cards = []
        for price_card_container in container:
            price_cards.append((price_card_container.find("div", attrs={"class": re.compile("(pricing-card)")}), price_card_container.find("p", attrs={"class":"pricing-card-price"})))

        for price_card in price_cards:
            result = price_card[0].find_all("li", attrs={"class":"pricing-card-list-items"})
            if result:
                ram, vcpu, storage, bandwidth = price_card[0].find_all("li", attrs={"class":"pricing-card-list-items"})
                self.data["HOSTGATOR"].append({
                    "CPU / VCPU": re.sub(r'[^\x00-\x7f]',r'', vcpu.text), 
                    "MEMORY": re.sub(r'[^\x00-\x7f]',r'', ram.text), 
                    "STORAGE/SSD DISK": re.sub(r'[^\x00-\x7f]',r'', storage.text), 
                    "BANDWIDTH / TRANSFER": re.sub(r'[^\x00-\x7f]',r'', bandwidth.text), 
                    "PRICE [ $/mo ]": re.sub(r'[^\x00-\x7f]',r'', price_card[1].text)})
        print(self.data)

if __name__ == "__main__":
    scraper = Scraper()

    scraper.hostgator()

