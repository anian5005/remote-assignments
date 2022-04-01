#!/usr/bin/env python
# coding: utf-8
Assignment 4: Algorithm Practice (Advanced Optional)
# In[1]:


#輔助 function
#輸入 array 回傳查詢定位點，接近中間值

# find array next finding position

def find_center(numbers):
    
    length = len(numbers)
    #print(length)
    
    if length == 1:
        pos = 0
        
    elif length%2 == 1:   #length is odd
        pos = int(length//2+1)
        
    else:              #length is even 選擇偏左後一位
        pos = int(length/2)
        #print(pos)
        
    value = numbers[int(pos)]
    return pos,value          # 回傳 中間位置、中間數值


numbers = [1, 2, 3, 4, 5, 6]

x,y = find_center(numbers)
print(x)
print(y)


# In[2]:


#輔助 function
#輸入長度 回傳至下一個定位點之移動距離

def move_len(length):
    
    result_len = length
    
    if length == 1:
        result_len = 1
        
    elif length%2 == 1:   #length is odd
        result_len = int(length//2+1)
        #print("odd")
        
    else:              #length is even 選擇偏左後一位
        result_len = int(length/2)+1
        #print(pos)
        #print("even")
    return result_len


numbers = [1, 2, 3, 4, 5, 6]

print(move_len(1)) # should print 1
print(move_len(5)) # should print 3
print(move_len(6)) # should print 4


# In[3]:


def binary_search_position(numbers, target):
    
    find,center_value = find_center(numbers) #find 為每次查詢的定位點 #move_len 為移動至下一個定位點之距離
    
    array = numbers # array 為每次查詢後，縮小範圍的 array，初值為 input 的 numbers
    
    while len(array) >= 1:
        

        if target == numbers[find]:
            #print("命中")
            return find
           #print("array",array)
            break
            
        elif  target > numbers[find]: # target 在左邊
            #print("左邊")
            array = numbers[find+1:]
           
            find = find +  move_len(len(array))
            
            #print("find",find)
            #print("array",array)

        else:
            #print("右邊")
            array = numbers[:find]
            find = find - move_len(len(array))
            
            #print("array",array)
        #print("---------------------------")
        
    return -1
            
    

print(binary_search_position([1, 2, 3, 4, 5 ],5)) # should print 4
print(binary_search_position([1, 2, 5, 6, 7], 8)) # should print -1
print(binary_search_position([1, 2, 5, 6, 7], 1)) # should print 0
print(binary_search_position([1, 2, 5, 6, 7], 6)) # should print 3


# In[5]:


#test
numbers = [1, 2, 3, 4, 5 ,6]

numbers[2:] #起始位置 : 最後位置+1

