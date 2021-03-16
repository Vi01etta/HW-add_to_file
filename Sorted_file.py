#!/usr/bin/env python
# coding: utf-8

# In[6]:


with open('1.txt', 'r') as a:
  text = a.read()
  a.seek(0)
  lines1 = a.readlines()
  size1 = len(lines1)
  
tuple1 = ('\n1.txt\n', str(size1), '\n', text)

with open('2.txt', 'r', encoding = 'utf-8') as b:
  text = b.read()
  b.seek(0)
  lines2 = b.readlines()
  size2 = len(lines2)


tuple2 = ('2.txt\n', str(size2), '\n', text)

with open('3.txt', 'r', encoding = 'utf-8') as c:
  text = c.read()
  c.seek(0)
  lines3 = c.readlines()
  size3 = len(lines3)
  
tuple3 = ('\n3.txt\n', str(size3), '\n', text)


tuple_list = [tuple2, tuple1, tuple3]


new_file = open ('4.txt', 'w')


for tuples in tuple_list:
  for text_values in tuples:
    print(text_values)
    new_file.write(text_values)
    
new_file.close()


# In[ ]:





# In[ ]:





# In[ ]:




