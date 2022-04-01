#!/usr/bin/env python
# coding: utf-8

# In[2]:


def avg(data):
    key = list(data.keys())[0] #除了list有其他方法嗎? #只能適用單一結構嗎?
    products = data[key]
    all_num = len(products)
    #print(products)

    all_price = 0
    for product in products:
        price = product['price']
        all_price = all_price + price

    avg = round(all_price/all_num, 3)
    print(avg)


# In[3]:


avg({
 "products": [
 {
 "name": "Product 1",
 "price": 100
 },
 {
 "name": "Product 2",
 "price": 700
 },
 {
 "name": "Product 3",
 "price": 300
 }
 ]
 })


# In[ ]:





# In[ ]:




