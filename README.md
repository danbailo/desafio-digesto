# Desafio Digesto

Este projeto consiste na criação de dois scrapers para realizar a coleta de dados de dois websites, [Vultr](https://www.vultr.com/products/cloud-compute/#pricing) e [HostGator](https://www.hostgator.com/vps-hosting). Assim que o programa for executado, os dois scrapers serão inicializados e os dados coletados serão dispostos de três formas, na linha de comando, num arquivo `.csv` ou num arquivo `.json`.

*Enunciado do desafio: [Desafio Digesto Backend Python-5.pdf](./Desafio_Digesto_Backend_Python-5.pdf)*

## Pré-requisítos

* `python >= 3.8.10`
* `pip >= 21.2.4 `

## Instalação

Basta abrir um terminal/prompt de comando na raiz do projeto e executar o seguinte comando:

    python3 -m pip install -r requirements.txt --user

## Como usar

Basta abrir um terminal/prompt de comando na raiz do projeto e executar o seguinte comando:

    python3 src/main.py

Assim que o programa for executado, basta interagir entre as opções desejadas.

## Resultados

* Opção 1 - Disposição dos dados via CLI.
    * ![](img/cli_data.png)

* Opção 2 - Preview do arquivo `.json`, o mesmo pode ser encontrado no diretório [/output/](./output/), ou clicando [aqui](./output/data.json)    
    * ![](img/json_preview.png)

* Opção 3 - Preview do arquivo `.csv`, o mesmo pode ser encontrado no diretório [/output/](./output/), ou clicando [aqui](./output/data.csv)
    * ![](img/csv_preview.png)

## Comentários e Observações

Inicialmente, o segundo scraper tinha como site alvo [https://www.digitalocean.com/pricing/#droplet](https://www.digitalocean.com/pricing/#droplet), porém, aparentemente o mesmo sofreu algumas alterações na estrutura do código fonte desde a data que este desafio foi proposto pela primeira vez (20/01/2021), e atualmente, para realizar o scrape do mesmo, é necessário a utilização do Selenium, mas um dos requisitos do desafio é não utilizar esse framework. Entrei em contato com o desenvolvedor que me enviou a proposta via email e o mesmo me encaminhou o novo site alvo e disse para usar o este no lugar da DigitalOcean, dessa forma foi possível continuar o desafio respeitando as regras impostas.

Porém, de qualquer forma, eu havia desenvolvido o scraper para o mesmo utilizando o Selenium de forma parcial, pois neste momento eu estava aguardando resposta do email em que eu havia entrado em contato. O mesmo foi removido do código principal, mas pode ser conferido no commit [449f5c412de12ee463df1a4c8c82dbefd5d78823](https://github.com/danbailo/digesto-challenge/commit/449f5c412de12ee463df1a4c8c82dbefd5d78823).

---

Sempre que vou desenvolver um crawler/scraper, procuro encapsular e organizar a estrutura alvo num bloco de código. Essa lógica foi utilizada para implementar os dois scrapers presente neste trabalho. Isso garante que nenhuma informação fora desse bloco será coletada, ou seja, não haverá "sujeira" entre os dados e a forma de manipula-los fica mais fácil.

No scraper do [Vultr](https://www.vultr.com/products/cloud-compute/#pricing), os dados estavam dispostos numa tabela, com isso, eu primeiro isolei a tabela alvo, isto é, a tabela que contém os dados que serão coletados, e depois os organizei em linhas. 
```python
table = soup.find("div", attrs={"class": "pt__body js-body"})
rows = table.find_all("div", attrs={"class":"pt__row-content"})
```

No scraper do [HostGator](https://www.hostgator.com/vps-hosting) os dados estavam dispostos em cartões, logo, isolei o bloco de código onde os cartões se encontravam e chamei esse objeto de container. Com isso, instanciei um novo objeto para deixar de forma orgazinada os dados informativos do servidor com o preço mensal, pois os mesmos se encontravam em blocos diferentes!
```python
container = soup.find("section", attrs={"class":"pricing-card-container false undefined", "class": "pricing-card-container"})
price_cards = []
for price_card_container in container:
    price_cards.append((price_card_container.find("div", attrs={"class": re.compile("(pricing-card)")}),
                        price_card_container.find("p", attrs={"class":"pricing-card-price"})))
```

Quando os dados estão de forma organizada numa estrutura, a coleta e manipulação dos mesmos fica mais facil. Essa foi uma breve explicação da lógica utilizada para o desenvolvimento do mesmo

## Agradecimentos

Obrigado pela oportunidade de mostrar meu trabalho.