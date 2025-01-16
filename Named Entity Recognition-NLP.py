#!/usr/bin/env python
# coding: utf-8

# In[14]:


sentence="The Eiffel Tower was built from 1887 to 1889 by Gustave Eiffel, whose company specialized in building metal frameworks and structures."
"""
Person Eg:Krish C Naik
Place or Location Eg:India
Date Eg: September,24-09-1989
Time Eg:4:30pm
Money Eg:1 million dollar
Organization Eg: iNeuron Private Limited
Percent Eg: 20%,twenty percent
"""


# In[15]:


sentence="The Eiffel Tower was built from 1887 to 1889 by Gustave Eiffel, whose company specialized in building metal frameworks and structures."


# In[16]:


import nltk
words=nltk.word_tokenize(sentence)


# In[17]:


tag_elements=nltk.pos_tag(words)


# In[18]:


nltk.download('maxent_ne_chunker')


# In[19]:


nltk.download('words')


# In[ ]:


nltk.ne_chunk(tag_elements).draw() #name entity chunker


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




