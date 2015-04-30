
# coding: utf-8

# In[11]:

import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

get_ipython().magic(u'matplotlib inline')

import zipfile
import urllib


# In[25]:

Loan3a = pd.read_csv('LoanStats3a.csv', header = 1)
Loan3a.head()


# In[27]:

Loan3b = pd.read_csv('LoanStats3b.csv', header = 1)
Loan3b.head()


# In[28]:

Loan3c = pd.read_csv('LoanStats3c.csv', header = 1)
Loan3c.head()


# In[114]:

LoanStatAll = Loan3a.append(Loan3b).append(Loan3c)


# In[115]:

LoanStatAll['int_rate'] = LoanStatAll['int_rate'].map(lambda x: round(float(str(x).rstrip("%"))/100, 4))


# In[116]:

LoanStatAll.head()


# In[131]:

LoanStatAll.dropna(inplace = True)
X = LoanStatAll['annual_inc']
y = LoanStatAll['int_rate']

X = sm.add_constant(X)
est = sm.OLS(y, X).fit()

est.summary()


# In[79]:

import collections

count = collections.Counter()
for n in LoanStatAll['home_ownership']:
    count[n] +=1
    
count


# In[127]:

LoanStatAll['home_ownership'] = pd.Categorical(LoanStatAll['home_ownership']).codes


# In[129]:

LoanStatAll['home_ownership2'].head()


# In[128]:

est1 = smf.ols(formula ='int_rate ~ home_ownership2 + annual_inc', data=LoanStatAll).fit()

est1.summary()


# In[126]:

est2 = smf.ols(formula ='int_rate ~ home_ownership2 * annual_inc', data=LoanStatAll).fit()

est2.summary()


# In[ ]:



