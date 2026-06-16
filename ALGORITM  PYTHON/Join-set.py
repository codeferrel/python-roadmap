#The union() and update() methods joins all items from both sets.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
set1.update(set2)
print(set3) 
print(set1) 

#The update() method inserts the items in set2 into set1:
set3 = {"a", "b" , "c"}
set4 = {1, 2, 3}

set3.update(set4)
print(set3) 