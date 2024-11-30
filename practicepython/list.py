# This file will help to revise what can be done with with list

List1 = [1, 2, 3, 4, 5]
List2 = [6, 7, 8, 9, 10]
List3 = [11, 12, 13, 14, 15]

#performing basic operation on list
# Append
List1.append(6)

# Insert
List1.insert(1, 0)
# this will insert 0 at index 0 and shift all other elements to right

# Remove
List1.remove(0)
# this will remove first occurance of 0 from the list

# Pop
List1.pop()
# this will remove last element from the list

# Clear
# this will remove all elements from the list
List1.clear()

# Copy
# this will copy all elements from the list
List1.copy()

# Reverse
# this will reverse all elements from the list
List1.reverse()



# Append List2 to List1
List1.extend(List2)
print(List1)


# Append List2 to List1
List1.append(List3)
print(List1)

# indexing

print(List1[0])
print(List2[1])
print(List3[2])

# Slicing
print(List1[0:2])
print(List2[1:3])
print(List3[2:4])

# Length of list
print(len(List1))
print(len(List2))
print(len(List3))

# Looping through list
for i in List1:
    print(i)

# Operation on list
# print(sum(List1))     will raise TypeError: unsupported operand type(s) for +: 'int' and 'list'
print(sum(List2))
print(max(List2))
print(min(List3))
print(List1.count(1))

make_list = list(range(1, 10))  #last number is not included
print(make_list)

# List comprehension
# Syntax: [expression for item in iterable if condition]
# List comprehension is an elegant way to define and create lists based on existing lists.
# List comprehension is generally more compact and faster than normal functions and loops for creating list.
# However, we should avoid writing very long list comprehensions in one line to ensure that code is user-friendly.

# Making list using Lambda function
squared = list(map(lambda x: x**2, range(10)))
print(squared)


# other example
cube = [x**3 for x in range(10)]
print(cube)

# List comprehension with if condition
# Syntax: [expression for item in iterable if condition]
# List comprehension is an elegant way to define and create lists based on existing lists.
even = [x for x in range(10) if x % 2 == 0]
print(even)

# List comprehension with if else condition
# Syntax: [expression for item in iterable if condition else expression]
# List comprehension is an elegant way to define and create lists based on existing lists.


even_odd = ["Even" if i % 2 == 0 else "Odd" for i in range(10)]
print(even_odd)

# Nested List comprehension
# Syntax: [expression for item in iterable if condition]
# List comprehension is an elegant way to define and create lists based on existing lists.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpose = [[row[i] for row in matrix] for i in range(3)]
print(transpose)

# List comprehension with zip
# Syntax: [expression for item in iterable if condition]
# The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpose = [list(row) for row in zip(*matrix)]
print(transpose)

