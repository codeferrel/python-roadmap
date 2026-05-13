name = "Noe"
age = 21
height = 1.65
is_student = True
print(name, age, height, is_student)

fruits = ["apple", "mango", "grape"]

print(fruits[0])  
print(fruits[1])  
print(fruits[2])  

number = 80
number1 = 100
number2 = 600
number3 = 78
number4 = 88

result1 = number + number1
result2 = number1 * number2
result3 = number ** 2
result4 = number2 // 10
result5 = number2 % number

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)

# Loop with range
for i in range(10):
    print("Hello Python")

# Fixed the input variable usage
nama = input("Enter your name here: ")
print("Hello", nama, "Welcome") 

x = 24
y = 20
my_list = [10, 20, 30, 40, 50] # Removed the dot in 10.20 for clarity

# Fix: Python relies strictly on indentation
if x not in my_list:
    print("x is not present in given list")
else:
    print("x is present in given list")

if y in my_list:
    print("y is present in given list")
else:
    print("y is not present in given list")

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

score = 75

# Fix: Removed the double commas and fixed indentation
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")


    # Python example for while loop
count = 0
while (count < 3):
    count = count + 1
    print("Hello Geek")