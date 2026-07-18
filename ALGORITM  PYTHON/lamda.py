#A lambda function can take any number of arguments, but can only have one expression.
x = lambda a, b : a * b
print(x(5, 6)) 


# A simple recursive function that counts down from 5:
def countdown(n):
  if n <= 0:
    print("Done!")
  else:
    print(n)
    countdown(n - 1)

countdown(5)