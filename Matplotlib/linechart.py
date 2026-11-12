# 1. Line Chart
# Line chart is one of the basic plots and can be created using plot() function. It is used to represent a relationship between two data X and Y on a different axis.
# Example: This code plots a simple line chart with labeled axes and a title using Matplotlib.
# import matplotlib.pyplot as plt

# x = [10, 20, 30, 40]
# y = [20, 25, 35, 55]

# plt.plot(x, y)
# plt.title("Line Chart")
# plt.ylabel('Y-Axis')
# plt.xlabel('X-Axis')
# plt.show()


# Pie chart is a circular chart used to show data as proportions or percentages. It is created using the pie(), where each slice (wedge) represents a part of the whole.
import matplotlib.pyplot as plt

cars = ['AUDI', 'BMW', 'FORD','TESLA', 'JAGUAR',]
data = [23, 10, 35, 15, 12]

plt.pie(data, labels=cars, autopct='%1.1f%%')
plt.title(" Pie Chart")
plt.show()