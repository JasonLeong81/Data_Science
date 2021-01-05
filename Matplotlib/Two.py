from matplotlib import pyplot as plt
from snippets import *
import numpy as np
from csv import *
from collections import Counter # to count programming language for each respondent in teh dataset efficiently as a dictionary
import pandas as pd

x_indexes = np.arange(len(dev_x))
width = 0.25

# plt.bar(x_indexes - width, dev_y,label='All Devs',width=width) # can also hex color code for color
# plt.bar(x_indexes, py_dev_y,label='Python',width=width)
# plt.bar(x_indexes + width, js_dev_y,label='JS',width=width)
# plt.xticks(ticks=x_indexes,labels=dev_x)
#
# plt.tight_layout() # makes padding a lot better
# plt.grid(True)
# plt.legend()
# plt.xlabel('Ages')
# plt.ylabel('Median Salary (USD)')
# plt.title('Median Salary (USD) by Age')

with open('data.csv') as f:
    csv_reader = DictReader(f)
    counter = Counter() # Counter is a class
    for i in csv_reader: # no need next?
        counter.update(i['LanguagesWorkedWith'].split(';'))
    # row = next(csv_reader)
    # print(row)
    # print(row['LanguagesWorkedWith'].split(';'))
    # print(counter)
    # print(counter.most_common(15)) # a tuple containing the language and its count

l,p = [],[]
for i in counter.most_common(15):
    l.append(i[0])
    p.append(i[1])
# print(l)
# print(p)

# plt.bar(l,p)
plt.barh(l,p) # need to change x and y labels, just be careful
# l.reverse()
# p.reverse()
# plt.barh(l,p) # why can't I reverse it here?
plt.tight_layout() # makes padding a lot better
plt.grid(True)
plt.xlabel('Programming Languages')
plt.ylabel('Number Of People Who Use')
plt.title('Most Popular Languages')


plt.show()