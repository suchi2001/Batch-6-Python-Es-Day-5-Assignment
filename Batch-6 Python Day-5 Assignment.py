#!/usr/bin/env python
# coding: utf-8

# In[80]:


print("Question 1:")


# In[4]:


def move_zero(num_list):
    a=[0 for i in range(num_list.count(0))]
    x=[i for i in num_list if i !=0]
    x.extend(a)
    return(x)
b=[0,1,2,10,4,1,0,56,0,1,3,0,56,0,4]
c=b.sort()
print(move_zero(b))


# In[82]:


print("Question 2:")


# In[69]:


list1 = [10,20,40,60,80] 
list2 = [5,15,25,35,45,60] 
print ("The original list 1 is : " + str(list1)) 
print ("The original list 2 is : " + str(list2)) 
size_1 = len(list1) 
size_2 = len(list2) 
res = [] 
i, j = 0, 0

while i < size_1 and j < size_2: 
    if list1[i] < list2[j]: 
     res.append(list1[i]) 
     i += 1

    else: 
     res.append(list2[j]) 
     j += 1

res = res + list1[i:] + list2[j:] 
print ("The combined sorted list is : " + str(res)) 

