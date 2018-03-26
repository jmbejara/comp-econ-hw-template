
# coding: utf-8

# In[1]:


import numpy as np
from matplotlib import pyplot as plt


# In[2]:


x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)
plt.plot(x, y)

