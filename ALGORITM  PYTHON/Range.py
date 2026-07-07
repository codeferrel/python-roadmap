#The built-in range() function returns an immutable sequence of numbers, commonly used for looping a specific number of times.
#This set of numbers has its own data type called range.

x = range(3, 10, 2)
print(x)

print(list(x))
#Loop
for i in range(10):
  print(i)

#
r = range(0, 10, 2)
print(list(r))
print(6 in r)
print(7 in r)