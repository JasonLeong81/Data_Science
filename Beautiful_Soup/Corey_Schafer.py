# Request ###################################################

# Installing request: pip install requests
import requests
# r = requests.get('https://xkcd.com/353/')
# print(r)
# print(dir(r)) # shows all methods and attributes within r
# help(r) # more detailed explanation about the methods
# print(r.text)
# r = requests.get('https://imgs.xkcd.com/comics/python.png')
# with open('comic.png','wb') as f:
#     f.write(r.content)
# print(r.status_code) # 200 (success), 300 (redirect), 400 (client error),500 (server errors)
# print(r.ok)
# print(r.headers)

# payload = {'page':2,'count':25}
# r = requests.get('https://httpbin.org/get',params=payload)
# print(r.text)
# print(r.url)
# payload = {'username':'Jason','password':'testing'}
# r = requests.post('https://httpbin.org/post',data=payload)
# print(r.text)
# r_dict = r.json()
# print(r_dict['form'])

# r = requests.get('https://httpbin.org/basic-auth/username/password',auth=('username','password'),timeout=3) # timeout = 3 seconds
# print(r.text)
# print(r)


# CSV ######################################################

import csv

# with open('names.csv','r') as f:
#     content = csv.reader(f)
#     # next(f)
#     with open('new.csv','w') as new:
#         content1 = csv.writer(new,delimiter='-') # tab = \t
#         for i in content:
#             # print(i)
#             content1.writerow(i)

# with open('names.csv') as f:
#     content = csv.DictReader(f)
#     for i in content:
#         print(i)

# with open('names.csv') as f:
#     content = csv.DictReader(f)
#     fieldnames = ['first_name','last_name','email']
#     # fieldnames = ['first_name', 'last_name']
#     with open('names_new.csv','w') as ff:
#         content1 = csv.DictWriter(ff,fieldnames=fieldnames,delimiter='\t')
#         content1.writeheader()
#         for i in content:
#             # print(i)
#             # del i['email']
#             content1.writerow(i)









# Beautiful soup ############################################
# installing: pip install beautifulsoup4
# installing: pip install lxml

from bs4 import BeautifulSoup
import requests
import csv

# with open('testing.html') as f:
#     soup = BeautifulSoup(f,'lxml')
# print(soup)
# print(soup.prettify())

# match = soup.title # title tag
# print(match,match.text)

# match = soup.find('div',class_='footer') # all, not only the first result
# print(match)

# article = soup.find('div',class_='article')
# headline = article.h2.a.text
# print(headline)
# summary = article.p.text
# print(summary)
# for i in soup.find_all('div',class_='article'):
#     headline = i.h2.a.text
#     print(headline)
#     summary = i.p.text
#     print(summary)

# source = requests.get('http://coreyms.com').text
# soup = BeautifulSoup(source, 'lxml')
# print(soup.prettify())

# csv_file = open('cms_scrape.csv', 'w')




