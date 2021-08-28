import csv

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
        for row in data:
            writer.writerow(row)

def save_json():
    pass