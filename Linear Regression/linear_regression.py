
# coding: utf-8

# In[104]:

import pandas as pd

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

loansData.head()


# In[105]:

loansData['Interest.Rate'][0:5]


# In[106]:

loansData['Loan.Length'][0:5]


# In[107]:

loansData['FICO.Range'][0:5]


# In[108]:

clean_percent = loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip("%"))/100, 4))
clean_month = loansData['Loan.Length'].map(lambda x: int(x.rstrip(" months")))

clean_percent[0:5]


# In[109]:

loansData['Interest.Rate'] = clean_percent
loansData['Loan.Length'] = clean_month

loansData['Interest.Rate'][0:5]


# In[110]:

loansData['Loan.Length'][0:5]


# In[111]:

clean_fico = loansData['FICO.Range'].map(lambda x: x.split("-"))
clean_fico[0:5]


# In[112]:

clean_fico = clean_fico.map(lambda x: [int(n) for n in x])


# In[113]:

loansData['FICO.Score'] = clean_fico.map(lambda x: x[0])
loansData['FICO.Score'].head()


# In[114]:

import matplotlib.pyplot as plt

get_ipython().magic(u'matplotlib inline')

plt.figure()
p = loansData['FICO.Score'].hist()
plt.show


# In[115]:

a = pd.scatter_matrix(loansData, alpha = 0.05, figsize = (10,10), diagonal = 'hist')


# In[116]:

import numpy as np
import statsmodels.api as sm


# In[117]:

intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']


# In[118]:

y = np.matrix(intrate).transpose()
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()


# In[119]:

x = np.column_stack([x1,x2])


# In[122]:

X = sm.add_constant(x)
model = sm.OLS(y, X)
f = model.fit()


# In[126]:

print 'Coefficients: ', f.params[1:3]
print 'Intercept: ', f.params[0]
print 'P-Values: ', f.pvalues
print 'R-Squared: ', f.rsquared


# In[ ]:



