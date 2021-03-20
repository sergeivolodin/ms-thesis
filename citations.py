#!/usr/bin/env python
# coding: utf-8

# In[1]:


import bibtexparser
import numpy as np
from matplotlib import pyplot as plt


# In[3]:


with open('thesis.bib') as bibtex_file:
    bibtex_str = bibtex_file.read()


# In[5]:


bib_database = bibtexparser.loads(bibtex_str)


# In[8]:


years = [int(x['year']) for x in bib_database.entries]


# In[13]:


plt.figure()
plt.hist(years)
plt.yscale('log')
plt.title("Papers in database by year")
plt.xlabel("Year")
plt.ylabel("Papers")
plt.show()


# In[ ]:




