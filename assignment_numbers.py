"""
WAP to assign 75 and 3.14 values to the variable and constant.
Check the values and type of those after the assignment.
"""
a=75
PI=3.14
print("a: ",a,", type: ",type(a),",PI: ",PI,",type: ",type(PI))

'''
WAP to define one complex number with lower case 'j' and
another one with the upper case 'J'.
Check the values and type of the variables after the assignment.
'''
x=4+6j
y=6+3J
print("x: ",x,",type: ",type(x),",b: ",y,",type: ",type(y))
'''
WAP to assign 99 digits integer number to a variable.
Check the value, size and type of the variable after the assignment.
'''
import sys
v=123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789
print("v: ",v,",type: ",type(v),",size in bytes: ",sys.getsizeof(v))
