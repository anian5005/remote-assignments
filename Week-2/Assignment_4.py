#!/usr/bin/env python
# coding: utf-8

# In[1]:


#PART1 count #v1
def count(input):
    
    count_list={}

    for i in input:
    
        if i not in count_list:# 如果在 dict 中找不到 i
            count_list.update({i:1}) #新增 i
        else:
            value = count_list.get(i,0) #如果找得到
            count_list.update({i:value+1}) # value +1
            print(count_list)
    return(count_list)


# In[2]:


#PART1 count  #v2
input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x']

count_list={}

for i in input1:
    if count_list.get(i,0) == 0:
        count_list[i]=1
    else:
        value = count_list.get(i,0)
        count_list[i] = value+1
print(count_list)


# In[3]:


#PART1 count  #v3
def count(input):
    count_list={}
    for i in input1:
        count_list[i] = count_list.get(i,0)+1  #dict[key]=1 建立新dict item
    print(count_list)


# In[14]:


#PART1 count  #v4 
#defaultdict 建立 default值

from collections import defaultdict

def count(input):
    count_list =defaultdict()
    for i in input:
        value = count_list.get(i,0)
        count_list.update({i:value+1})
    
    return count_list


# In[15]:


#test

input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x']

print(count(input1))  # should print {'a': 3, 'b': 1, 'c': 2, 'x': 1}


# In[6]:


#PART2 group_by_key #V1

def get_key_list(input):
    key_list=[]
    for w in input[0].keys():
        key_list.append(w) 
    return key_list

def group_by_key(input):
    dif_list={}
    list = get_key_list(input)
    print(list)

    for item in input:
        key = item[list[0]]
        value = item[list[1]]
        dif_list[key]=dif_list.get(key,0)+value
    return dif_list


# In[13]:


#PART2 group_by_key  #V2
#defaultdict 建立 default值

from collections import defaultdict

def get_key_list(input):
    key_list=[]
    for w in input[0].keys():
        key_list.append(w) 
    return key_list

def group_by_key(input):
    list = get_key_list(input)
    merge_list = defaultdict()
    
    for item in input:
        key = item[list[0]]
        value = item[list[1]]
        new_value = merge_list.get(key,0) + value
        merge_list.update({key:new_value})           
    return merge_list


# In[12]:


#test

input2 = [
 {'key': 'a', 'value': 3},
 {'key': 'b', 'value': 1},
 {'key': 'c', 'value': 2},
 {'key': 'a', 'value': 3},
 {'key': 'c', 'value': 5}
]

print(group_by_key(input2))     # should print {‘a’: 6, ‘b’: 1, ‘c’: 7}




