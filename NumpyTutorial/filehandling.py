# File Handling

# The key function for working with files in Python is the open() function.

# The open() function takes two parameters; filename, and mode.

# There are four different methods (modes) for opening a file:

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists

# # In addition you can specify if the file should be handled as binary or text mode
# # "t" - Text - Default value. Text mode
# # "b" - Binary - Binary mode (e.g. images)
# # Syntax
# # To open a file for reading it is enough to specify the name of the file:

# # Syntax

# # To open a file for reading it is enough to specify the name of the file:
# f = open("demofile.txt")

# # The code above is the same as:
# f = open("demofile.txt", "rt")


# ##############################
# f = open("demofile.txt")
# print(f.read())

# f = open("D:\\myfiles\welcome.txt")
# print(f.read()) 

# # Write to an Existing File
# # To write to an existing file, you must add a parameter to the open() function:
# # "a" - Append - will append to the end of the file
# # "w" - Write - will overwrite any existing content
# with open("demofile.txt", "a") as f:
#   f.write("Now the file has more content!")

# #open and read the file after the appending:
# with open("demofile.txt") as f:
#   print(f.read()) 


#   Open the file "demofile.txt" and overwrite the content:
with open("demofile.txt", "w") as f:
  f.write("Woops! I have deleted the content!")

#open and read the file after the overwriting:
with open("demofile.txt") as f:
  print(f.read()) 





# Delete a File

# To delete a file, you must import the OS module, and run its os.remove() function:
# import os
# os.remove("demofile.txt") 