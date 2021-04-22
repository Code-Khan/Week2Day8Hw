#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def shoppingcart():
    cart={}
    while True:
        action = input("Add Item?, Delete Item?, Quit?, Checkout? ")
        if action == "Add Item":
            item = input("What item would you like to add? ")
            cart[item]= 1
        if action == "Delete Item":
            item = input("What item would you like to delete? ")
            cart[item]= cart[item] -1
        if action == "Quit":
            break
        if action == "Checkout":
            
            print(cart)
            
shoppingcart()
        
        
    


# In[ ]:


shoppingcart()


# In[18]:


import shopping.ipynb


# In[ ]:




