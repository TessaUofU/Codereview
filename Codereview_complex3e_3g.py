#Problem 3: Set combinations

#Given the predefined sets below and using set methods

#3e add 9 to the set
#3f Using == compare this set to the list in one_a
#3g Explain why they are not the same. What would you need to change if you wanted this to be True?


three_setA = {1,2,3,4,5}
three_setB = {2,3,4,5,6}
three_setC = {3,5,7,9}
three_setD = {2,4,6,8}
three_setE = {1,2,3,4}



three_d = three_setC.union(three_setD, three_setE) #need this set to continue with problem 3e

three_e = three_d.copy()                           #created a copy of the three_d set to add the element 9 to it
three_e.add(9)                                     #add 9 to the set
print("3.E:" ,three_e)                             #print the new list as the answer for the problem 3e

one_a = [0, 8, 7, 1, 5, 6, 4, 2, 3, 9, 1, 2]       #copied list one_a for reference for problem 3f
three_f = set(one_a)                               #converted list to set to compare to 3e set
if three_f == three_e :                            #Use if/else statement to compare the sets
    print("3.F: Equal")
else:
    print("3.F: Not Equal")

three_g = three_f.difference(three_e)              #Print out the differences between the sets and what needs to be changed.
print("3.D: The differences between the sets of one_a and three_e. The elements requiring being changed:" , three_g)
