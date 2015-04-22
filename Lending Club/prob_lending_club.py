
# coding: utf-8

# In[1]:

import matplotlib.pyplot as plt
import pandas as pd

get_ipython().magic(u'matplotlib inline')

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')


# In[3]:

loansData.dropna(inplace = True)


# In[5]:

loansData.head()


# In[6]:

loansData.boxplot(column = 'Amount.Requested')
plt.show


# In[7]:

loansData.hist(column = 'Amount.Requested', histtype = 'bar')
plt.show


# In[9]:

import scipy.stats as stats

plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot = plt)
plt.show


# In[ ]:

'''
The Amounts Requested and the Amounts Funded by Inverstors were fairly similar
when compariing the boxplots and the frequency distributions.
Both the Amounts Requested and the Amounts Funded are right skewed with the average of loans around 10000.
There were somewhat less numbers of loans Funded by Investors comparing to Amount Requested 
between the amounts of 15000 and 20000, and there were somewhat more numbers of loans Funded by Inverstors
comparing to Amount Requested in the 5000 to 10000 range.
Both distributions are not normal.
'''

