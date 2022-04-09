#!/usr/bin/env python
# coding: utf-8
# Assignment 5: Algorithm Practice (Advanced Optional)# For example:
 twoSum([2, 7, 11, 15], 9);
 Should returns:
 [0, 1]
 Because:
 nums[0] + nums[1] is 9
'''
def twoSum(nums, target):
 # your code her
# In[26]:


def twoSum(nums, target):
    result= []
    leng = len(nums)
    
    for x,i in enumerate(nums):
        #print("++++++++num_one++++++++++",i)
        pos_one = x
        num_one = i
        pos_two = x+1 #num_two 起始值
      
        if num_one <= target: #如果單一數字已超過 target 不計算
            for y,j in enumerate(nums[x+1:]): #num_two 只從 num_one 往後找組合，避免重複
                num_two = j
                #print("num_two",num_two)
                
                if  num_two <= target: #如果單一數字已超過 target 不計算
                    total = num_one + num_two
                    #print("total",total)

                    if total == target:
                        result.append(pos_one)
                        result.append(pos_two)
                        #print("Hit!")
                #else:
                     #print('dont need to count')
                        
                pos_two = pos_two +1 #num_two 右移一位
                
            #print('--------------------')
            
    if result == []:
        return None
    else:
        return result


# In[30]:


#print( twoSum([2, 7, 11, 15], 9) ) #Should returns:[0, 1]
#print( twoSum([2, 7, 1, 8], 4) ) #Should returns:None
#print( twoSum([2, 7, 1, 8], 9) ) #Should returns:[0, 1, 2, 3] 兩組
