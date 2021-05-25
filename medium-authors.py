# Python program to get data inside
# a button tag using BeautifulSoup

# Import the libraries BeautifulSoup
# and os
from bs4 import BeautifulSoup as bs
import os

# Remove the last segment of the path
base = os.path.dirname(os.path.abspath(__file__))

# Open the HTML in which you want to make
# # changes
html = open(os.path.join(base, 'medium-authors.html'))

# # Parse HTML file in Beautiful Soup


a = bs(html, "html.parser")

main_text = a.find("div", class_="tags js-writers tags--dark tags--fontSizeSmall is-withUserCard")
print(main_text.text)
