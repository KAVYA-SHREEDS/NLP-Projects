#!/usr/bin/env python
# coding: utf-8

# In[1]:


## Speech Of DR APJ Abdul Kalam
paragraph = """I have three visions for India. In 3000 years of our history, people from all over
               the world have come and invaded us, captured our lands, conquered our minds.
               From Alexander onwards, the Greeks, the Turks, the Moguls, the Portuguese, the British,
               the French, the Dutch, all of them came and looted us, took over what was ours.
               Yet we have not done this to any other nation. We have not conquered anyone.
               We have not grabbed their land, their culture,
               their history and tried to enforce our way of life on them.
               Why? Because we respect the freedom of others.That is why my
               first vision is that of freedom. I believe that India got its first vision of
               this in 1857, when we started the War of Independence. It is this freedom that
               we must protect and nurture and build on. If we are not free, no one will respect us.
               My second vision for India’s development. For fifty years we have been a developing nation.
               It is time we see ourselves as a developed nation. We are among the top 5 nations of the world
               in terms of GDP. We have a 10 percent growth rate in most areas. Our poverty levels are falling.
               Our achievements are being globally recognised today. Yet we lack the self-confidence to
               see ourselves as a developed nation, self-reliant and self-assured. Isn’t this incorrect?
               I have a third vision. India must stand up to the world. Because I believe that unless India
               stands up to the world, no one will respect us. Only strength respects strength. We must be
               strong not only as a military power but also as an economic power. Both must go hand-in-hand.
               My good fortune was to have worked with three great minds. Dr. Vikram Sarabhai of the Dept. of
               space, Professor Satish Dhawan, who succeeded him and Dr. Brahm Prakash, father of nuclear material.
               I was lucky to have worked with all three of them closely and consider this the great opportunity of my life.
               I see four milestones in my career"""


# In[4]:


import nltk
from nltk.corpus import stopwords
sentences=nltk.sent_tokenize(paragraph)


# In[5]:


sentences


# In[7]:


nltk.download('averaged_perceptron_tagger')


# In[8]:


## we will find the Pos Tag

for i in range(len(sentences)):
    words=nltk.word_tokenize(sentences[i])
    words=[word for word in words if word not in set(stopwords.words('english'))]
    pos_tag=nltk.pos_tag(words)
    print(pos_tag)
    #pos tag is shown below


# In[9]:


"Taj Mahal is a beautiful Monument".split()


# In[11]:


print(nltk.pos_tag("Taj Mahal is a beautiful Monument".split()))


# In[12]:


get_ipython().system('pip install pandas')


# In[13]:


import pandas as pd

# Data for the table
data = {
    "POS Tag": ["PRP", "CD", "NNS", "NNP", ".", "IN", "NN", "VBP", "VBN", "VBD", "JJ", "RB", "WRB", "MD", "VB", "DT", "PRP$", "VBG", "VBZ"],
    "Full Form": [
        "Personal Pronoun", 
        "Cardinal Number", 
        "Noun, Plural", 
        "Proper Noun, Singular", 
        "Punctuation Mark", 
        "Preposition or Subordinating Conjunction", 
        "Noun, Singular", 
        "Verb, Present Tense", 
        "Verb, Past Participle", 
        "Verb, Past Tense", 
        "Adjective", 
        "Adverb", 
        "Wh-Adverb", 
        "Modal Verb", 
        "Verb, Base Form", 
        "Determiner", 
        "Possessive Pronoun", 
        "Verb, Gerund or Present Participle", 
        "Verb, Present Tense, 3rd Person Singular"
    ],
    "Description": [
        "Refers to a person or object.",
        "Represents numbers (used as adjectives or nouns).",
        "Plural form of a noun.",
        "Singular proper noun (specific names).",
        "Indicates the end of a sentence or a statement.",
        "Links nouns to other words or introduces clauses.",
        "Singular form of a noun.",
        "Present tense verb (non-3rd person singular).",
        "Past participle of a verb.",
        "Simple past tense verb.",
        "Describes or modifies a noun.",
        "Describes or modifies a verb, adjective, or another adverb.",
        "Introduces questions.",
        "Indicates mood or tense (possibility, necessity, permission).",
        "Base form of a verb (infinitive without 'to').",
        "Introduces a noun.",
        "Shows possession or ownership.",
        "Gerund (verb ending in -ing) or present participle.",
        "Present tense verb for 3rd person singular."
    ],
    "Example": [
        "`I`, `we`, `us`",
        "`three`, `3000`, `four`",
        "`visions`, `years`, `nations`",
        "`India`, `Alexander`, `British`",
        "`.` (period)",
        "`in`, `from`, `because`",
        "`history`, `nation`, `opportunity`",
        "`believe`, `consider`",
        "`invaded`, `done`, `recognised`",
        "`captured`, `succeeded`, `grabbed`",
        "`great`, `self-reliant`, `developed`",
        "`yet`, `closely`, `also`",
        "`why`",
        "`must`, `would`, `can`",
        "`protect`, `see`, `stand`",
        "`both`, `the`",
        "`my`, `our`",
        "`developing`, `falling`",
        "`stands`"
    ]
}

# Create the dataframe
df = pd.DataFrame(data)

# Display the table
display(df)


# In[ ]:




