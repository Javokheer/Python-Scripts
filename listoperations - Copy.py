
# Generating a random number of list
from random import randint
list1 = []
for i in range(10):
    num = randint(1, 100)
    list1.append(num)
print('list: ', list1)          #(a) print the list
print('max: ', max(list1))      #(b) print the largest and smallest value
print('min: ', min(list1))
list1 = sorted(list1)
#(c) 
print('third largest: ', list1[-3])
print('third smallest: ', list1[2])   
even = 0
for i in list1:
    if i % 2 == 0:
        even+=1
print('even: ', even)
        
# txt = "Hello \bWorld!"
# print(txt) 
