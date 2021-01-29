#!/usr/bin/env python
# coding: utf-8

# ## Set up 

# In[2]:


# Upload the modules I need
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# I want my graphs to be generated and reloaded in the same page of my code
get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('reload_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')

# Confirm my setup is complete
print('Set up complete')


# ## Upload the CSV file

# In[4]:


# Upload the CSV where I have my data
df = pd.read_csv(r'C:\Users\raflg\Desktop\Random Data.csv', sep=';')
# Check it
df.head()


# In[6]:


df.shape


# ## Create group

# In[5]:


# Create and add a new column to get two groups: Team and Staff
df['Group'] = ['Team' if name != 'Coach' else 'Staff' for name in df['Name']]
#Check it
df.tail()


# ## Arrange the dataframe for the graph

# In[34]:


# Arrange the dataframe to have my perceptions on rows for the graph
df_arranged = df.melt(id_vars=['Name','Group'], var_name='Perceptions', value_name='Value')
# Check it
df_arranged


# ## Create the graph

# In[38]:


# Generate the graph with all the settings
sns.violinplot(data=df_arranged, x='Perceptions', y='Value', hue='Group', palette='pastel', split=True)


# In[ ]:




