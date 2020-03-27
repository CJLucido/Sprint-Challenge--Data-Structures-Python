import time
from recursive_sorting import merge

import sys
sys.path.append('../Queue_and_stack')
from dll_queue import Queue

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

names_1.sort()
j = 0
for j in range(len(names_1)-1):
    last = names_1[j]
    current = names_1[j+1]
    if names_1[j+1]:
        if names_1[j+1] == last:
            names_1[j+1] = str(j)
    else:
        continue
    j +=1

names_2.sort()
j = 0
for j in range(len(names_2)-1):
    last = names_2[j]
    current = names_2[j+1]
    if names_2[j+1]:
        if names_2[j+1] == last:
            names_2[j+1] = str(j-1)
    else:
        continue
    j +=1
#sorting cuts off .3 seconds
names_3 = names_1 + names_2
names_3.sort()

i = 0
for i in range(len(names_3)-1):
    last = names_3[i]
    if names_3[i+1]:
        if names_3[i+1] == last:
            if names_3[i+1] not in duplicates:
                duplicates.append(names_3[i+1])
    else:
        continue
    i +=1
#!!! runtime: 0.03125715255737305 seconds




# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

#print(names_1)# already an array
# names_1.sort()
# names_2.sort()




end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")


#THE Original RUNTIME IS O(n!)
# The runtime complexity is at best O(n), if one of the files was only 1 word, but at worst and in actuality it is O(n!) because we have to make a combination for every possible pair just to ensure that there are no duplicates. Put another way, we are running through the entire n of  the second list the n of the first amount of times .







# Use an LRU Cache so that we can do one for loop to load it and another to check every item in the second file

# SCRATCH THAT can't use a dictionary, can an LRU cache be made without a dictionary? not enough time to answer that question 

# maybe take all the items of the first list and put them in a stack, then we can do a for loop for the second list against it and when one is found pop it from the stack and add it to the duplicates. this will lower our entries in the stack to check every time...at it's worst that is still O(n!)

# the rubric suggests mergesort
# sort both, then compare using a stack for one of them


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
