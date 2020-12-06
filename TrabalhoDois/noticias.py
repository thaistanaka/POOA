#o que pode ser passado pela linha de comando:
# OPCIONAIS
    # SITEURL = site em que será buscada as noticias, tem como padrão o G1
        # por exemplo, https://www.globo.com/

    # FILENAME = nome em que o arquivo csv será salvo, tem como
    # padrão o nome "news-ANO-MES-DIA-HORA-MINUTO.csv"
        # por exemplo, noticia.csv
import argparse
from ParserHtml.parserHtmlG1 import ParserHtmlG1
from ParserHtml.parserHtmlUol import ParserHtmlUol
from file import File
from htmlSite import HtmlSite

# função que organiza os argumentos passados por linha de comando       
def argParser(listArgs):
    parser = argparse.ArgumentParser()
    for arg in listArgs:
        parser.add_argument("--"+arg)
    return parser.parse_args()

# função que imprime os titulos das noticias        
def printTitles(titles):
    for item in titles:
        print(item)
        
listArgs = ["siteUrl","filename"]
args = argParser(listArgs)
titles = []

# caso a URL não seja passada, default: G1
if args.siteUrl is None:
    html = HtmlSite()
else:
    html = HtmlSite(args.siteUrl)

if html.siteUrl == "https://g1.globo.com/":
    titlesG1 = ParserHtmlG1()
    # retorna os titulos das noticias
    titles.extend(titlesG1.getTitles(html.getHtml()))
    if args.filename is None:
        # caso não tenha sido passado nome de arquivo, imprime os titulos na tela
        printTitles(titles)
    else:
        fileCsv = File(titles,args.filename)
        fileCsv.writeFile()
elif html.siteUrl == "https://www.uol.com.br/":
    titlesUol = ParserHtmlUol()
    titles.extend(titlesUol.getTitles(html.getHtml()))
    if args.filename is None:
        printTitles(titles)
    else:
        fileCsv = File(titles,args.filename)
        fileCsv.writeFile()
else:
    print("Site de notícias não suportado pela ferramenta!")
    print("Crie uma classe parserHtml nova usando BeautifulSoup para processar as notícias.")