### for diagonal elements:

import numpy as np
from io import StringIO

diagonal_array = np.diag([3,5,7])
# print(diagonal_array)
#also we can start the diagonal numbers from any index of first row
diagonal_array2 = np.diag([3,5,7], 1)
# print(diagonal_array2)

# let's make an array and after that convert it to the diag

basic_array = np.array([[1,2],
                        [3,4]])

diagnoal_basic_array = np.diag(basic_array)
# print(diagnoal_basic_array)

### loading array from a file

loaded_array = np.loadtxt("simple_array.csv", delimiter=",", skiprows=1)
# print(loaded_array)

### I/O with numpy

data = u"1,2,3\n4,5,6"
array_from_data = np.genfromtxt(StringIO(data), delimiter=",")
# print(array_from_data)

# we can make all the lines column same like that:

data = u"  1  2  3\n  4  5 67\n890123  4"
array_from_data = np.genfromtxt(StringIO(data), delimiter=3)
# print(array_from_data)

data = u"123456789\n   4  7 9\n   4567 9"
array_from_data = np.genfromtxt(StringIO(data), delimiter=(4,3,2))
# print(array_from_data)

### using the autostrip

data = u"1, abc , 2\n 3, xxx, 4"

array_from_data = np.genfromtxt(StringIO(data), delimiter="," , dtype=("|U5"))
# print(array_from_data)  ## this is without the autostrip

array_from_data = np.genfromtxt(StringIO(data), delimiter=",", autostrip=True, dtype="|U5")
# print(array_from_data) ## as you can see, the whitespaces are not there anymore :)

### how can we ignore the comments:

data = u"""#

# Skip me !

# Skip me too !

1, 2

3, 4

5, 6 #This is the third line of the data

7, 8

# And here comes the last line

9, 0

"""

array_from_data = np.genfromtxt(StringIO(data), delimiter=",", comments="#")  ## I define the comment symbol and it automatically ignores the comments
# print(array_from_data)  # there we go :)


### skipheader and skipfooter

data = u"\n".join(str(x) for x in range(15))

array_from_data = np.genfromtxt(StringIO(data), delimiter=",", 
                                skip_header= 5,  # the header starts from beginnning of the array
                                skip_footer= 3)  # the footer start from end of the array

# print(array_from_data)   

### selecting the specific columns in the array

data = u"1,2,3\n4,5,6"

array_from_data = np.genfromtxt(StringIO(data), delimiter=",", usecols=(1,2)) # in here, i wanted to second and third columns in the array

# print(array_from_data)
#! also, if the columns have names, we can select them by their names:

array_from_data = np.genfromtxt(StringIO(data), delimiter=",", 
                                names="first_column, second_column, third_column"
                                , usecols=("first_column", "second_column"))

# print(array_from_data)


#! NOTE: the dtype:floar is the default data type in the genfromtext()

array_from_data = np.genfromtxt(StringIO(data), delimiter=",", dtype=[(_, np.int64) for _ in("abc")])

# print(array_from_data.dtype)

# and also we can do it with that:

array_from_data = np.genfromtxt(StringIO(data), delimiter=",", names="A,B,C")
# print(array_from_data.dtype)

#! well, i will make it more complicated. Let's imagine that you use the skipheaders command but also you have the
# columns name in the first lines. How can we say the program that ignore the headers without touching to the names:

data = StringIO("So it goes\n#a b c\n1 2 3\n 4 5 6")

array_from_data = np.genfromtxt(data, skip_header=1, names=True)
# print(array_from_data)


### the defaultfmt argument

data = u"1,2,3\n4,5,6"

array_from_data = np.genfromtxt(StringIO(data), delimiter=",",  dtype=(float, int,int), names="a") ## i left the number of names missing

# print(array_from_data.dtype) # it automatically fill the names with f0, f1, f2...... fn

array_from_data = np.genfromtxt(StringIO(data), delimiter=",", dtype= (int, int, float), defaultfmt='var_%02i')  # 02i represents the maximum 2 digits
# print(array_from_data.dtype)  # it completes the names with like var_00, var_01 and so on.


### validating the names

delete_chars = ","
array_from_data = np.genfromtxt(StringIO(data), delimiter=",", dtype=None, deletechars=delete_chars, names=True)
# print(array_from_data.dtype)

## using exclude list

data = u"name age return salary\nAlice 28 0.05 50000\nBob 35 0.06 60000\nCharlie 30 0.04 55000"
exclude_list = ["return"]
array_from_data = np.genfromtxt(StringIO(data), delimiter= " ", dtype=None, names= True, excludelist=exclude_list, encoding="utf-8")
# print(array_from_data.dtype) # it makes the return expression unique by changing its name as return_


## using case sensitive 

data = u"Name Age Salary\nAlice 28 50000\nBob 35 60000"
case_sensitive = "upper" # it makes all the headers uppercase

array_from_data = np.genfromtxt(StringIO(data), delimiter=(" "), dtype=None, names=True, encoding="utf-8", case_sensitive=case_sensitive)

# print(array_from_data.dtype)


### converters argument
data = u"1, 2.3%, 45.\n6, 78.9%, 0"
convertfunc = lambda x: float(x.strip(b"%"))/100 # i want to convert the strings in the data to float

array_from_data = np.genfromtxt(StringIO(data), names="e,l,f", delimiter=",", converters={1 : convertfunc})  ## it converts
## also  i can use the name of "l" instead of index of it(1)

# print(array_from_data)
# print(array_from_data.dtype)


## fill the whitespaces

data = u"1, , 3\n 4, 5, 6"
convert = lambda x: float(x.strip() or -999)  #! it fills the missing values with -999

array_from_data = np.genfromtxt(StringIO(data), names="e,l,f", converters={1: convert}, delimiter=",")  ## we are done :)
# print(array_from_data)
# print(array_from_data.dtype)

#! In the following example, we suppose that the missing values are flagged with "N/A" in the first column and 
# by "???" in the third column. We wish to transform these missing values to 0 if they occur in the 
# first and second column, and to -999 if they occur in the last column:

data = u"N/A, 2, 3\n4, ,???"
kwargs = {
    "names" : "e,l,f",
    "delimiter" : ",",
    "dtype" :int, 
    "missing_values" : {0:"N/A", "l": " ",2: "???"},
    "filling_values" : {0: 0, "l": 0, 2: -999}

}

array_from_data = np.genfromtxt(StringIO(data), **kwargs, usemask=False)

# print(array_from_data)  # [(0, 2,    3) (4, 0, -999)] 
                        # here we go :)




### overflow errors

#! sometimes, numpy function can't detect the correct number:

number1 = np.power(100,8, dtype=np.int64)
number2 = np.power(100,8, dtype=np.int32)

# print(number1)  ## 10000000000000000 #! this is the true result in this section
# print(number2)  ## 1874919424  #! even the result is the same, int32 dtype is not enough to store this large number

### in case, we can learn minumun and maximum values of a data type in the numpy 

def give_the_number_info(dtype):

    return np.iinfo(dtype)

# print(give_the_number_info(int))

# print(np.finfo(np.longdouble))

### broadcasting

#! sometimes, operations in the two or more differetn numpy object, numpy automatically expand the smaller one to match with the bigger object.

simple_array = np.array([1,2,4])
any_number = 3

operation_result = simple_array * any_number
# print(operation_result)  # the numpy completed the smaller dimention to the biggest dimention 

#! also, we can make possible that broadcast two differen 1-d arrays 
 
one_dimention_array = np.array([1,2,3,4])
one_dimention_array2 = np.array([1,2,3])

# first_braoadcasting = one_dimention_array + one_dimention_array2
# print(first_braoadcasting) # here you are, you got an error :)
# if we want to broadcast two of array succesfully, we have to convert first arrays columns to rows by using newaxis

new_one_dimention_array = one_dimention_array[:, np.newaxis]

second_broadcsting = new_one_dimention_array + one_dimention_array2
# print(second_broadcsting)

### vector quantization example
#! we will find the closest observation to codes in this example

# Create an observation (the athlete to be classified)
observation = np.array([111.0, 188.0])

# Create an array of known codes (athlete classes)
codes = np.array([[102.0, 203.0],
                 [132.0, 193.0],
                 [45.0, 155.0],
                 [57.0, 173.0]])

diff = codes - observation #! in here, the broadcsting is running
# print(dif) # we got the differences between observation and code 

# and we will calculate the euklidean distance with the formula
# print(diff)
dist = np.sqrt(np.sum(diff ** 2, axis=1))
# print(dist)
# print(np.sqrt(np.sum(diff[0] ** 2)))
# print(dist)

best_match = dist[np.argmin(dist)]# we get the shortest or nearsest distances index between obsevation and codes and it is the best match

# print(best_match)


### some tips about copies and views

x = np.array([1,2,3,4,5,6,7,8,9])
y = x[0:5]  ## this is view becasue:

x[0:3] = [10,11,12]
# print(y)  #[10 11 12  4  5]  # as you can see, the y is the view of the x

#! but, there is differencee between basic indexing and advanced indexing:

x = np.arange(15).reshape(5,3)

y = x[[2,3]]
is_y_view = y.base
# print(is_y_view)  ## None #! as you can see the result, y is an copy of the x


### Structured arrays

## structured datatypes 

#! there area several ways to define structured datatypes but i chooes the dictionary method
#! because the dictionary method the simpliest and organized way to do that for me 

dtype = np.dtype({

    "names" : ["column1", "column2"],
    "formats" : ["f4", "i4"]

})  # dictionary method requires two options: names and formats 

#! if you wanti you can specify the offset that is optional

dtype = np.dtype({

    "names" : ["column1", "column2"],
    "formats" : ["f4", "i4"],
    "offsets" : [4,8] # that means the first columns start from the 4th byte and second one starts from 8th byte
})

#! and you can specify the total byte size also

dtype = np.dtype({

    "names" : ["column1", "column2"],
    "formats" : ["f4", "i4"],
    "offsets" : [4,8], # that means the first columns start from the 4th byte and second one starts from 8th byte
    "itemsize" : 16
})

#! for me, the shortest way to describe all these section is:

dtype = np.dtype({'column1': ('f4', 4), 'columns': ('i4', 8)})


## manipulating and alignment of the structured data types 

def print_offsets(d):
    print("offsets:", [d.fields[name][1] for name in d.names])
    print("itemsize:", d.itemsize)

# print_offsets(np.dtype('u1, u1, i4, u1, i8, u2')) # offsets: [0, 1, 2, 6, 7, 15]
                                                  # itemsize: 17
                                                  # each elements offset starts from the end of previous element

                                
# print_offsets(np.dtype('u1, u1, i4, u1, i8, u2', align=True))   #offsets: [0, 1, 4, 8, 16, 24]
                                                                # itemsize: 32
                                                                # each elements offset start from a new byte


np.dtype({'name': ('i4', 0, 'my title')})  ## you can also define a file title addiditonally with this code



### also we can create a dtype which is based on another dtype

example_dtype = np.dtype([("number", "float64"), ("name", "U4")])
array = np.array([(1.5, "emin"), (3.4 ,"elif")], dtype=example_dtype)

field_descriptions = example_dtype.descr
field_descriptions.append(("ages", "int32"))

new_dtype = np.dtype(field_descriptions)
new_array = np.array([(1.2, "emin",19), (4.2, "elif", 19)], dtype=new_dtype)

# print(new_array)


### record arrays

recordarr = np.rec.array([(3,7.5, "hello"), (5, 6.5, "hi!")], dtype= [("first", "i4"), ("second", "f4"), ("third", "S10")])
# print(recordarr)

#! also, you can access the any of field without define a string name:
# print(recordarr.first) 

#! when you try to the same thing on the normal array:
normal_array = np.array([(3,7.5, "hello"), (5, 6.5, "hi!")], dtype= [("first", "i4"), ("second", "f4"), ("third", "S10")])

# print(normal_array.first)  #! that gives you an error!ß

### helper functions to the recarray

## append a new feld:

from numpy.lib.recfunctions import append_fields

normal_array = append_fields(normal_array, "new_field", ("ibrahim","eyup"), dtypes="S12")

# print(normal_array)

## applying along fields

from numpy.lib import recfunctions as rfn 

an_array = np.array([(1,2,3),(4,5,6),(7,8,9)], dtype=[("first_column", "i4"),("second_column", "f4"),("third_column", "i4")])

any_process_i_run = rfn.apply_along_fields(np.mean, an_array[["first_column"]])
# print(any_process_i_run)


## assingning two structured arrays by the name

array1 = np.array([(1,2.,"emin"),(3,5.,"elif")], dtype=[("name1", "i4"), ("name2", "f4"), ("name3", "U10")])

array2 = np.array([(5,6.,"ibrahim"), (3,7., "eyup")], dtype=[("name1", "i4"), ("name2", "f4"), ("name3", "U10")])

rfn.assign_fields_by_name(array2, array1)
# print(array2)


## dropping fields from the array

any_array_for_this_example = np.array([(1, (2, 4.5)), (3, (4, 5.6))], dtype=[("first_column", np.int64),("second_column", [("second_column_container_a", np.double), ("second_column_container_b", np.int64)])])

result_array = rfn.drop_fields(any_array_for_this_example, "first_column")
# print(result_array)

## find the dublicates in the structured arrays 

dtype = [("a", int)]

a = np.ma.array([1,1,7,8,45,4,32,0,0,6,5,2,1], mask = [0,0,0,1,1,1,1,0,1,1,0,1,0]).view(dtype)   #! np.ma is for creating masked arrays


result_of_duplicates = rfn.find_duplicates(a, ignoremask=True)

# print(result_of_duplicates)

#! a short description of a masked array:

# Create a NumPy array with some missing or invalid values
data = np.array([1, 2, -999, 4, 5, -999, 7])

# Create a mask array to specify which elements are invalid
mask = (data == -999)

# Create a masked array by combining data and mask
masked_data = np.ma.array(data, mask=mask)

# Perform operations on the masked array
# For example, calculate the mean without considering the masked elements
mean = np.ma.mean(masked_data)

# Print the masked array and the calculated mean
            # print("Original Data:", data)
            # print("Masked Array:", masked_data)
            # print("Mean (excluding masked values):", mean)


### flatten a structured array 

ndtype = np.dtype([('a', '<i4'), ('b', [('ba', '<f8'), ('bb', '<i4')])])
flatten_description = rfn.flatten_descr(ndtype)

# print(flatten_description)  #! (('a', dtype('int32')), ('ba', dtype('float64')), ('bb', dtype('int32')))


### getting fields and their parents as a dictionary

ndtype =  np.dtype([('A', int),

                    ('B', [('BA', int),

                           ('BB', [('BBA', int), ('BBB', int)])])])

# print(rfn.get_fieldstructure(ndtype))

### getting the name flat

adtype = ndtype

# print(rfn.get_names_flat(adtype))   # ('A', 'B', 'BA', 'BB', 'BBA', 'BBB')  #! it returns a tuple


### join two structured arrays by specific keys

r1 = np.array([(1, "Alice"), (2, "Bob"), (3, "Charlie")], dtype=[('id', int), ('name', 'U10')])
r2 = np.array([(2, 25), (3, 30), (4, 35)], dtype=[('id', int), ('age', int)])

joined_array = rfn.join_by(key="id", r1= r1, r2=r2)  #! it joined them where id numbers are matched
# print(joined_array)

arr1 = np.array([1,2,3])
arr2 = np.array([10.0,20.0,30.0])

merged_array = rfn.merge_arrays((arr1, arr2))
# print(merged_array)


arr1 = np.array([("hello", 1), ("hallo", 2)], dtype=[("the_message", "U10"), ("id", "i4")])
arr2 = np.array([("thanks", 2), ("danke shon", 3)], dtype=[("the_message", "U15"), ("id", "i4")])

merged_array = rfn.merge_arrays((arr1, arr2))
# print(merged_array)
# print(merged_array.dtype)


### add a new fields in an existing array

arr1 = np.array([("hello", 1), ("hallo", 2)], dtype=[("the_message", "U10"), ("id", "i4")])

appended_array = rfn.rec_append_fields(arr1, names = "sender", data = ["english person", "german person"], dtypes= ("U15"))

# print(appended_array.dtype)


### dropping the names 

#! we will use the arr1 in this example

the_arr1_without_message = rfn.rec_drop_fields(arr1, "the_message")
# print(the_arr1_without_message)


### fill an output array according to an input array

input_arr = np.array([(1,10),(2,20)], dtype=[("a",np.int64), ("10_times_a", np.float64)])
output_arr = np.ones(3, dtype=input_arr.dtype)


result_arr = rfn.recursive_fill_fields(input_arr, output_arr)  #! the output arrays size must be at least size of input array
# print(result_arr)



### rename the fields: :)

any_array_in_this_example = np.array([(1,2,3.4), (3,4,23)], dtype=[("a", np.int64), ("b", np.float64), ("c", np.double)])

field_name_changed_array = rfn.rename_fields(any_array_in_this_example, {"a" : "first_column"})

# print(field_name_changed_array.dtype)  # [('first_column', '<i8'), ('b', '<f8'), ('c', '<f8')]



### repacking (reorganizing) the fields

dt = np.dtype("u1,<i4,<i8", align=True)


def print_offsets(d):

    print("Offsets:", [d.fields[name][1] for name in d.names])
    print("Itemsize:", d.itemsize)


# print_offsets(dt)  

            # Offsets: [0, 12, 16]
            # Itemsize: 24

repacked_item = rfn.repack_fields(dt)
# print_offsets(repacked_item)

            # Offsets: [0, 12, 16]
            # Itemsize: 24





