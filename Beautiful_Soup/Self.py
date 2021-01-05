from bs4 import BeautifulSoup
import requests

def clean_1(l):
    # clean commas and brackets
    for i in range(1,len(l)):
        for j in range(len(l[i][1])):
            # print(l[i][1][j])
            if l[i][1][j] == '(':
                l[i][1] = l[i][1][:j].strip()
                break
    for i in range(1,len(l)):
        for j in range(len(l[i][1])):
            if l[i][1][j] == ',':
                l[i][1] = l[i][1][:j] + l[i][1][j+1:]
                break
        l[i][1] = int(l[i][1])
    return l
    # for i in l:
    #     print(i[1],type(i[1]))
# clean_1([['NEGERI', 'BILANGAN KES BAHARU *( )', 'BILANGAN KES KUMULATIF'], ['SABAH', '260 (1)', '34,083'], ['SELANGOR', '692 (2)', '23,623'], ['W.P. KUALA LUMPUR', '197 (3)', '9,623'], ['NEGERI SEMBILAN', '174', '6,858'], ['JOHOR', '77 (2)', '2,912'], ['PULAU PINANG', '37', '2,900'], ['KEDAH', '4', '2,869'], ['PERAK', '65', '2,775'], ['W.P. LABUAN', '19', '1,495'], ['SARAWAK', '1', '1,085'], ['PAHANG ', '6', '861'], ['MELAKA', '140', '691'], ['KELANTAN', '1', '483'], ['TERENGGANU', '4', '285'], ['W.P. PUTRAJAYA', '6', '228'], ['PERLIS', '0', '45'], ['JUMLAH KESELURUHAN', '1,683 (8)', '90,816']]
# )

def detail(string):
    import csv
    url = "https://kpkesihatan.com/"
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    # string = soup.find('section',class_='entry').h2.a.text
    n = soup.find_all('a',href=True)
    # print(soup.prettify())
    next_page = ''
    for i in n:
        # if 'Kenyataan Akhbar KPK 6 Disember 2020' in i.text:
        #     print(i.text.strip()==string)
        if i.text.strip() == string:
            # print(i)
            # print(i['href'])
            next_page = i['href']
            break
    url = next_page
    # print('url',url)
    # return


    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    # print(soup.prettify())


    ### write your code here

    # st = soup.find_all('ul', class_=False)
    # for i in st:
    #     y = i.li
    #     j = y.find_all('strong')
    #     jj = y.find_all('ul',class_=False)
    #     try:
    #         # for n in j:
    #         #     print(n)
    #         # print(n.text)
    #         for nn in jj:
    #             print(nn.text)
    #             print()
    #     except:
    #         continue

    ### end of your code



    n = soup.find_all('figure',class_='wp-block-table')
    # for i in n[1:]:
    #     print(i.table.tbody)
    temp = []
    for j in n[1:]:
        try:
            tr = j.table.tbody.find_all('tr')
            # print(tr)
        except:
            pass
            print(j)
        else:
            for h in tr:
                tds = h.find_all('td')
                temp.append([tds[0].text,tds[1].text,tds[2].text])
    # for i in temp:
    #     print(i) # answer

    l = len(temp[0][1])
    for i in range(l):
        if temp[0][1][i] == '*':
            temp[0][1] = temp[0][1][:i+1] + '( )'
            break
    # for i in temp:
    #     print(i)
    return temp
def Filter(day_of_month,Sort=None):
    url = "https://kpkesihatan.com/"
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    strings = soup.find_all('section',class_='entry')

    target = f"Kenyataan Akhbar KPK {day_of_month} Disember 2020 – Situasi Semasa Jangkitan Penyakit Coronavirus 2019 (COVID-19) di Malaysia"
    state = 'all'
    for i in strings:
        t = i.h2.a.text.strip()
        if target == t:
            print(target)
            print()
            if not Sort:
                t = detail(target)
                for i in t:
                    if state.upper() == "ALL":
                        print(i)
                    if state.upper() == i[0]:
                        print(i)
                        break
                return
            else:
                t = detail(target)
                # print(t)
                t = clean_1(t)
                if Sort.upper() == 'A':
                    for i in range(1,len(t)-2):
                        for j in range(1,len(t)-2):
                            if t[j][1] > t[j+1][1]:
                                t[j+1],t[j] = t[j],t[j+1]
                else:
                    for i in range(1,len(t)-2):
                        for j in range(1,len(t)-2):
                            if t[j][1] < t[j+1][1]:
                                t[j+1],t[j] = t[j],t[j+1]
                for i in t:
                    if state.upper() == "ALL":
                        print(i)
                    if state.upper() == i[0]:
                        print(i)
                        break
                return
    return 'Not in the website.'



def overview():
    source = requests.get('https://www.worldometers.info/coronavirus/country/malaysia/').text
    soup = BeautifulSoup(source, 'lxml')
    # print(soup.prettify())

    n = soup.find_all('li',class_='news_li')
    nn = soup.find_all('div',class_='news_date')
    nnn = soup.find_all('button',class_='btn btn-light date-btn')
    dates = []
    temp = ''
    for i in nn:
        temp += i.h4.text
    dates.append(temp)
    temp = ''
    for i in nnn:
        dates.append(i.text)
    # for i in dates:
    #     print(i)

    c = 0
    for i in n:
        print(dates[c],i.strong.text)
        c += 1


# overview()
ans = int(input('Enter date: '))
Filter(ans,'d')





def location():
    url = "https://kpkesihatan.com/"
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')

# location()
