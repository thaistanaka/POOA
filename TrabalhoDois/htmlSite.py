import urllib.request

class HtmlSite:
    def __init__(self, siteUrl="https://g1.globo.com/"):
        self.siteUrl = siteUrl

    # função que retorna o html do site de noticia 
    def getHtml(self):
        f = urllib.request.urlopen(self.siteUrl)
        htmlString = f.read().decode("utf8")
        f.close()
        return htmlString