from datetime import datetime
import codecs

class File:
    def __init__(self, titles, urls, siteUrl,filename=datetime.now().strftime("news-%Y-%m-%d-%H-%M.csv")):
        self.filename = filename
        self.titles = titles
        self.urls = urls
        self.siteUrl = siteUrl

    # função que cria o arquivo com titulos de noticias
    def writeFile(self):
        file = codecs.open(self.filename, "w", encoding='utf-8')
        if len(self.urls) == 0:
            file.write('TITULOS:\n')
            for title in self.titles:
                file.write(title + '\n')
        elif len(self.titles) == 0 and len(self.urls) == 0:
            file.write('Erro na extração de notícias do site!')
        else:
            file.write('TITULOS E LINKS:\n')
            for title, url in zip(self.titles, self.urls):
                file.write(title + " - "+ url + "\n")
        file.close()