#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os, shutil


# In[7]:


path = r"G:/My Drive/Data/Portfolio Project/Python Tutorials/"


# In[10]:


file_name = os.listdir(path)


# In[18]:


folder_names = ['csv files', 'image files', 'text files']
for loop in range (0,3):
   if not os.path.exists(path + folder_names[loop]):
        os.makedirs((path + folder_names[loop]))
        
for file in file_name:
    if ".xlsm" in file and not os.path.exists(path + "csv files/" + file):
        shutil.move(path + file, path + "csv files/" + file)
    elif ".png" in file and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file, path + "image files/" + file)
    elif ".jpg" in file and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file, path + "image files/" + file)
    elif ".txt" in file and not os.path.exists(path + "text files/" + file):
        shutil.move(path + file, path + "text files/" + file)


# In[17]:





# In[ ]:




