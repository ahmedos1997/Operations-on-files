import bs4
import requests

res = requests.get('https://en.wikipedia.org/wiki/main_page')
notsoup = bs4.BeautifulSoup(res.text,'html.parser')
print(type(notsoup))


element = notsoup.select('#mp-tfa > p')
print((element))
print(element[0].getText())