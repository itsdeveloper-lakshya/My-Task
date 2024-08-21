#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install google


# In[ ]:


from googlesearch import search
search_query=input("Enter your query:")
for i in search(search_query,tld='co.in',lang='en',num=5,stop=5,pause=2.0):
    print(i)


# In[ ]:




