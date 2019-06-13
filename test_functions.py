
# coding: utf-8

# In[12]:


"""Test for functions.
"""

from my_module.my_functions import selector, prepare_text, end_chat
import pytest


# In[13]:


def selector_test():
    
    assert callable(selector)
    assert selector(['in', 'words'], ['words'], ['yes'], 'aditi') == 'yes'
    assert selector(['in', 'words'], ['out'], ['yes'], 'aditi') == None


# In[14]:


def prepare_text_test():

    assert prepare_text('Hi! I Am Stressed') == ['hi', 'i', 'am', 'stressed']


# In[15]:


def end_chat_test():
    
    assert callable(end_chat)
    assert isinstance(end_chat(['stressed', 'great']), bool)
    assert end_chat(['quit']) == True

