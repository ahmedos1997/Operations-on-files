import bs4
from pathlib import Path

examplefile = open(Path.home() / Path('G:/python cource','project','WebScraping','example.html'))

examplesoup = bs4.BeautifulSoup(examplefile,'html.parser')

print(type(examplesoup))


element = examplesoup.select('#author')
print(element)
print(element[0].getText())
