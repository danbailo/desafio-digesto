import csv
import json


def print_data(data):
    """ Printa os dados na linha de comando """
    # Printa o header na tela, separando os dados por tabulação
    print("CPU / VCPU\t\tMEMORY\t\tSTORAGE / SSD DISK\t\tBANDWIDTH / TRANSFER\t\tPRICE [ $/mo ]\n")
    for k,v in data.items():
        # Printa os dados linha a linha na tela, divido por scraper
        print(k)
        for row in v:
            cpu, memory, storage, bandwidth, price_month = row.values()
            # Mostra os dados, separando os por tabulação
            print(f"{cpu}\t\t\t{memory}\t\t\t{storage}\t\t\t{bandwidth}\t\t\t{price_month}")
        print()

def save_csv(data):
    """ Salva os dados coletados num arquivo .csv """
    with open("output/data.csv", "w") as file:        
        writer = csv.writer(file)
        # Grava o header no arquivo .csv
        writer.writerow("CPU / VCPU,MEMORY,STORAGE / SSD DISK,BANDWIDTH / TRANSFER,PRICE [ $/mo ]".split(","))
        for k,v in data.items():
            # Grava os dados linha a linha no arquivo gerado, divido por scraper
            writer.writerow([k])
            for row in v:            
                writer.writerow(row.values())

def save_json(data):
    """ Salva os dados coletados num arquivo .json """
    with open("output/data.json", "w", encoding="utf-8") as file:
        # Grava o arquivo .json, convertendo o dicionário diretamente para .json
        json.dump(data, file, ensure_ascii=False, indent=4,)
