#!/usr/bin/env python
# coding: utf-8

# In[2]:


#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("""**********************************

2. cikarma islemi.

3. carpma islemi.

4. bolme islemi.
***********************************
""")
a = int(input("Birinci Sayi:"))
b = int(input("ikinci Sayi:"))

işlem = input("islemi giriniz:")

if işlem == "1":
    print("{} ile {} in toplami {} dir".format(a,b,a+b))
    
elif işlem == "2":
    print("{} ile {} in farki {} dir".format(a,b,a-b))
    
elif işlem =="3":
    print("{} ile {} in carpimi {} dir".format(a,b,a * b))
    
elif işlem =="4":
    print("{} ile {} carpimi {} dir".format(a,b, a / b))
    
else:
    print("gecersiz islem")
    


# In[ ]:


# In[ ]:




