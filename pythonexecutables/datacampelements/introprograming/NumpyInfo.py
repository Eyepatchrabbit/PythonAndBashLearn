# importing an element to use
import numpy as np

# arrays =>no calculations on lists ->inefficient
regArray = [1, 2, 3]

print("regArray*3 gives: ", regArray * 3)

# a numpy array
# can do calculations on all elements on tbe array
# can only contain one type of variables
nparray = np.array([1, 2, 3])

print("nparray*3 gives:", nparray * 3)

# can make n-dimentional arrays!!


# some handy elements:
print("\nmean & median:")

x = [1, 4, 8, 10, 12]

print("array: ", x)
print("np.mean(x)", np.mean(x))
print("np.median(x)", np.median(x))
print(np.std(x))

# you can stack arrays together
print("\ncolumn_stack")
y = [10, 9, 8, 6, 5]
fuse = np.column_stack((x, y))
print(fuse)
print("\ncorrcoef")
print(np.corrcoef(x, y))

# selective filtering data
print("\nselective filtering data")

np_positions = np.array(['GK', 'M', 'A', 'D'])
np_heights = np.array([191, 184, 185, 180])

print("GK: ", np_heights[np_positions == 'GK'])
