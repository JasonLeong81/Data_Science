from matplotlib import pyplot as plt
import pandas as pd

plt.style.use('fivethirtyeight')

# ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]
# bins = [10,20,30,40,50,60]
# plt.hist(ages,bins=bins,edgecolor='black')


data = pd.read_csv('data2.csv')
bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
ids = data['Responder_id']
ages = data['Age']
plt.hist(ages,bins=bins,edgecolor='black',log=True) # True log plots it on a logarithmic scale # otherwise we dont see very small values

median_age = 29
color = '#fc4f30'
plt.axvline(median_age, color=color, label='Age Median', linewidth=2) # axis vertical line


plt.legend()
plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

plt.tight_layout()

plt.show()