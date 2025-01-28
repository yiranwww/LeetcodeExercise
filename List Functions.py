LinkedList() # create a new empty list, no parameter needed, return the new empty list

example_list.is_empoty() # test weather the list is empty. No parameter neeede, return True or False
# or use 
## if list: 
#  This will return True or False

example_list.append(data) # add data at the end of the list

example_list.clear()	Removes ALL the elements from the list
##
fruits = ["apple", "banana", "cherry", "apple"]
fruits.clear()
print(fruits) >> []
##


copy()	Returns a copy of the list

count()	Returns the number of elements with the specified value
##
fruits = ["apple", "banana", "cherry", "apple"]
x = fruits.count("apple")
print(x) >> 2
##

extend()	Add the elements of a list (or any iterable), to the end of the current list

index()	Returns the index of the first element with the specified value
##
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x) >> 2
##

insert()	Adds an element at the specified position

pop()	Removes the element at the specified position

remove()	Removes the first item with the specified value

reverse()	Reverses the order of the list

sort()	Sorts the list. It can only be used in List and will effect the original list
sorted() will not effect the orginal list/array

##
L = [1, 5, 4, 2, 3]

#Print the sorted list
print("Sorted list:")
print(sorted(L))
Sorted list:
[1, 2, 3, 4, 5]
#Print the original list
print("\nOriginal list after sorting:")
print(L)
Original list after sorting:
[1, 5, 4, 2, 3]
##


L = [1, 5, 4, 2, 3]
 
# Sorting the list in-place using sort()
L.sort()
 
# Print the sorted list
print("Sorted list:")
print(L)
Sorted list:
[1, 2, 3, 4, 5]
# Print the original list after sorting
print("\nOriginal list after sorting:")
print(L)
Original list after sorting:
[1, 2, 3, 4, 5]

