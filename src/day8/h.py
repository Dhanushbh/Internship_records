import numpy as np
arr=np.arange(12)

reshaped=arr.reshape(3,4)
print(reshaped)
a=np.array([[1,2]])
b=np.array([[3,4]])
vstacked=np.vstack((a,b))
print(vstacked)
####hstack##
hstacked=np.hstack((a,b))
print(hstacked)

####
data=np.array([[10,20,30],[40,50,60]])
print(np.mean(data))
print(np.mean(data,axis=0))
print(np.mean(data,axis=1))

#######matrix###
arr=np.linspace(0,3)
print(arr)
#####random####3
arr=np.random.randn(2,2)
print(arr)


