from bs4 import BeautifulSoup
from ParserHtml.parserHtml import ParserHtml

class ParserHtmlG1(ParserHtml):
    # função que retorna os titulos de noticias do G1
    def getTitles(self, htmlString):
        htmlParsed = BeautifulSoup(htmlString, 'html.parser')
        return [item.get_text() for item in htmlParsed.find_all("a", class_="feed-post-link")]

    # função que retorna as URLs das noticias do G1
    def getUrls(self, htmlString):
        htmlParsed = BeautifulSoup(htmlString, 'html.parser')
        return [item['href'] for item in htmlParsed.find_all("a", class_="feed-post-link", href=True)]