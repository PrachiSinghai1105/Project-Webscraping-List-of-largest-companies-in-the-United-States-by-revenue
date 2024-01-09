#!/usr/bin/env python
# coding: utf-8

# In[2]:


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')


# In[1]:


from bs4 import BeautifulSoup
import requests


# In[3]:


print(soup)


# In[4]:


soup.find('table' , class_ = 'wikitable sortable')


# In[5]:


table = soup.find_all('table')[1]
print(table)


# In[6]:


world_titles = table.find_all('th')
world_titles
world_table_titles = [title.text.strip() for title in world_titles]
world_table_titles


# In[7]:


import pandas as pd


# In[8]:


df = pd.DataFrame(columns = world_table_titles)

df


# In[9]:


column_data = table.find_all('tr')
print(column_data)


# In[10]:


for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data


# In[11]:


df


# In[12]:


df.to_csv(r'C:\Users\alexf\OneDrive\Documents\Python Web Scraping\Folder for Output\Companies.csv', index = False)


# In[ ]:




