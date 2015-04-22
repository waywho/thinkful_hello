
# coding: utf-8

# In[12]:

# Distribution Plot

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab

get_ipython().magic(u'matplotlib inline')
#to show plots in line

mean = 0
variance = 1
sigma = np.sqrt(variance) #standard deviation
x = np.linspace(-3,3,100)
plt.plot(x,mlab.normpdf(x,mean,sigma))
plt.title('Normal Distribution')

plt.show


# In[4]:

import collections

testlist = [1, 4, 5, 6, 9, 9, 9]

c = collections. Counter(testlist)

print c

count_sum = sum(c.values())

for k,v in c.iteritems():
    print "The frequency of number " + str(k) + " is " + str(float(v) / count_sum)


# In[13]:

# Box Plot

import matplotlib.pyplot as plt

get_ipython().magic(u'matplotlib inline')

x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]

plt.boxplot(x)
plt.title('Boxplot')
#option to save plt.savefig('boxplot.png')

plt.show()


# In[20]:

plt.hist(x, histtype='bar')
plt.title('Frequency Distribution')
plt.xlabel('values')
plt.ylabel('frequency')
plt.show


# In[21]:

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

get_ipython().magic(u'matplotlib inline')

plt.figure()
test_data = np.random.normal(size = 1000)
graph1 = stats.probplot(test_data, dist="norm", plot = plt)
plt.title('QQ-Plot of Normal Distribution')
plt.show() #generate first plot
plt.figure()
test_data2 = np.random.uniform(size = 1000)
graph2 = stats.probplot(test_data2, dist="norm", plot = plt)
plt.title('QQ-Plot of Uniform Distribution')
plt.show()


# In[ ]:



