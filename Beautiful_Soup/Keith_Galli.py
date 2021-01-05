import requests
from bs4 import BeautifulSoup as bs

r = requests.get("https://keithgalli.github.io/web-scraping/example.html")
soup = bs(r.content,'lxml')
# print(soup.prettify())

headers = soup.find_all(['h1','h2'])
# print(headers)
paragraph = soup.find_all("p", attrs={"id": "paragraph-id"})
# print(paragraph)

import re
paragraphs = soup.find_all("p", string=re.compile('Some'))
# print(paragraphs)

content = soup.select('div p')
# print(content)
content = soup.select('h2 ~ p') # directly after h2 (on the same level)
# print(content)
bold_text = soup.select("p#paragraph-id b") # tag p with id = paragraph-id
# print(bold_text)

paragraphs = soup.select("body > p")
# print(paragraphs)
# for paragraph in paragraphs:
#   print(paragraph.select("i"))

# Grab by element with specific property
# print(soup.select("[align=middle]"))
# css selector reference: https://www.youtube.com/redirect?redir_token=QUFFLUhqbXJjeTNzemNSQzJjRURidHI5Rkk2d0JCUVhMZ3xBQ3Jtc0tuRUM1c1lGV1ZHUDd4VEdWbnR2TkRQbkNFNURUeHZSR0hnUjVoMWNKRHFyNDYxbEFBclJuMXd4VWhiMGRhMkE2Z1JZMmV4RGJ2Wmlxc1JIYTQzWHZkd0FoNmI4UWRhSmduUHB5Z195Zk1GQzVILWp2OA%3D%3D&q=https%3A%2F%2Fwww.w3schools.com%2Fcssref%2Fcss_selectors.asp&v=GjKQ6V_ViQE&event=video_description



####### Getting different properties of the html ####################################################
div = soup.find("div")
# print(div.get_text()) # because div.string will not work

p = soup.select('p#paragraph-id')
# print(p[0]['id'])
# print(p)
# print(p[0])

####### Code Navigation ####################################################
# print(soup.body.prettify())
# print(soup.body.find('div').find_next_siblings()) # everything below except for itself (in its level)



######### Exercise ######################################################
r = requests.get('https://keithgalli.github.io/web-scraping/webpage.html')
soup = bs(r.content,'lxml')
# print(soup.prettify())

# Get all of the social links form the webpage (in three ways) ##########
# t = soup.find('ul',class_='socials').find_all('li')
# for i in t:
#     print(i.a['href'])
# links = soup.select("ul.socials a") # class is . and # is id
# actual_links = [link['href'] for link in links]
# print(actual_links)
# links = soup.select("li.social a") # What????
# actual_links = [link['href'] for link in links]
# print(actual_links)

#  Scrape the table #####################################################
table = soup.select('table.hockey-stats')[0] # a list with one element (we get a list when we use select)
# print(table)
columns = table.find('thead').find_all('th')
column_names = [c.string for c in columns]
rows = table.find('tbody').find_all('tr')
l = []
for tr in rows:
    td = tr.find_all('td')
    row = [str(tr.string).rstrip() for tr in td]
    l.append(row)
import pandas as pd
df = pd.DataFrame(l,columns=column_names)
# print(df.head())

# Grab all the fun fact that use word "is" #####################################################
# import re
# ff = soup.select('ul.fun-facts li')
# fff = [fact.find(string=re.compile('is')) for fact in ff]
# for i in fff:
#     if i:
#         print(i.find_parent().text)

# Download an Image  #####################################################
url = "https://keithgalli.github.io/web-scraping/"
r = requests.get(url+"webpage.html")
soup = bs(r.content,'lxml')
images = soup.select('div.row div.column img')
image_url = images[0]['src']
full_url = url + image_url

img_data = requests.get(full_url).content
with open('lake.jpg','wb') as h:
    h.write(img_data)


