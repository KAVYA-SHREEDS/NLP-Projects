#!/usr/bin/env python
# coding: utf-8

# # Wordnet Lemmatizer

# Lemmatization technique is like stemming.The output we will get after lemmatization is called  'lemma' which is a root word rather than root stem,the output of stemming.After  lemmatization we will gettig a vaid word that means the same thing

# NLTK provides WordNetLemmatizer class which is a thin wrapper around the wordnet corpus.This class uses morphy() function to the WordNet CorpusReader class to find a lemma.Let us understand with an example...

# In[4]:


import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')  # Optional, for better lemmatization support


# In[5]:


from nltk.corpus import wordnet
print(wordnet.synsets("test"))



# In[6]:


from nltk.stem import WordNetLemmatizer


# In[7]:


lemmatizer=WordNetLemmatizer()


# In[10]:


##with respect to noun
lemmatizer.lemmatize("going")


# from the above we could understand that it is trying to find out the root word 
# 
# about the function of the lemmatization
# #lemmatizer.lemmatize(word,pos='n')
# n basically means the word actually i am passing it is being treated as noun("going")
# 
# different pos tags :
# -->Noun-n
# -->Verb-v
# -->adjective-a
# -->adverb-r

# In[11]:


##with respect to verb
lemmatizer.lemmatize("going",pos='v')


# In[12]:


words=["eating","eats","eaten","writing","writes","programming","programs","history","finally","finalized"]


# In[14]:


##for each and every word lemmatization is going to be applied
##by default the pos tag is noun 
for word in words:
    print(word+"----->"+lemmatizer.lemmatize(word,pos='n'))


# In[15]:


##for each and every word lemmatization is going to be applied
##by default the pos tag is verb
for word in words:
    print(word+"----->"+lemmatizer.lemmatize(word,pos='v'))


# In[16]:


##for each and every word lemmatization is going to be applied
##by default the pos tag is adjective
for word in words:
    print(word+"----->"+lemmatizer.lemmatize(word,pos='a'))


# In[18]:


##now lets try the problem that we've faced with the stemming
lemmatizer.lemmatize("goes",pos='v')


# In[19]:


lemmatizer.lemmatize("fairly",pos='v'),lemmatizer.lemmatize("sprotingly")


# This is just tell you that how good the lemmatizer is... as it is giving the correct form of the word
# 
# but the question is which will take more time?
# wornet or stemming?
# The answer is Wordnet lemmatizer 
# If we have a big para it will consume time 
# This is the difference btw the stemming and the lemmatizer 
# 
# use cases:
# Q&A
# chatbot
# text summarization 
# 

# In[ ]:




