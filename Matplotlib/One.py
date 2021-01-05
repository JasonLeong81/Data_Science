from snippets import *


# Installing : pip install matplotlib
from matplotlib import pyplot as plt

# print(plt.style.available) # all styles available
plt.style.use('fivethirtyeight')
# plt.xkcd() # just for fun


plt.plot(dev_x, dev_y,'k--.',label='All Devs',linewidth='3') # can also hex color code for color
plt.plot(py_dev_x,py_dev_y,'b',label='Python')
plt.legend() # empty argument only if label are specified above

plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Median Salary (USD) by Age')

# plt.legend(['All Devs','Python']) # not so good

plt.tight_layout() # makes padding a lot better

plt.grid(True)

# plt.savefig('plot.png') # save in the current directory or to a specific path but we have to specify full path

plt.show()

# format string matplotlib : https://www.youtube.com/redirect?v=UO98lJQ3QGI&event=video_description&redir_token=QUFFLUhqbEpfZG9SWWQzcC1Dai1oS3pKU3FPYkNnaHJDd3xBQ3Jtc0tsRWxQVjdRN1ZpaHVKSS1hVm83OTJqMGo3emF1Y0lIVVVPSTh0STNOX0M0M04tQUtWY3V5enlHSk1iaGRmVm5iN1hXUHdVaWhvSlk5Z0lCSHpOc0FYc1hFSUhoV3lIc09RV1VmTzNfRHVwWVBhZDg2WQ%3D%3D&q=http%3A%2F%2Fbit.ly%2FMatplotlib-Fmt-Str