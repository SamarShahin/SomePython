# plot_time_series.py

import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from matplotlib import dates as mpl_dates
import pandas as pd
plt.style.use('seaborn')

data = pd.read_csv('/home/user/Desktop/MotionDetection/Motionlog.csv')
data['dateandtime'] = pd.to_datetime(data['dateandtime'])
#data.sort_values('dateandtime', inplace=True)
action_date = data['dateandtime']
action_type = data['action']
action_duration=data['duration']
plt.plot_date(action_date, action_type, linestyle='solid')

plt.gcf().autofmt_xdate()
date_format = mpl_dates.DateFormatter('%d%b-%Y_%Hh-%Mm-%Ss.%f')
plt.gca().xaxis.set_major_formatter(date_format)
plt.tight_layout()
plt.title('Motion Detection')
plt.xlabel('Date')
plt.ylabel('Motion Status')


plt.show()
