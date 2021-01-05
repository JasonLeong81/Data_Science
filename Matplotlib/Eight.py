import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

# Datetime Format Codes : https://www.youtube.com/redirect?q=http%3A%2F%2Fbit.ly%2Fpython-dt-fmt&v=_LWjaAiKaf8&redir_token=QUFFLUhqa2gxTHdyT3ZXTXVzc2hyb0hNRng4OGlZM2wwZ3xBQ3Jtc0tsaEpBcGpxQUNiajZCRTEwTUxpR1pzTndsZnByRldzc05RaEdnN2ZOakhTbnhhOWIyS1RUYnhtVFZGX1hISTlOWVhRYklCeGQ4NzdQdGg3WVAxaVR3M1BFa1BUVVNsRTdRTF9SaTVHLWlIWUo4SmN3dw%3D%3D&event=video_description

plt.style.use('seaborn')

dates = [
    datetime(2019, 5, 24),
    datetime(2019, 5, 25),
    datetime(2019, 5, 26),
    datetime(2019, 5, 27),
    datetime(2019, 5, 28),
    datetime(2019, 5, 29),
    datetime(2019, 5, 30)
]

y = [0, 1, 3, 4, 6, 5, 7]

# plt.plot_date(dates,y,linestyle='solid')
# plt.gcf().autofmt_xdate() # get current figure.autoformat_xdate()
# date_format = mpl_dates.DateFormatter('%b, %d' '%Y')
# plt.gca().xaxis.set_major_formatter(date_format) # grab current axis.xaxis.set_major_formatter(date_format)


data = pd.read_csv('data4.csv')
data['Date'] = pd.to_datetime(data['Date']) # we do this because otherwise it will be read in as strings and not dates
data.sort_values('Date', inplace=True)
price_date = data['Date']
price_close = data['Close']

plt.plot_date(price_date,price_close,linestyle='solid')
plt.gcf().autofmt_xdate() # get current figure.autoformat_xdate()


plt.title('Bitcoin Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.tight_layout()
plt.show()