#o que pode ser passado pela linha de comando:
# OPCIONAIS
    # SITEURL = site em que será buscada as noticias, tem como padrão o G1
        # por exemplo, https://www.globo.com/

    # FILENAME = nome em que o arquivo csv será salvo, tem como
        # padrão o nome "news-ANO-MES-DIA-HORA-MINUTO.csv"
        # por exemplo, noticia.csv
    # HTMLNAME = nome da estrutura html em que será buscado o titulo da noticia
        # caso a URL não seja do G1, nem da UOL
        # exemplo: a, p, div
    # CLASSNAME = nome da classe em que será buscado o titulo da noticia
        # caso a URL não seja do G1, nem da UOL
        # exemplo: "titulo"
from ParserHtml.parserHtmlG1 import ParserHtmlG1
from ParserHtml.parserHtmlUol import ParserHtmlUol
from ParserHtml.parserHtmlNew import ParserHtmlNew
from file import File
from htmlSite import HtmlSite
from argParser import argParser
from printTitles import printTitles

# lista de argumentos opcionais        
listArgs = ["siteUrl","filename","htmlname","classname"]
args = argParser(listArgs)
titles = []
urls = []

# caso a URL não seja passada, default: G1
if args.siteUrl is None:
    html = HtmlSite()
else:
    html = HtmlSite(args.siteUrl)

if html.siteUrl == "https://g1.globo.com/":
    titlesG1 = ParserHtmlG1()
    # retorna os titulos das noticias
    titles.extend(titlesG1.getTitles(html.getHtml()))
    urls.extend(titlesG1.getUrls(html.getHtml()))
    if args.filename is None:
        # caso não tenha sido passado nome de arquivo, imprime os titulos na tela
        printTitles(titles)
    else:
        fileCsv = File(titles,urls,html.siteUrl,args.filename)
        fileCsv.writeFile()
elif html.siteUrl == "https://www.uol.com.br/":
    titlesUol = ParserHtmlUol()
    titles.extend(titlesUol.getTitles(html.getHtml()))
    if args.filename is None:
        printTitles(titles)
    else:
        fileCsv = File(titles,urls,html.siteUrl,args.filename)
        fileCsv.writeFile()
elif args.htmlname is None or args.classname is None:
    # caso não seja a URL do G1, nem do UOL e não tenham sido passados os argumentos htmlname e classname
    print("Site de notícias não suportado pela ferramenta!")
    print("Crie uma classe parserHtml nova usando BeautifulSoup para processar as notícias.")
else:
    # processamento de noticias de um novo site
    dataSite = ParserHtmlNew(args.htmlname,args.classname)
    titles.extend(dataSite.getTitles(html.getHtml()))
    urls.extend(dataSite.getUrls(html.getHtml()))
    if args.filename is None:
        printTitles(titles)
    else:
        fileCsv = File(titles, urls, html.siteUrl, args.filename)
        fileCsv.writeFile()