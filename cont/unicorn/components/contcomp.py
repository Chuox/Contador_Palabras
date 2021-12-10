from django_unicorn.components import UnicornView

class ContcompView(UnicornView):
    url = ""
    #palabras = []
    numpalabras = 0
    cuenta = dict()
    palabras = []

    def count(self):
        self.palabras = self.url.split()
        for palabra in self.palabras:
            if palabra in self.cuenta:
                self.cuenta[palabra] += 1
            else:
                self.cuenta[palabra] = 1