
# coding: utf-8

# In[46]:

import pandas as pd
import statsmodels.api as sm
import math


# In[24]:

df = pd.read_csv('/Users/weihsi/Dropbox/Thinkful/thinkful_hello/Linear Regression/loansData_clean.csv')


# In[25]:

df['IR_TF'] = df['Interest.Rate'].map(lambda x: x < 0.12 )


# In[26]:

df.head(5)


# In[27]:

df = sm.add_constant(df, prepend = True)


# In[58]:

df.head(10)


# In[34]:

ind_vars = ['FICO.Score', 'Amount.Requested', 'const']


# In[35]:

logit = sm.Logit(df['IR_TF'], df[ind_vars])


# In[36]:

result = logit.fit()


# In[41]:

coeff = result.params
print result.summary()


# In[56]:

def logistic_function(FICO_Score, Loan_Amt):
    p = 1/(1 + math.e**(-60.125045 + 0.087423*(FICO_Score) - 0.000174*(Loan_Amt)))
    return p


# In[61]:

logistic_function(720, 10000)


# In[ ]:



