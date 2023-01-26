#!/usr/bin/env python
# coding: utf-8

# # Find the squares from the given list , write a python program to square the element of a list using map() function

# In[3]:


def square_num(n):
    return n*n
nums = [4,5,2,9]
result = map(square_num, nums)
print("square the elements of the list using map():")
print(list(result))


# In[ ]:




