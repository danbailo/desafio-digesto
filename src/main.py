from core.Scraper import Scraper
from utils import print_data, save_csv, save_json

if __name__ == "__main__":
    scraper = Scraper()

    print("Coletando dados do site Vultr...")
    scraper.vultr()
    print("Dados coletados com sucesso!\n")

    print("Coletando dados do site Digital Ocean...")
    scraper.digital_ocean()
    print("Dados coletados com sucesso!\n")

    while True:
        print("Digite a opção desejada:")
        print("[1] --print")
        print("[2] --save_csv")
        print("[3] --save_json")
        print("[4] sair")
        op = int(input())
        print()

        if op == 1:
            print_data(scraper.data)
        elif op == 2:
            save_csv(scraper.data)
            print("Arquivo .csv gravado com sucesso!\n")
        elif op == 3:
            save_json(scraper.data)
            print("Arquivo .json gravado com sucesso!\n")
        else:
            break