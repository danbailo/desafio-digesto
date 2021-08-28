import csv
import json

def print_data(data):
    print(f"Storage\t\tCPU\t\tMemory\t\tBandwidth\tPrice/mo\n")
    for row in data:
        storage, cpu, memory, bandwidth, price = row
        print(f"{storage}\t\t{cpu}\t\t{memory}\t\t{bandwidth}\t\t{price}")

def save_csv(data):
    header = ["Storage", "CPU", "Memory", "Bandwidth", "Price/mo"]
    with open("output/data.csv", "w") as file:        
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)

def save_json(data):
    header = ["Storage", "CPU", "Memory", "Bandwidth", "Price/mo"]
    json_data = []
    with open("output/data.json", "w", encoding="utf-8") as file:
        for row in data:
            storage, cpu, memory, bandwidth, price = row
            json_data.append({"Storage":storage, "CPU":cpu, "Memory":memory, "Bandwidth":bandwidth, "Price/mo":price})
        json.dump(json_data, file, ensure_ascii=False, indent=4,)