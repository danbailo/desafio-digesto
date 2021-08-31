import csv
import json

from tabulate import tabulate

# Headers para as tabelas, no formato do enunciado do desafio
headers = ["CPU / VCPU","MEMORY","STORAGE / SSD DISK","BANDWIDTH / TRANSFER","PRICE [ $/mo ]"]

def print_data(data):
    """ Printa os dados na linha de comando """
    # Printa o header na tela, separando os dados por tabulação
    for k,v in data.items():
        print(k)
        temp_table = []
        for row in v:
            # Cria uma tabela para printar os dados de forma mais agradável para o usuário
            temp_table.append(list(row.values()))
        print(tabulate(temp_table, headers=headers, tablefmt="github"))
        print()

def save_csv(data): 
    """ Salva os dados coletados num arquivo .csv """
    with open("output/data.csv", "w") as file:        
        writer = csv.writer(file)
        # Grava o header no arquivo .csv
        writer.writerow(headers)
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
