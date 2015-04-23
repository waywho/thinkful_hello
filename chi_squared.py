
# coding: utf-8

# In[5]:

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import collections

get_ipython().magic(u'matplotlib inline')

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansData.dropna(inplace = True)

freq = collections.Counter(loansData['Open.CREDIT.Lines'])


# In[6]:

plt.figure()
plt.bar(freq.keys(), freq.values(), width = 1)
plt.show


# In[8]:

chi, p = stats.chisquare(freq.values())


# In[9]:

chi


# In[10]:

p


# In[ ]:



