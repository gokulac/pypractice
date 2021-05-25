from bs4 import BeautifulSoup as bs
import os

base = os.path.dirname(os.path.abspath(__file__))

html = open(os.path.join(base, 'medium-authors.html'))

a = bs(html, "html.parser")

main_text = a.find("div", class_="tags js-writers tags--dark tags--fontSizeSmall is-withUserCard")

print(main_text.text)