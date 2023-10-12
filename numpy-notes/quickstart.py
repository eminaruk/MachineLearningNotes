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

d = np.exp((sample_array + sample_array2) * 1j)
# print(d)

# [[-0.93224452-0.3618289j  -0.69031568-0.7235083j  -0.99999671-0.00256696j
#   -0.69162717-0.7222547j  -0.98554434-0.1694177j  -0.96057485-0.27802151j
#   -0.77371634-0.63353218j]
#  [-0.96440656-0.26442387j -0.9179158 -0.39677524j -0.99350522+0.11378656j
#   -0.81854634-0.5744405j  -0.92239875-0.38623898j -0.98235399-0.18703112j
#   -0.79799459-0.60266461j]
#  [-0.98697076-0.16089971j -0.95175063-0.3068725j  -0.99997149+0.00755088j
#   -0.96599801-0.25854949j -0.99808712-0.06182314j -0.9927221 -0.12042768j
#   -0.82035087-0.57186052j]]

a = rg.random((2,3))
# print(a)              # [[0.28040876 0.48519097 0.9807372 ]
                        #  [0.96165719 0.72478994 0.54122686]]

# print(a.sum())  # 3.974010922203668
# print(a.min())  # 0.2804087579860399
# print(a.max())  # 0.9807371998012386

#! Let's make the changes with the axis parameter

the_array_for_this_example = np.arange(15).reshape(5,3)

sum_of_array = the_array_for_this_example.sum() #105
sum_of_each_column = the_array_for_this_example.sum(axis=0)  # [30 35 40]
sum_of_each_row = the_array_for_this_example.sum(axis=1) #[ 3 12 21 30 39]
cumulative_sum_of_each_row = the_array_for_this_example.cumsum(axis=1)  #[[ 0  1  3]
                                                                        #  [ 3  7 12]
                                                                        #  [ 6 13 21]
                                                                        #  [ 9 19 30]

#! numpy also haves and help to us about universal mathematical funcitons. These funcitons called by ufunc (universal functions)
#! you can index, slice and iterate any one-dimentional array like lists

### Using np.fromfunction() method


def array_function(x,y):

    return x**y

array_for_function = np.fromfunction(array_function, (3,7), dtype=int)

# print(array_for_function)

# [[ 1  0  0  0  0  0  0]
#  [ 1  1  1  1  1  1  1]
#  [ 1  2  4  8 16 32 64]]

#! also we can use dots(...) to avoid unecessary symbols

three_dimention_array = np.arange(42).reshape(2,3,7)    # [[[ 0  1  2  3  4  5  6]
                                                        #   [ 7  8  9 10 11 12 13]
                                                        #   [14 15 16 17 18 19 20]]

                                                        #  [[21 22 23 24 25 26 27]
                                                        #   [28 29 30 31 32 33 34]
                                                        #   [35 36 37 38 39 40 41]]]



get_second_values = three_dimention_array[... , 1] #[[ 1  8 15]
                                                   #  [22 29 36]

# if we want to rach each element of the array we can use flat for that 

# an_array = np.arange(120).reshape(2,6,10) # and now, this is a 3D array and we can reach the each element with the flat

# for each_element in an_array.flat:

#     print(each_element)

### Shape manipulation (change the shape of an array)

#! we can change the shape of an array by three easy method:

myarray = np.array([[[ 0,  1,  2,  3],
                    [ 4,  5,  6,  7],
                    [ 8,  9, 10, 11]],

                   [[12, 13, 14, 15],
                    [16, 17, 18, 19],
                    [20, 21, 22, 23]],

                   [[24, 25, 26, 27],
                    [28, 29, 30, 31],
                    [32, 33, 34, 35]]])

flattened_array = myarray.ravel()   # it seperate element by element

# print(flattened_array) #[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
#  24 25 26 27 28 29 30 31 32 33 34 35]

standart_reshaped_array = myarray.reshape(9,2,2)    # [[[ 0  1]
                                                    #   [ 2  3]]

                                                    #  [[ 4  5]
                                                    #   [ 6  7]]

                                                    #  [[ 8  9]
                                                    #   [10 11]]

                                                    #  [[12 13]
                                                    #   [14 15]]

                                                    #  [[16 17]
                                                    #   [18 19]]

                                                    #  [[20 21]
                                                    #   [22 23]]

                                                    #  [[24 25]
                                                    #   [26 27]]

                                                    #  [[28 29]
                                                    #   [30 31]]

                                                    #  [[32 33]
                                                    #   [34 35]]]


transposed_array = myarray.T # you can transpose (the columns become rows, rows become columns) by this method
# print(myarray.shape, transposed_array.shape, sep=" | ") # (3, 3, 4) | (4, 3, 3) # as you can see, the shape is transposed.

# also, we can use the resize() method to change array itself directly 

myarray.resize((9,4))
# print(myarray)    #[[ 0  1  2  3]
                    #  [ 4  5  6  7]
                    #  [ 8  9 10 11]
                    #  [12 13 14 15]
                    #  [16 17 18 19]
                    #  [20 21 22 23]
                    #  [24 25 26 27]
                    #  [28 29 30 31]
                    #  [32 33 34 35]]

# you can get dimention calculated exist first dimention, you can use -1 to refer the other dimentions:

reshaped_array = myarray.reshape(3, -1) # so, I just want to 3 row and I don't care other dimentions. The algorithm
# will calculate the other dimention for you

# print(reshaped_array.shape) # (3, 12) # as you can seee three tiems twelve qual to total element number :)


### Stacking togother the different arrays 

a = np.floor(20 * rg.random((2,2)))
b = np.floor(20 * rg.random((2,2)))

stacked_a_b_vertical = np.vstack((a,b))
stacked_a_b_horizontal = np.hstack((a,b))

# print(stacked_a_b_vertical)
 
            #  [[ 5.  3. 19.]
            #  [10.  2. 12.]
            #  [15. 12. 18.]
            #  [ 0. 10.  9.]
            #  [ 1. 12. 17.]
            #  [11.  5. 16.]]
# print(stacked_a_b_horizontal)

            # [[ 5.  3. 19.  0. 10.  9.]
            #  [10.  2. 12.  1. 12. 17.]
            #  [15. 12. 18. 11.  5. 16.]]


from numpy import newaxis

columns_stack = np.column_stack((a,b))
# print(columns_stack)

            # [[ 5.  3. 19.  0. 10.  9.]
            #  [10.  2. 12.  1. 12. 17.]
            #  [15. 12. 18. 11.  5. 16.]]

a = np.array([4., 2.])
b = np.array([3., 8.])

h_stacked_array = np.hstack((a,b))
# print(h_stacked_array)
# [4. 2. 3. 8.]

a_Like_2dimention = a[:, newaxis] # this code provides to view a as a 2D array 

# print(a_Like_2dimention)  
            # [[4.]
            #  [2.]]

# let's stack their 2d views horizontally but

b_Like_2dimention = b[:, newaxis]

h_stacked_array = np.hstack((a_Like_2dimention, b_Like_2dimention))
column_stacked_array = np.column_stack((a, b))
# print(h_stacked_array)
# print(column_stacked_array)

            # [[4. 3.]
            #  [2. 8.]]
            # [[4. 3.]
            #  [2. 8.]]  #! as you can see, the result is the same with the column stack :)


### splitting one array into the several smaller ones 

sample_array_for_splitting = np.floor(10 * rg.random((2,12)))  
# print(sample_array_for_splitting)
            # [[9. 0. 5. 4. 0. 6. 8. 5. 2. 8. 5. 5.]
            #  [7. 1. 8. 6. 7. 1. 8. 1. 0. 8. 8. 8.]]

split_into_the_3pcs = np.hsplit(sample_array_for_splitting, 3)
# print(split_into_the_3pcs)

            # [array([[9., 0., 5., 4.],
            #        [7., 1., 8., 6.]]), array([[0., 6., 8., 5.],
            #        [7., 1., 8., 1.]]), array([[2., 8., 5., 5.],
            #        [0., 8., 8., 8.]])]

split_after_columns = np.hsplit(sample_array_for_splitting, (4,5))
# print(split_after_columns)

            # [array([[9., 0., 5., 4.],
            #        [7., 1., 8., 6.]]), array([[0.],
            #        [7.]]), array([[6., 8., 5., 2., 8., 5., 5.],
            #        [1., 8., 1., 0., 8., 8., 8.]])]


### copies and views

#! the function calls make no copy:

def f(x):

    print(id(x))


# print(id(a))
# f(a)

            # 2885855918384
            # 2885855918384  # as you can see, when we call the function, the function doesn't create a new copy for argument

a = np.floor(10 * rg.random((3,4)))
s = a[:, 1:3]
s[:] = 10  ## this is not a copy, is a view. Hence, it owns the data and when you make a change on it, you make the change on the s also

# print(a)
# print(s)

            # [[ 4. 10. 10.  6.]
            #  [ 7. 10. 10.  2.]
            #  [ 6. 10. 10.  1.]]
            # 10


## deep copy

a = np.arange(int(1e8))

# the expression 1e8 represents a mathematical notation for a number, which is equal to 10,000,000. 
# It's using scientific notation, where 1e8 means "1 times 10 to the power of 8," and 10 to the power of 8 is 100,000,000.

b = a[:100].copy() # we don't need to copy whole the large array, we just take wha we need from the large array.
del a


### advanced indexing

a = np.arange(12)**2 
j = np.array([2,5,4,7,9])

# print(a[j])  # [ 4 25 16 49 81] #! the each element corresponds the one index of a

a = np.arange(12).reshape(3,4)
i = np.array([[1,2],
              [0,1]])

j = np.array([[0,3],
              [0,3]])

# print(a)

            # [[ 0  1  2  3]
            #  [ 4  5  6  7]
            #  [ 8  9 10 11]]
# print(a[i,j])

            # [[ 4 11]
            #  [ 0  7]]


### indexing with boolen arrays

# a quick example

a = np.arange(15).reshape(3,5)
b = a > 7
# print(a[b]) # [ 8  9 10 11 12 13 14]

#! and also we can modify the items like that:
a[b] = 0
# print(a)


        # # [[0 1 2 3 4]
        # #  [5 6 7 0 0]
        # #  [0 0 0 0 0]]

