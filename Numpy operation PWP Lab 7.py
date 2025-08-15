#type 1
import numpy as np
array1 = np.arange(2, 11).reshape(3, 3)
print("3x3 Matrix ranging from 2 to 10:\n", array1)

#type 2
import numpy as np
array2 = np.array([[2, 3, 4],[5, 6, 7],[8, 9, 10]])
print(array2)


array2 = np.array([1, 2, 3, 4, 5])
array3 = array2[::-1]
print("Reversed array:", array3)


array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([4, 5, 6, 7, 8])
array3 = np.intersect1d(array1, array2)
print("Common values:", array3)


array4 = np.array([1, 2, 3])
arr4 = np.repeat(array4, 3)
print("Repeated array:", arr4)


A = np.array([[[1, 2],[3,4]],[[5, 6],[7, 8]]])
print("Memory size of array (in bytes):", A.nbytes)
print("size of the array: ",A.size)


zeros = np.zeros((2, 3))
ones = np.ones((2, 3))
print("Array of zeros:\n", zeros)
print("Array of ones:\n", ones)


B = np.array([10, 20, 30, 40, 50])
C = B[3]
print("4th element in B is:", C)

