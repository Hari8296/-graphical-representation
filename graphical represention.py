# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 14:09:35 2022

@author: haris
"""

import pandas as pd

import matplotlib.pyplot as plt
import scipy.stats as skew

# Q1 ) Calculate Skewness, Kurtosis using PYHTON 

a :-

data =pd.read_csv("D:/assignments of data science/graphical representation/Day04_Assignment_Datasets/Q1_a.csv")
data

plt.hist(data.speed)
plt.hist(data.dist)

SKEWNESS 

data.skew()

speed = -0.117510
dist = -0.806895

KURTOSIS 

data.kurt()

speed = -0.508994
dist = 0.405053

b:-

data1=pd.read_csv("D:/assignments of data science/graphical representation/Day04_Assignment_Datasets/Q2_b.csv")
data1

plt.hist(data1.SP)
plt.hist(data1.WT)
SKEWNESS 
data1.skew()

sp = 1.611450
wt = -0.614753

KURTOSIS 
data1.kurt()

sp = 2.977329
wt = 0.950291


Q2

ANS:- positive skewed 

Q3

a

import statistics as st
list=[34,36,36,38,38,39,39,40,40,41,41,41,41,42,42,45,49,56]

a = st.mean(list)
a
mean= 41

b = st.median(list)
b
median=40.5

c= st.variance(list)
c
variance = 25.52

d=st.stdev(list)
d
d=standard deviation = 5.05

b

2)	What can we say about the student marks
ANS:- scors are in ascending order

Q4

What is the nature of skewness when mean, median of data is equal?
ANS:- normalized skewness 

Q5

What is the nature of skewness when mean > median?
ANS:-right skewness 

Q6

What is the nature of skewness when median > mean?
ANS:- left skewness 

Q7

What does positive kurtosis value indicates for a data?
ANS:-sharp peak in the plot less gap b/w tails to x-axis

Q8

What does negative kurtosis value indicates for a data?
ANS:- Border peak under the curve & more gap between tails to x-axis

Q9

A:- What can we say about the distribution of the data?
ANS:- The data is distributed in de-assigned format

B:- What is nature of skewness of the data?
ANS:-left side skewed 

C:- What will be the IQR of the data (approximately)? 
ANS:-18-10
8 is IQR

Q10

1 bar plot is with range of 3
2 bar plot is with range of 1.5

Q11

 1
ANS:-IQR=Q3-Q1
        =13-5
        =7
   
 2
ANS:-the data is positive skwed

 3
ANS:-may be 3 

Q12

 1 Where would the mode of this dataset lie? 
ANS:- 7

 2 Comment on the skewness of the dataset
ANS:- right skewed data

 3 Suppose that the above histogram and the boxplot in question 2 are plotted for the same dataset. Explain how these graphs complement each other in providing information about any dataset.  
ANS:- data is positive skewed 
       data is not noromal distrubuted   







