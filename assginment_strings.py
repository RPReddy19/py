"""
Write a Program to retrieve character 'X' using positive indexing
from "Semantic segmentation of Lung Cancer from Chest X-Ray" string
"""
a="Semantic segmentation of Lung Cancer from Chest X-Ray"
print(a[len(a)-5])
'''
Write a Program to retrieve the 'L' character from "I have to Love Python Programming" string
using negative/reverse indexing
'''
b="I have to Love Python Programming"
print(b[-23])
'''
Can prove that python string is immutable with the program
'''
name="Vishnuteja"
print("name: ",name)
#now i am trying to modifing the staring char in name string
name[0]="v"
print("name: ",name)
#in line number 19 we getting Error: TypeError: 'str' object does not support item assignment..
#python interpreter will not allows item assignment to exicting string.
