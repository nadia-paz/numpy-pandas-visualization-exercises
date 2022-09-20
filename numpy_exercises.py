import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

#1 How many negative numbers are there?
negative_numbers = a[a < 0]
print(negative_numbers) # [-2 -1 -6 -7]
negative_numbers.size # 4

#2 How many positive numbers are there?
positive_numbers = a[a > 0]
positive_numbers.size #5

#3 How many even positive numbers are there?
positive_even_numbers = positive_numbers[positive_numbers % 2 == 0]
positive_even_numbers.size #3

# using the original array a

positive_even_numbers = (a[a % 2 == 0])[(a[a % 2 == 0]) > 0]
print(positive_even_numbers)
# array([ 4, 10, 12])
#[(a[a % 2 == 0]) > 0] #returns array of true and false

#4 If you were to add 3 to each data point, how many positive numbers would there be?
plus_3_positive = (a + 3)[a > 0]
plus_3_positive.size #5

#5 If you squared each number, what would the new mean and standard deviation be?
squared_array = a ** 2
squared_mean = np.mean(squared_array)
squared_std = np.std(squared_array)
print(f'Mean is {squared_mean}, STD is {round(squared_std, 2)}')
# Mean is 74.0, STD is 144.02

#6 A common statistical operation on a dataset is centering. 
# This means to adjust the data such that the mean of the data is 0. 
# This is done by subtracting the mean from each data point. Center the data set.
centered_array = a - int(np.mean(a))
np.mean(centered_array)

#7 Calculate the z-score for each data point.
zscores = (a - int(np.mean(a))) / np.std(a)
zscores = np.array([round(z, 2) for z in zscores])
zscores

"""
Copy the set up and exercise directions from More Numpy Practice 
into your numpy_exercises.py and add your solutions."""

# Life w/o numpy to life with numpy

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_a = sum(a)
print(sum_of_a) #55
sum_of_a = np.array(a).sum()
print(sum_of_a)

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a = min(a)
print(min_of_a) #1
min_of_a = np.array(a).min()
print(min_of_a)

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = max(a)
print(max_of_a) #10
#with numpy
max_of_a = np.array(a).max()
print(max_of_a)

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a = sum(a) / len(a)
#or
mean_of_a = np.mean(a)
mean_of_a

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
product_of_a = np.prod(a)
product_of_a #3628800

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
squares_of_a = [n ** 2 for n in a]
print(squares_of_a)
#or
squares_of_a = np.array(a) ** 2
print(squares_of_a)

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
odds_in_a = [n for n in a if n % 2 == 1]
print(odds_in_a)
# or with numpy
odds_in_a = np.array(a)[np.array(a) % 2 == 1]
print(odds_in_a)

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
evens_in_a = [n for n in a if n % 2 == 0]
print(evens_in_a)
#or with numpy
evens_in_a = np.array(a)[np.array(a) % 2 == 0]
print(evens_in_a)

## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]
#transform b as a numpy array
b_arr = np.array(b)
print(b_arr)

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)

sum_of_b = b_arr.sum()
print(sum_of_b) #33

# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  

min_of_b = b_arr.min()
print(min_of_b) #3

# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])

max_of_b = b_arr.max()
print(max_of_b) #8

# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))
mean_of_b = b_arr.mean()
print(mean_of_b)

# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number

prod_of_b = np.prod(b_arr)
print(prod_of_b)

# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)

squares_of_b = b_arr ** 2
print(squares_of_b)


# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)

odds_in_b = b_arr.flatten()[b_arr.flatten() % 2 == 1]
#or
b_arr_list = b_arr.flatten()
odds_in_b = b_arr_list[b_arr_list % 2 != 0]

print(odds_in_b)

# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)

# Exercise 9 - print out the shape of the array b.
evens_in_b = b_arr_list[b_arr_list % 2 == 0] #b_arr_list from the previous exercise
print(evens_in_b)

# Exercise 10 - transpose the array b.
b_transposed = b_arr.transpose((1, 0))
print(b_transposed)
"""
[[3 6]
 [4 7]
 [5 8]]
"""
# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
b_arr_list = b_arr.reshape(1, 6)
print(b_arr_list)

# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
arr_vertical = b_arr.reshape(6, 1)
print(arr_vertical)
"""
[[3]
 [4]
 [5]
 [6]
 [7]
 [8]]
"""

## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.
min_of_c = c.min()
max_of_c = c.max()
prod_of_c = c.prod()
print(f'Min is {min_of_c}, \nMax is {max_of_c}, \nProduct is {prod_of_c}')
'''
Min is 1, 
Max is 9, 
Product is 362880
'''

# Exercise 2 - Determine the standard deviation of c.
std_of_c = c.std() #2.581988897471611

# Exercise 3 - Determine the variance of c.
var_of_c = c.var() # ~6.67

# Exercise 4 - Print out the shape of the array c
print(c.shape) #(3, 3)

# Exercise 5 - Transpose c and print out transposed result.
print(c.transpose())
'''
[[1 4 7]
 [2 5 8]
 [3 6 9]]
'''

# Exercise 6 - Get the dot product of the array c with c. 
dot_prod = np.dot(c, c)
print(dot_prod)
'''
[[ 30  36  42]
 [ 66  81  96]
 [102 126 150]]
'''

# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. 
# Answer should be 261
sum_with_transpose = (c * c.transpose()).sum()

# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.
prod_with_transpose = (c * c.transpose()).prod()

## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

# Exercise 1 - Find the sine of all the numbers in d

# Exercise 2 - Find the cosine of all the numbers in d

# Exercise 3 - Find the tangent of all the numbers in d

# Exercise 4 - Find all the negative numbers in d

# Exercise 5 - Find all the positive numbers in d

# Exercise 6 - Return an array of only the unique numbers in d.

# Exercise 7 - Determine how many unique numbers there are in d.

# Exercise 8 - Print out the shape of d.

# Exercise 9 - Transpose and then print out the shape of d.

# Exercise 10 - Reshape d into an array of 9 x 2
