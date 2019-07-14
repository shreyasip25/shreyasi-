#!/usr/bin/env python
# coding: utf-8

# In[3]:


def freq(str):
    str=str.split()
    str2=[]
    
    for i in str:
        if i not in str2:
            str2.append(i)
            
    for i in range(0, len(str2)):
        print(str2[i],':',str.count(str2[i]))


# In[4]:


str="blue color red color white color blue is my favourite color blue looks good"
freq(str)


# In[ ]:




