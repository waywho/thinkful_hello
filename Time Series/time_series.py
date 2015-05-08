
# coding: utf-8

# In[18]:

get_ipython().magic(u'matplotlib inline')
import numpy as np
from pandas import Series, DataFrame
import pandas as pd
from datetime import datetime


# In[23]:

df = pd.read_csv('~/Dropbox/Thinkful/LoanStats/LoanStats3b.csv', header=1, low_memory=False)


# In[24]:

df.ix[0]


# In[25]:

df['issue_d'].head()


# In[26]:

# converts string to datetime object in pandas:
df['issue_d_format'] = pd.to_datetime(df['issue_d']) 
dfts = df.set_index('issue_d_format') 
year_month_summary = dfts.groupby(lambda x : x.year * 100 + x.month).count()
loan_count_summary = year_month_summary['issue_d']


# In[22]:

loan_count_summary.head()


# In[20]:

loan_count_summary.plot(kind = 'bar')


# In[32]:

import statsmodels.api

statsmodels.api.graphics.tsa.plot_acf(loan_count_summary)


# In[33]:

statsmodels.api.graphics.tsa.plot_pacf(loan_count_summary)


# In[ ]:



