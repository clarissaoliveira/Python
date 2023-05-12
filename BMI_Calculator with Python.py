#!/usr/bin/env python
# coding: utf-8

# In[11]:


name = input("Enter your name: ")

weight = int(input("Enter your weight in pounds: "))

height = int(input("Enter your height in inches: "))

BMI = (weight * 703) / (height * height)

print(BMI)

if BMI > 0:
    if(BMI<18.5):
        print(name + ", you are underweight.")
    elif(BMI<=24.9):
        print(name + ", you are normal weight.")
    elif(BMI<29.9):
        print(name + ", you are overweight.")
    elif(BMI<34.9):
        print(name + ", you are obese.")
    elif(BMI<39.9):
        print(name + ", you are severely obese.")
    else:
        print(name + ", you are morbidly obese.")
else:
    print("Enter valid input")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


Underweight = <18.5
Normal weight = 18.5–24.9
Overweight = 25–29.9
Obesity = BMI of 30 or greater


# In[10]:


if BMI > 0:
    if(BMI<18.5):
        print(name + ", you are underweight.")
    elif(BMI<=24.9):
        print(name + ", you are normal weight.")
    elif(BMI<29.9):
        print(name + ", you are overweight.")
    elif(BMI<34.9):
        print(name + ", you are obese.")
    elif(BMI<39.9):
        print(name + ", you are severely obese.")
    else:
        print(name + ", you are morbidly obese.")
else:
    print("Enter valid input")

