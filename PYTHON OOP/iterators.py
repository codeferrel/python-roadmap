# An iterator in Python is an object used to traverse through all the elements of a collection (like lists, tuples or dictionaries) one element at a time. It follows the iterator protocol, which involves two key methods:
#     __iter__(): Returns the iterator object itself.
#     __next__(): Returns the next value from the sequence. Raises StopIteration when the sequence ends.

s="NOEL"
it=iter(s)

print(next(it))
print(next(it))
print(next(it))
print(next(it))