# Trabalho 2: Princípio Aberto-Fechado

Ferramenta em Python para encontrar e baixar títulos das notícias do dia nos principais sites de notícias respeitando os princípios de responsbilidade única e aberto-fechado.\
Alunas: Thaís Oyamada Tanaka e Gabrielle Scaranello Faria

## Instalar Python e bibliotecas

[Python 3](https://www.python.org/downloads/)\

em Ubuntu:
```console
sudo apt update
sudo apt install python3-pip
```

[urllib.request](https://docs.python.org/3/library/urllib.request.html)\
[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)\
[codecs](https://docs.python.org/3/library/codecs.html)\
[argparse](https://docs.python.org/3/library/argparse.html)

## Como executar

python3 noticias.py [--siteUrl SITEURL] [--filename FILENAME]\
\
--siteUrl é um argumento opcional com valor default: "https://g1.globo.com/", é a URL do site de notícias.\
--filename é um argumento opcional com o nome do arquivo que será criado com os títulos de notícias. Caso este argumento não seja passado, os títulos serão impressos na tela.

## Como incluir um novo site de notícias

Para incluir um novo site de notícias, basta trocar a URL no argumento --siteUrl. Para processar as notícias de um novo site, é preciso criar uma nova classe ParserHtmlNovoSite() e extrair as informações com o uso da biblioteca BeautifulSoup. 