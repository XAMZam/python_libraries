#import numpy as np
#Creating an array using np.array() method
#arr = np.array([10,20,30,40,50])
#printing
#print(arr)

#more than one dimensons
#import numpy as np
#a = np.array([[1,2],[3,4],[5,6],[7,8],[9,10]])
#print(a)

#minimum dimensions
#import numpy as np
#a = np.array([1,2,3,4,5], ndmin = 0)
#print(a)

#dtype parameter
#import numpy as np
#a = np.array([1,2,3],dtype = int)
#print(a)

#import numpy as np
#a= np.arange(0,60,5)
#a = a.reshape(3,4)
#print('Original array is:')
#print(a)
#print('\n')
#print('Modifies array is:')
#for x in np.nditer(a):
 #   print(x)

import numpy as np
a= np.arange(0,60,5)
a = a.reshape(3,4)
print('Original array is:')
print(a)
print('\n')
print('Transponse of the original array is:')
b= a.T
print(b)
print('\n')
print('Modefies array is:')
for x in np.nditer(b):
    print(x)