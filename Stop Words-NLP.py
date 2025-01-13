#!/usr/bin/env python
# coding: utf-8

# In[20]:


##Speech Of DR APJ Abdul Kalam 
paragraph = """I have three visions for India. In 3000 years of our history, people from all over the world have come and invaded us, captured our lands, conquered our minds. From Alexander onwards, the Greeks, the Turks, the Moguls, the Portuguese, the British, the French, the Dutch, all of them came and looted us, took over what was ours. Yet we have not done this to any other nation. We have not conquered anyone. We have not grabbed their land, their culture, their history and tried to enforce our way of life on them. Why? Because we respect the freedom of others.That is why my first vision is that of freedom. I believe that India got its first vision of this in 1857, when we started the War of Independence. It is this freedom that we must protect and nurture and build on. If we are not free, no one will respect us. My second vision for India’s development. For fifty years we have been a developing nation. It is time we see ourselves as a developed nation. We are among the top 5 nations of the world in terms of GDP. We have a 10 percent growth rate in most areas. Our poverty levels are falling. Our achievements are being globally recognised today. Yet we lack the self-confidence to see ourselves as a developed nation, self-reliant and self-assured. Isn’t this incorrect? I have a third vision. India must stand up to the world. Because I believe that unless India stands up to the world, no one will respect us. Only strength respects strength. We must be strong not only as a military power but also as an economic power. Both must go hand-in-hand. My good fortune was to have worked with three great minds. Dr. Vikram Sarabhai of the Dept. of space, Professor Satish Dhawan, who succeeded him and Dr. Brahm Prakash, father of nuclear material. I was lucky to have worked with all three of them closely and consider this the great opportunity of my life. I see four milestones in my career"""


# In[21]:


import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


# In[22]:


nltk.download('stopwords')
nltk.download('punkt')


# In[23]:


stemmer = PorterStemmer()


# from this we could see some words like i,the,have,and,you,know,to there,why,when all this words will not play a very big role when we are doing task like spam/Ham classification and along with that to see that it is positive review or negative review so with the help of stop words we could able to remove these kind of words because with this kind of use cases where you're specifically focusing on some of the important words to determine the output these will not be helpful.
# 
# 
# so we can pass the entire paragraph to that particular stop words and see that what all words can be basically removed and that is the importance of stop words in short 

# Along with the stop words we can also apply stemming 

# In[24]:


stopwords.words('english')


# In[25]:


##we can also see the stop wprds for other languages also 
stopwords.words('french')


# In[26]:


##apply stemming
from nltk.stem import PorterStemmer


# In[27]:


stemmmer=PorterStemmer()


# In[28]:


nltk.download('punkt')


# In[29]:


#tokenization process wherein we take the entire paragraph and divide it into sentences
sentences=nltk.sent_tokenize(paragraph)


# In[30]:


##type of the sentences
type(sentences)


# In[31]:


##traverse through all the sentences
##first of all apply the stop words which all the words not present in the stop words we are only going to take that and apply stemming 
##apply stopwords and filter and then apply stemming

for i in range(len(sentences)):
    words=nltk.word_tokenize(sentences[i])
    #stemming is applied only if that particular word is not a stop word
    words=[stemmer.stem(word) for word in words if word.lower() not in set(stopwords.words('english'))]
    sentences[i]=' '.join(words) #convertong all the list of wordsinto sentences
   


# In[32]:


sentences


# Now if we see the result the stemming is not very good
# so trying snowball stemmer

# In[33]:


from nltk.stem import SnowballStemmer


# In[34]:


snowballstemmer=SnowballStemmer('english')


# In[35]:


##traverse through all the sentences
##first of all apply the stop words which all the words not present in the stop words we are only going to take that and apply stemming 
##apply stopwords and filter and then apply snowballstemming

for i in range(len(sentences)):
    words=nltk.word_tokenize(sentences[i])
    #stemming is applied only if that particular word is not a stop word
    words=[snowballstemmer.stem(word) for word in words if word.lower() not in set(stopwords.words('english'))]
    sentences[i]=' '.join(words) #convertong all the list of wordsinto sentences
   


# In[36]:


sentences


# In[37]:


from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()


# In[40]:


##traverse through all the sentences
##first of all apply the stop words which all the words not present in the stop words we are only going to take that and apply stemming 
##apply stopwords and filter and then apply snowballstemming

for i in range(len(sentences)):
    words=nltk.word_tokenize(sentences[i])
    #stemming is applied only if that particular word is not a stop word
    words=[lemmatizer.lemmatize(word,pos='v') for word in words if word.lower() not in set(stopwords.words('english'))]
    sentences[i]=' '.join(words) #convertong all the list of wordsinto sentences
   


# In[41]:


sentences


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




