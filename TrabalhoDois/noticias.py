import urllib.request
from bs4 import BeautifulSoup
import codecs
#import argparse

#class ArgParser:

class Html:
    
    def __init__(self,siteUrl="https://g1.globo.com/"):
        self.siteUrl = siteUrl
        
    def getHtml(self):
        f = urllib.request.urlopen(self.siteUrl)
        htmlString = f.read().decode("utf8")
        f.close()
        return htmlString
    
class ParserHtml:
    
    def getTitles(self,htmlString):
        pass

class ParserHtmlG1(ParserHtml):
    
    def getTitles(self,htmlString):
        htmlParsed = BeautifulSoup(htmlString,'html.parser')
        return [item.get_text() for item in htmlParsed.find_all("a",class_="feed-post-link")]

class File:
    
    def __init__(self,titles,filename = "test.csv"):
        self.filename = filename
        self.titles = titles
    
    def writeFile(self):
        file = codecs.open(self.filename,"w",encoding='utf-8')
        for item in self.titles:
            file.write(item+"\n")
        file.close()
        
def printTitles(titles):
    
    for item in titles:
        print(item)
        
html = Html()
titles = []
if html.siteUrl == "https://g1.globo.com/":
    titlesG1 = ParserHtmlG1()
    titles.extend(titlesG1.getTitles(html.getHtml()))
    fileCsv = File(titles)
    fileCsv.writeFile()