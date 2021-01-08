import requests
import re
from bs4 import BeautifulSoup

base_URL = "http://www.paulgraham.com/"
updatePage = False

# Update local copy of PG Essays
if (updatePage):
    all_articles_URL = baseURL + "articles.html"
    page = requests.get(all_articles_URL)
    writef = open("pg.html", "w")
    writef.write(str(page.content))
    writef.close()

# Read most recent HTML
readf = open("pg.html", "r")
html_doc = readf.read()

soup = BeautifulSoup(html_doc, 'html.parser')

all_tables = []

for table in soup.find_all('table'):
    for subtable in table.find_all('table'):
        all_tables.append(subtable)
    
best_essays_html = all_tables[-3]
best_essays_links = []
all_essays_html = all_tables[-2] 
all_essays_links = []


print("All Essays")
for link in all_essays_html.find_all('a'):
    all_essays_links.append(link.get('href'))

all_essays_content = []
for link in all_essays_links[0:20]:
    endpoint = base_URL + "articles.html" + "/" + link
    page = requests.get(endpoint)
    content = page.content
    soup = BeautifulSoup(content, 'html.parser')
    images = soup.find_all("img", alt=True)
    title = images[0]['alt']
    essay_content = soup.body.get_text()
    tempfile = open("essays/" + title+".txt", "w")
    tempfile.write(title + "\n" + essay_content)
    tempfile.close



    


    # newfile = open(link, "w")
    # newfile.write(str(print_content))
    # newfile.close
    # for table in soup.find_all('table'):
    #     for subtable in table.find_all('table'):
    #         print(subtable)
    #         print("\n")
    #         #temp.append(subtable)
    # #all_essays_content.append(temp[-3].get_text())
    
# print(all_essays_content[0])