#!/usr/bin/env python
# coding: utf-8

# # QTM 385
# 
# ***
# 
# ## Homework 2
# 
# Student: Mina Lee[2298297]

# In this homework we will create a text scrambler. The idea is that the user is going to input some text, and we will scramble the letters in the text. Each question will guide you up to the desired result.

# 
# ***
# 
# ### Question 1
# 
# Suppose that you have a string `S = 'My beautiful string'`. Show that you can transform your string into a list by applying the command `list(S)` to it.

# In[1]:


# Your answer here
S='My beautiful string'
list(S)


# 
# ***
# 
# ### Question 2
# 
# If you have a list, you can put the elements together forming a string if you do the following:
# 
# ```
# L = ['1', '2', '3', '4', '5', '6']
# ''.join(L)
# ```
# 
# Try for the list in this example. Try also for the list below:
# 
# ```
# L2 = ['a', '2', 'c', '4', 'e', '6']
# ```

# In[5]:


# Your answer here
L2 = ['a', '2', 'c', '4', 'e', '6']
' '.join(L2)


# 
# ***
# 
# ### Question 3
# 
# If you have a list of objects, we learned how to select one using the function `choice` in the `random` module. This module has also a function `sample`, where you can select one or more elements from a list or tuple. Suppose we have a list `L` with elements, and that we imported the module as `rd` (see previous homework). The syntax for selecting three elements there is:
# 
# ```
# rd.sample(L, 3)
# ```
# 
# Now, from the following list:
# 
# ```
# preferred_food = ['pizza', 'ice cream', 'salad']
# ```
# 
# Select two favorite foods to eat.

# In[7]:


# Your answer here
preferred_food = ['pizza', 'ice cream', 'salad']
import random as rd
rd.sample(preferred_food,2)


# 
# ***
# 
# ### Question 4
# 
# To get the user's input, we can use the function `input()`. The syntax is simple: `variable_saving = input('Prompt here: ')`. Use the function below to save the input in the variable `my_entry`. As a prompt, use the phrase 'Enter your text here: '. Print the text typed by the user.

# In[9]:


# Your answer here
my_entry = input('Enter your text here: ')
print(my_entry)


# 
# ***
# 
# ### Question 5
# 
# Now, build your scrambler. Assume the user will enter a word, or a name, or even a phrase. Scramble it and return the input scrambled after the user type it.

# In[2]:


# Your answer here
import random as rd
my_entry = input('Enter your text here: ')
scrambler = rd.sample(my_entry, len(my_entry))
scramblercombined = ''.join(scrambler)
print(scramblercombined)


# **That's all, folks!**
