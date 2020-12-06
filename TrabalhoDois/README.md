# Trabalho 2: Princípio Aberto-Fechado

Ferramenta em Python para encontrar e baixar títulos das notícias do dia nos principais sites de notícias respeitando os princípios de responsbilidade única e aberto-fechado.\
Alunas: Thaís Oyamada Tanaka e Gabrielle Scaranello Faria

## Instalar Python e bibliotecas

[Python 3](https://www.python.org/downloads/)

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

python3 noticias.py [--siteUrl SITEURL] [--filename FILENAME] [--htmlname HTMLNAME] [--classname CLASSNAME]\
\
--siteUrl é um argumento opcional com valor default: "https://g1.globo.com/", é a URL do site de notícias.\
--filename é um argumento opcional com o nome do arquivo que será criado com os títulos de notícias. Caso este argumento não seja passado, os títulos serão impressos na tela.\
--htmlname é um argumento opcional com nome da estrutura html em que será buscado o titulo da notícia. Exemplo: p, a, h1. Apenas usado quando a URL do argumento --siteUrl não é da UOL ou do G1.\
--classname é um argumento opcional com nome da classe em que será buscado o titulo da notícia. Apenas usado quando a URL do argumento --siteUrl não é da UOL ou do G1.\

python3 noticias.py --help
```console
usage: noticias.py [-h] [--siteUrl SITEURL] [--filename FILENAME]
                   [--htmlname HTMLNAME] [--classname CLASSNAME]

optional arguments:
  -h, --help            show this help message and exit
  --siteUrl SITEURL
  --filename FILENAME
  --htmlname HTMLNAME
  --classname CLASSNAME
```

## Como incluir um novo site de notícias

Para incluir um novo site de notícias, basta passar a URL do novo site no argumento --siteUrl junto com os argumentos --htmlname e --classname. Estes dois últimos argumentos podem ser encontrados inspecionando o html do site de notícias. Para incluir um algoritmo para processar as notícias extraídas, basta utilizar a classe parserHtml no diretório ParserHtml para ter acesso as informações do site. A implementação dessas classes de processamento foi baseada no design pattern Strategy.