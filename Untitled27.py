#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import numpy as np
import csv
import sys
import random
import numpy as np
with open('C:\\Users\\hp\\Downloads\\file.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('coors_new.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        mydict = {rows[0]:int(rows[1]) for rows in reader}


# In[ ]:


num=int(input("Enter the number of employees"))


# In[ ]:


mylist1= []
for key,value in mydict.items() :
    mylist1.append(value)


# In[ ]:



for i in range(num):
    r=random.sample(range(1,10),num)
    


# In[ ]:


mylist2 = []
for key,value in mydict.items() :
    mylist2.append(key)


# In[ ]:


list1=[]
for i in range(0,len(r)):
    a=r[i];
    list1.append(mylist1[a])


# In[ ]:


list2=[]
for i in range(0,len(r)):
    a=r[i];
    list2.append(mylist2[a])


# In[ ]:


for i in range(0,num):
    print(list1[i],list2[i])
    


# In[ ]:


high=0
low=9999999
for i in list1:
    if i> high:
        high=i;
for i in mydict.values():
    if i<low:
        low=i;


# In[ ]:


high


# In[ ]:


low


# In[ ]:


print("The difference between the highest and the lowest seleceted numbers are")
print(high-low)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




