#!/usr/bin/env python
# coding: utf-8

# In[29]:


def revword(word):
    return word[::-1].lower()


def countword():
    with open('text.txt', 'r') as file_handler:
        my_file = file_handler.read().split()
        word = my_file[0].lower()
        wordCounter = 1
        for w in my_file[1:]:
            if revword(w) == word:
                wordCounter += 1
    return wordCounter


# In[ ]:




