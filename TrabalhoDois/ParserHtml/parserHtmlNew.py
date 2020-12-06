from bs4 import BeautifulSoup
from ParserHtml.parserHtml import ParserHtml

class ParserHtmlNew(ParserHtml):
    def __init__(self, htmlname, classname):
        self.classname = classname
        self.htmlname = htmlname

    def getTitles(self, htmlString):
        htmlParsed = BeautifulSoup(htmlString, 'html.parser')
        return [item.get_text() for item in htmlParsed.find_all(self.htmlname, class_=self.classname)]

    def getUrls(self, htmlString):
        htmlParsed = BeautifulSoup(htmlString, 'html.parser')
        return [item['href'] for item in htmlParsed.find_all(self.htmlname, class_=self.classname, href=True)]