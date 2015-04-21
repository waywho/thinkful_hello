
# coding: utf-8

# In[9]:

import pandas as pd
from scipy import stats

data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''


# In[10]:

data = data.splitlines()


# In[11]:

data = [i.split(', ') for i in data]


# In[12]:

column_names = data[0] # this is the first row
data_rows = data[1::] # thesea re all the following rows
df = pd.DataFrame(data_rows, columns=column_names)


# In[13]:

df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)


# In[31]:

alco_mean = df['Alcohol'].mean()


# In[32]:

alco_med = df['Alcohol'].median()


# In[33]:

alco_mode = stats.mode(df['Alcohol'])


# In[34]:

tob_mean = df['Tobacco'].mean()


# In[35]:

tob_med = df['Tobacco'].median()


# In[36]:

tob_mod = stats.mode(df['Tobacco'])


# In[37]:

alco_range = max(df['Alcohol']) - min(df['Alcohol'])


# In[38]:

alco_std = df['Alcohol'].std()


# In[39]:

alco_var = df['Alcohol'].var()


# In[40]:

tob_range = max(df['Tobacco']) - min(df['Tobacco'])


# In[41]:

tob_std = df['Tobacco'].std()


# In[42]:

tob_var = df['Tobacco'].var()


# In[48]:

alc_result = {
    'mean': df['Alcohol'].mean(),
    'median': df['Alcohol'].median(),
    'mode': stats.mode(df['Alcohol']),
    'range': max(df['Alcohol']) - min(df['Alcohol']),
    'variance': df['Alcohol'].var(),
    'standard deviation': df['Alcohol'].std()
}

tob_result = {
    'mean': df['Tobacco'].mean(),
    'median': df['Tobacco'].median(),
    'mode': stats.mode(df['Tobacco']),
    'range': max(df['Tobacco']) - min(df['Tobacco']),
    'variance': df['Tobacco'].var(),
    'standard deviation': df['Tobacco'].std()
}


# In[50]:

ct = ['mean', 'median', 'mode', 'range', 'variance', 'standard deviation']
for i in ct:
    print "The weekly Alcohol spending %s for the Alcohol and Tobacco dataset is %s" % (i, alc_result[i])

print '\n'
    
for i in ct:
    print "The weekly Tobacco spending %s for the Alcohol and Tobacco dataset is %s" % (i, tob_result[i])


# In[ ]:



