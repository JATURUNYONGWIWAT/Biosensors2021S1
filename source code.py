# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 09:56:24 2021

@author: ja-14
"""



import pandas as pd
import matplotlib.pyplot as plt


df2 =pd.read_excel("folder1/store.xlsx")       
x = df2["DATE"]
y = df2["store1"]
z = df2["store2"]
a = df2["store3"]
b = df2["store4"]
c = df2["store5"]
plt.figure(figsize=(10, 6))
plt.plot(x,y ,label = "store1")
plt.plot(x,z ,label = "store2")
plt.plot(x,a ,label = "store3")
plt.plot(x,b ,label = "store4")
plt.plot(x,c ,label = "store5")
plt.xlabel('DATE')
plt.title('Amount of oximeter sold')
plt.legend()


Death =pd.read_excel("folder1/Death.xlsx")       
x = Death["DATE"]
y = Death["Death"]
plt.figure(figsize=(10, 6))
plt.grid(axis = 'y')
plt.plot(x,y, color ='red')
plt.xlabel('DATE')
plt.ylabel('Number of death')
plt.title('Death')


Deathslide =pd.read_excel("folder1/Deathslide.xlsx")       
x1 = Deathslide["DATE"]
y1 = Deathslide["Death"]
plt.figure(figsize=(10, 6))
plt.grid(axis = 'y')
plt.plot(x1,y1, color ='red')
plt.xlabel('DATE')
plt.ylabel('Number of death')
plt.title('Death')



severelyill =pd.read_excel("folder1/severely ill.xlsx")       
x2 = severelyill["DATE"]
y2 = severelyill["severely ill"]
plt.figure(figsize=(10, 6))
plt.grid(axis = 'y')
plt.plot(x2,y2)
plt.xlabel('DATE')
plt.ylabel('Number of severely ill')
plt.title('severely ill')

ventilator =pd.read_excel("folder1/ventilator.xlsx")       
x3 = ventilator["DATE"]
y3 = ventilator["ventilator"]
plt.figure(figsize=(10, 6))
plt.grid(axis = 'y')
plt.plot(x3,y3)
plt.xlabel('DATE')
plt.ylabel('Use of ventilator')
plt.title('Ventilator')

Fieldhospital =pd.read_excel("folder1/Field hospital.xlsx")       
x4 = Fieldhospital["DATE"]
y4 = Fieldhospital["Field hospital"]
plt.figure(figsize=(10, 6))
plt.plot(x4,y4, color ='green')
plt.grid(axis = 'y')
plt.xlabel('DATE')
plt.ylabel('Number of Field hospital')
plt.title('Field hospital')

Homeorcommunity =pd.read_excel("folder1/Home or community.xlsx")     
x5 = Homeorcommunity["DATE"]
y5 = Homeorcommunity["Home/community"]
plt.figure(figsize=(10, 6))
plt.plot(x5,y5, color ='green')
plt.grid(axis = 'y')
plt.xlabel('DATE')
plt.ylabel('Number of home/community isolation')
plt.title('Home/community isolation')


Homeorcommunity =pd.read_excel("folder1/Home or community.xlsx")       
x6 = Homeorcommunity["DATE"]
y6 = Homeorcommunity["Home/community"]
plt.figure(figsize=(10, 6))
plt.grid(axis = 'y')
plt.plot(x6,y6, color ='red',label = "Home/community isolation")
Fieldhospital =pd.read_excel("folder1/Field hospital.xlsx")       
x7 = Fieldhospital["DATE"]
y7 = Fieldhospital["Field hospital"]
plt.plot(x7,y7, color ='green',label = "Field hospital")
plt.xlabel('DATE')
plt.title('Comparison between field hospital and home/community isolation')
plt.legend()





    
    
    
    
    
    
    
    
    
    
    
    
    
    