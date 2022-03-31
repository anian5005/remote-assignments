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


# In[4]:


#test

input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x']

count(input1)  # should print {'a': 3, 'b': 1, 'c': 2, 'x': 1}


# In[11]:


#PART2 group_by_key

def get_key_list(input):
    key_list=[]
    for w in input[0].keys():
        key_list.append(w) 
    return key_list

def group_by_key(input):
    dif_list={}
    list = get_key_list(input)

    for item in input:
        key = item[list[0]]
        value = item[list[1]]
        dif_list[key]=dif_list.get(key,0)+value
    return dif_list


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


# In[15]:


#dict 用法
k = {}

k = dict({"3":0}) #建立新dict 再次dict()會被蓋掉

print(k)

k.update(dict({3:4})) #更新內容或新增

print(k)

k = dict({5:5})
k = dict({5:6})

print(k)


# In[15]:


#注意
#dict()括弧內任何直接成為 key 無法放入變數
input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x']


list_2={}
for i in input1:
    list_2 = dict(i=0) #錯誤寫法
print(list_2) #{'i': 0}     "i"直接被鍵入字典


# In[ ]:




