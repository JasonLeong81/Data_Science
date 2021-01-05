from matplotlib import pyplot as plt

# use pie chart only when there are no more than 5 data, if more than 5, use horizontal bar chart

plt.style.use('fivethirtyeight')
labels = ['Sixty','Forty','Ten']
slices  = [60,40,10]
color =['green','red','blue']
explode = [0,0.1,0]
plt.pie(slices,autopct='%1.1f%%',startangle=90,shadow=True,labels=labels,wedgeprops={'edgecolor':'black'},colors=color,explode=explode) # can use hex colors as well


plt.title('My Awesome Pie Chart')
plt.tight_layout()
plt.show()