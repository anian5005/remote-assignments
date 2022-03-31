#!/usr/bin/env python
# coding: utf-8

# In[3]:


def avg(data):
    key = list(data.keys())[0] #除了list有其他方法嗎? #只能適用單一結構嗎?
    products = data[key]
    print(products)

    all_price = 0
    for product in products:
        price = product['price']
        all_price = all_price + price

    avg = round(all_price/3, 3)
    print(avg)


# In[2]:


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


# In[4]:


#product = ["Product 1","Product 1","Product 2"]

price = [100,700,300]
    
product={product,price}

print(product)
product = ["Product 1","Product 1","Product 2"]
price = [100,700,300]
    
    
product={product,price}

print(product)


# In[ ]:




