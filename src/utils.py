import csv
import json

def print_data(data):
    print("CPU / VCPU\t\tMEMORY\t\tSTORAGE / SSD DISK\t\tBANDWIDTH / TRANSFER\t\tPRICE [ $/mo ]\n")
    for k,v in data.items():
        print(k)
        for row in v:            
            storage, cpu, memory, bandwidth, price = row.values()
            print(f"{storage}\t\t\t{cpu}\t\t\t{memory}\t\t\t{bandwidth}\t\t\t{price}")
        print()

def save_csv(data):
    with open("output/data.csv", "w") as file:        
        writer = csv.writer(file)
        writer.writerow("CPU / VCPU,MEMORY,STORAGE / SSD DISK,BANDWIDTH / TRANSFER,PRICE [ $/mo ]".split(","))
        for k,v in data.items():
            writer.writerow([k])
            for row in v:            
                writer.writerow(row.values())

def save_json(data):
    with open("output/data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4,)