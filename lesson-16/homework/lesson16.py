#1
import numpy as np
orglist=[12.23, 13.32, 100, 36.32]
arr=np.array(orglist)
print(arr)
#2
ls=np.arange(2,11).reshape(3,3)
print(ls)
#3
ls=np.zeros(10)
ls[6]=11
print("Update sixth value to 11", ls)
#4
ls=np.arange(12,38)
print(ls)
#5
arr=np.array([1,2,3,4])
floatarr=arr.astype(float)
print(floatarr)
#6
centigrade=np.array([0, 12, 45.21, 34, 99.91, 0.])

#7
centigrade = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0.])
fahrenheit = centigrade * 9/5 + 32
print("Values in Centigrade degrees:", centigrade)
print("Values in Fahrenheit degrees:", fahrenheit)
#8
orgarr=[10,20,30]
appendvalues=[40,50,60,70,80,90]
arr=np.append(orgarr,appendvalues)
print("After append values to the end of the array:", arr)
#9
randomarr=np.random.rand(10,10)
minvalue=np.min(randomarr)
maxvalue=np.max(randomarr)
print("random 10x10 array:\n", randomarr)
print("\nMinimum value:", minvalue)
print("\nMaximum value:", maxvalue)
#10
arr=np.random.rand(3,3,3)
print(arr)
