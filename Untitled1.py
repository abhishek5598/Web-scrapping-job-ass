#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[59]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[60]:


# Send an HTTP GET request to the URL
page= requests.get("https://www.kotak.com/en/offers.html")


# In[87]:


# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find elements containing the required information
    card_elements = soup.find_all("div", class_="card")


# In[90]:


# Parse the HTML content of the page
soup=BeautifulSoup(page.content)


# In[91]:


card_names=[]
views=[]
expiry_date=[]
description=[]
rating=[]


# In[92]:


#for all Cardname
card_name_elements=soup.find_all("h4",class_="card-heading")
for element in card_name_elements:
    card_names.append(element.text)


# In[93]:


#for the rating


# In[94]:


ratings=soup.find_all("div",class_="rating")
# to extract the all the ratings of the card
for i in ratings:
    rating.append(i.text.replace("\n",""))


# In[95]:


#for the views
views_card=soup.find_all("div",class_="views")
# to extract the all the ratings of the card
for i in views_card:
    if hasattr(i,'text'):
        views.append(i.text)
    else:
        views.append(i)


# In[96]:


#for the expiry
expiry=soup.find_all("div",class_="article-date")
# to extract the all the ratings of the card
for i in expiry:
    if hasattr(i,'text'):
        expiry_date.append(i.text)
    else:
        expiry_date.append(i)


# In[97]:


#for the description
desc=soup.find_all("div",class_="card-desc")
# to extract the all the description of the card
for i in desc:
    if hasattr(i,'text'):
        description.append(i.text)
    else:
        description.append(i)


# In[98]:


#now i have to scrape these all things inside the list 


# In[99]:


df=pd.DataFrame(index=list(range(1,22)))

df["Views"]=pd.Series(views)
df["Expiry_Date"]=pd.Series(expiry_date)
df["Card_Name"]=pd.Series(card_names)
df["Description"]=pd.Series(description)
df["Rating"]=ratings

df


# # End of Assignment 

# In[100]:


#If i got the opportunity i will definately improve and workhard for my JD.


# In[ ]:




