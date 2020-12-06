from datetime import datetime
import codecs

class File:
    def __init__(self, titles, filename=datetime.now().strftime("news-%Y-%m-%d-%H-%M.csv")):
        self.filename = filename
        self.titles = titles

    # função que cria o arquivo com titulos de noticias
    def writeFile(self):
        file = codecs.open(self.filename, "w", encoding='utf-8')
        for title in self.titles:
            file.write(title+"\n")
        file.close()