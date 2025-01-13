#!/usr/bin/env python
# coding: utf-8

# In[12]:


get_ipython().system('pip install nltk')


# In[15]:


##Tokenixation
##sentence-->paragraphs

import nltk
from nltk.tokenize import sent_tokenize


# In[21]:


for sentence  in documents:
    print(sentence)


# In[22]:


##Tokenization
##paragraph --->words
##sentences --->words
from nltk.tokenize import word_tokenize


# In[23]:


word_tokenize(corpus)


# why we are converting into words? 
# because everyword have it's different importance.And we need to preprocess it on the top of it.That is the reson why we focus on each and every word
# 
# 
# 
# NOTE: The only thing is that the words like "Kavya's" is considering as two words "Kavya" , "'s" both seperately

# In[26]:


##word tokenize on sentences
for sentence in documents:
    print(word_tokenize(sentence))


# In[27]:


##another thing called wordpunkt tokenize

from nltk.tokenize import wordpunct_tokenize


# In[28]:


wordpunct_tokenize(corpus)


# NOTE: puncuations is also splitted . it make sure that Puncuations is also considered as a seperate word

# In[29]:


from nltk.tokenize import TreebankWordTokenizer


# In[30]:


tokenizer=TreebankWordTokenizer()


# In[31]:


tokenizer.tokenize(corpus)


# NOTE: In this full stop will not be consider as a seperate word only for the last word it will be considering as a seperate word other than that it will be considering the full stop as a part of the word.Only this is the difference with res
