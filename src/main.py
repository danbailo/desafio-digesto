from core.Scraper import Scraper
from utils import print_data, save_csv, save_json

if __name__ == "__main__":
    # Instância da classe Scraper, responsável por realizar a chamada dos métodos
    # para inicializar cada um dos scrapers
    scraper = Scraper()

    # Executa o Scraper 1
    print("Coletando dados do site Vultr...")
    scraper.vultr()
    print("Dados coletados com sucesso!\n")

    # Executa o Scraper 2
    print("Coletando dados do site HostGator...")
    scraper.hostgator()
    print("Dados coletados com sucesso!\n")

    # Menu de operações
    while True:
        print("Digite a opção desejada:")
        print("[1] --print")
        print("[2] --save_json")
        print("[3] --save_csv")
        print("[4] sair")
        op = input() # Armazena a opção selecionada pelo usuário
        print()

        if op == "1":
            # Printa os dados coletados para o usuário
            print_data(scraper.data)
            print()
        elif op == "2":
            # Salva os dados coletados num arquivo .json
            save_json(scraper.data)
            print("Arquivo .json gravado com sucesso no diretório /output na raiz do projeto!\n")            
        elif op == "3":
            # Salva os dados coletados num arquivo .csv
            save_csv(scraper.data)
            print("Arquivo .csv gravado com sucesso no diretório /output na raiz do projeto!\n")
        elif op == "4":
            break
