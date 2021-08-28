def print_data(data):
    print(f"Storage\t\tCPU\t\tMemory\t\tBandwidth\tPrice/mo\n")
    for row in data:
        storage, cpu, memory, bandwidth, price = row
        print(f"{storage}\t\t{cpu}\t\t{memory}\t\t{bandwidth}\t\t{price}")

def save_csv():
    pass

def save_json():
    pass