#!/usr/bin/env python
# coding: utf-8

# In[2]:


if 5>2:
    print("five is greater than two")


# In[3]:


x=5
print(x)


# In[4]:


x=4
x="ABHI"
print(str(x))


# In[6]:


x=4
x="ABHI"
print(x)


# In[8]:


x=4
y="ABHI"
print(type(x))
print(type(y))


# In[10]:


fruits = ("apple", "banana", "cherry")
x, y, z = fruits
print(x)
print(y)
print(z)


# In[14]:


x = "awesome"


x = "fantastic"
print("Python is " + x)



print("Python is " + x)


# In[18]:


def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


# In[19]:


x = {"name" : "John", "age" : 36}
print(type(x))


# In[20]:


x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


# In[24]:


import random as rd #print random number in the range

print(random.randrange(1, 10))


# In[26]:


a = '''Krishna is my name'''
print(a)


# In[28]:


a = (2,5,1,8,2,5)
print(a[1])


# In[ ]:




