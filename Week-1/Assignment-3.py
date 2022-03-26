#!/usr/bin/env python
# coding: utf-8

# In[1]:


def find_max(array):
    max = array[0]
    for y in array:
        if y > max:
            max=y
    return max


# In[2]:


#test
print(find_max([1, 2, 4, 5]) ); # should print 5
print(find_max([5, 2, 7, 1, 6]) ); # should print 7


# In[3]:


def find_position(array, num):
    pos=-1
    target=num
    loop=0
    for x in array:
        if x!=target:
            loop=loop+1
        else:
            pos=loop
            return pos
            break
    if pos==-1:
        return pos


# In[4]:


#test
print(find_position([5, 2, 7, 1, 6], 5)) # should print 0
print(find_position([5, 2, 7, 1, 6], 7)) # should print 2
print(find_position([5, 2, 7, 7, 7, 1, 6], 7)) # should print 2 (the first one)
print(find_position([5, 2, 7, 1, 6], 8)) # should print -1


# In[ ]:




