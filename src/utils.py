import csv
import json

def print_data(data):
    print(f"Storage\t\tCPU\t\tMemory\t\tBandwidth\tPrice/mo\n")
    for row in data:
        storage, cpu, memory, bandwidth, price = row.values()
        print(f"{storage}\t\t{cpu}\t\t{memory}\t\t{bandwidth}\t\t{price}")

def save_csv(data):
    with open("output/data.csv", "w") as file:        
        writer = csv.writer(file)
        writer.writerow(data[0].keys())
        for row in data:
            writer.writerow(row.values())

def save_json(data):
    with open("output/data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4,)