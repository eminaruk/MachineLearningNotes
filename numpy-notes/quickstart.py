import numpy as np

array1 = np.array([1,2,3,4])


zero_array = np.zeros((3,5))
one_array = np.ones((3,7))
empty_array = np.empty((5,7))  #the function empty creates an array whose initial content is random and depends on the state of the memory

ranged_array = np.arange(0,15,3)

### linspace an array 

from numpy import pi
array2 = np.linspace(0, 3, 10)
array3 = np.linspace(0 , 2*pi, 100)
f = np.sin(array3)


### printing arrays

onedimentionArray = np.arange(7) # [0 1 2 3 4 5 6]

twodimentionArray = np.arange(0,42).reshape(7,6)
                                                    # [[ 0  1  2  3  4  5]
                                                    #  [ 6  7  8  9 10 11]
                                                    #  [12 13 14 15 16 17]
                                                    #  [18 19 20 21 22 23]
                                                    #  [24 25 26 27 28 29]
                                                    #  [30 31 32 33 34 35]
                                                    #  [36 37 38 39 40 41]]


threedimentionArray = np.arange(0,24).reshape(2,3,4)

                                                    # [[[ 0  1  2  3]
                                                    #   [ 4  5  6  7]
                                                    #   [ 8  9 10 11]]

                                                    #  [[12 13 14 15]
                                                    #   [16 17 18 19]
                                                    #   [20 21 22 23]]]


#!!! what if array is too big?

bigarray = np.arange(10000) # [   0    1    2 ... 9997 9998 9999]
bigtwodimentionArray = np.arange(10000).reshape(100,100) 
                                                        # [[   0    1    2 ...   97   98   99]
                                                        #  [ 100  101  102 ...  197  198  199]
                                                        #  [ 200  201  202 ...  297  298  299]
                                                        #  ...
                                                        #  [9700 9701 9702 ... 9797 9798 9799]
                                                        #  [9800 9801 9802 ... 9897 9898 9899]
                                                        #  [9900 9901 9902 ... 9997 9998 9999]]

#!!! if I want to show all the array elements of the big array, I can set the array printing settings :


import sys 
np.set_printoptions(threshold=sys.maxsize) # I can't copy here whole these numbers :)

### Basic Operations

array4 = np.array([15,30,45,60])
array5 = np.linspace(0,30,4)


# print(array4 - array5) # [15. 20. 25. 30.]
# print(array4 ** 2) # [ 225  900 2025 3600]
# print(array5 > 10) # [False False  True  True]

### Unlike in many matrix languages, the product operator * operates elementwise in NumPy arrays. 
# The matrix product can be performed using the @ operator (in python >=3.5) or the dot function or method:

A = np.array([[1,2],
              [3,4]])

B = np.array([[5,6],
             [7,8]])

elementwise_object = A * B
# print(elementwise_object)
# print(type(elementwise_object))

# [[ 5 12]
#  [21 32]]
matrix_product = A @ B
#!!! also we can get matrix product with dot function, the answer is the same
matrix_product = np.dot(A, B)

#!!! how to calculate the matrix multiplication:

# # # Matrix A (2x3):

# # # | 1  2  3 |
# # # | 4  5  6 |

# # # Matrix B (3x2):

# # # | 7  8 |
# # # | 9 10 |
# # # | 11 12 |

# # # To multiply A and B, the resulting matrix C will be a 2x2 matrix:

# # # scss

# # # C = A * B

# # # C[0][0] = (1*7) + (2*9) + (3*11) = 7 + 18 + 33 = 58
# # # C[0][1] = (1*8) + (2*10) + (3*12) = 8 + 20 + 36 = 64
# # # C[1][0] = (4*7) + (5*9) + (6*11) = 28 + 45 + 66 = 139
# # # C[1][1] = (4*8) + (5*10) + (6*12) = 32 + 50 + 72 = 154

# # # So, the resulting matrix C is:

# # # | 58  64 |
# # # | 139 154 |

# print(matrix_product)
# [[19 22]
#  [43 50]]


#!!! Some operations, such as += and *=, act in place to modify an existing array rather than create a new one.

rg = np.random.default_rng(1)
sample_array = np.ones((3,7), dtype=int)
sample_array2 = rg.random((3,7))

sample_array *= 3
# print(sample_array) 
# [[3 3 3 3 3 3 3]
#  [3 3 3 3 3 3 3]
#  [3 3 3 3 3 3 3]]






