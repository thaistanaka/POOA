from bs4 import BeautifulSoup
from ParserHtml.parserHtml import ParserHtml

class ParserHtmlUol(ParserHtml):
    
    # função que retorna os titulos de noticias da UOL
    def getTitles(self,htmlString):
        htmlParsed = BeautifulSoup(htmlString,'html.parser')
        titles = []
        titles.extend([item.get_text() for item in htmlParsed.find_all("h1",class_="titulo")])
        titles.extend([item.get_text() for item in htmlParsed.find_all("h2",class_="titulo color2 ")])
        titles.extend([item.get_text() for item in htmlParsed.find_all("h2",class_="titulo color2")])
        return titles