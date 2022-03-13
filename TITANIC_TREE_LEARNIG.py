#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import tree
get_ipython().run_line_magic('matplotlib', 'inline')

from graphviz  import Source
from IPython.display import SVG, display, HTML
style = "<style>svg{width: 70% !important; height: 60% !important;} </style>" 


# In[2]:


data=pd.read_csv('C:/Users/oleg3/Downloads/cats.csv')


# In[3]:


data


# In[4]:


data.Шерстист


# In[5]:


np.log2(12)


# In[6]:


-(4/9)*np.log2((4/9))-(5/9)*np.log2((5/9))


# In[7]:


(1/1)*np.log2((1/1)) - 0


# In[8]:


-(4/10)*np.log2((4/10)) - (6/10)*np.log2((6/10))


# In[9]:


0.9709505944546686-0.72


# In[10]:


9/10*0.99


# In[11]:


0.9709505944546686-(9/10)*0.99


# In[12]:


0.9709505944546686-(5/10)*0.72


# In[13]:


E_gav_sob=0 - (5/5)*np.log2((5/5))
E_gav_kot=-(4/5)*np.log2((4/5)) - (1/5)*np.log2((1/5))
IG_gav = - 0.97 - (5/10)*E_gav_sob - (5/10)*E_gav_kot


# In[14]:


titanic_data=pd.read_csv('C:/Users/oleg3/Downloads/train.csv')


# In[15]:


titanic_data


# In[16]:


X = titanic_data.drop(['PassengerId','Survived','Name','Ticket','Cabin'],axis = 1)


# In[17]:


y=titanic_data.Survived
X = pd.get_dummies(X)
X.head()


# In[18]:


X=X.fillna({'Age':X.Age.median()})
X.isnull().sum()


# In[19]:


clf = tree.DecisionTreeClassifier(criterion='entropy')
clf.fit(X,y)


# In[20]:


plt.figure(figsize=(100, 25))


# In[21]:


from sklearn.model_selection import train_test_split


# In[22]:


X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.33,random_state=42)


# In[23]:


clf.score(X,y)


# In[24]:


clf.fit(X_train,y_train)


# In[25]:


clf.score(X_train,y_train)


# In[26]:


clf.score(X_test,y_test)


# In[27]:


clf = tree.DecisionTreeClassifier(criterion='entropy',max_depth=3)
clf.fit(X_train,y_train)


# In[28]:


clf.score(X_train,y_train)


# In[29]:


clf.score(X_test,y_test)


# In[30]:


max_depth_values=range(1,100)


# In[31]:


score_data=pd.DataFrame()


# In[34]:


for max_depth in max_depth_values:
    clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=max_depth)
    clf.fit(X_train, y_train)
    train_score = clf.score(X_train, y_train)
    test_score = clf.score(X_test, y_test)
    
    temp_score_data = pd.DataFrame({'max_depth': [max_depth], 'train_score': [train_score], 'test_score': [test_score]})
    score_data=score_data.append(temp_score_data)


# In[35]:


score_data.head()


# In[36]:


score_data_long=pd.melt(score_data, id_vars = ['max_depth'], value_vars = ['train_score','test_score'], var_name = 'set_type', value_name = 'score')

sns.lineplot(x='max_depth', y='score', hue='set_type', data=score_data_long)


# In[ ]:




