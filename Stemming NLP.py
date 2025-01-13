#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##classification problem
##comments of product is a positive review or negative review
##reviews-->eating,eat,eaten[going,gone,goes]-->go


# In[1]:


words=["eating","eats","eaten","writing","writes","programming","programs","history","finally","finalized"]


# # PORTER STEMMER
# 

# In[2]:


from nltk.stem import PorterStemmer


# In[3]:


stemming=PorterStemmer()


# In[4]:


##for each and every word stemming is going to be applied
for word in words:
    print(word+"----->"+stemming.stem(word))


# problem:
#     history--->histori
#     *this is the major diadvantage of the stemming
#     *when stemming is basically applied for some of the words you may not have exact meaning

# In[5]:


##some more example
stemming.stem('congratulations')


# problem:
#     the meaning of the word is changing
#     not the word does not have any meaning
#     which is the major disadvantage of stemming
#     *But this all will be getting fixed with the lemmatization 
#     *But in classification or review kind of problem it is better to use stemming technique these issues will be fixed with other stemming functionalities

# # RegexpStemmer class

# This is the class with the help of which we can seasily implemet Regular expression stemmer algorithms. it basically takes a sinngle regular expression and removes any prefix or suffix that mtches the expression. Let us see an example

# In[6]:


from nltk.stem import RegexpStemmer


# In[14]:


reg_stemmer=RegexpStemmer('ing$|s$|e$|able$',min=4)


# In[15]:


reg_stemmer.stem('eating')


# In[16]:


reg_stemmer.stem('ingeating')


# In[18]:


reg_stemmer.stem("congratulations")


# # Snowball Stemmer

# *Snowball stemmer is again a stemming technique
# *But it performs better than the portter stemmer
# *snowball stemmer brings good accuraccy(better word stemming)

# In[19]:


from nltk.stem import SnowballStemmer


# In[20]:


snowballstemmer=SnowballStemmer('english')


# In[21]:


for word in words:
    print(word+"--------->"+snowballstemmer.stem(word))


# still we have issues with the 'histori'
# But lets see where this snowball stemmer is better than all
# 

# In[22]:


##this is with repect to porter stemmer
stemming.stem("fairly"),stemming.stem("sportingly")


# In[23]:


snowballstemmer.stem("fairly"),snowballstemmer.stem("sportingly")


# all  together we could see that when we apply snowballstemmer could actully gives a better result

# Disadvantage:
#  In short how much we try for some of the words. The stem form of the word is changing
#  There is a thing called lemmatization which solves all the problem because it has the dictionary of all the root words.

# In[ ]:




