# David Markham 2019-02-17
# Solution to problem number 1
# Write a program that asks the user to input any positive integer
# And outputs the sum of all numbers between one and that number.


start = 10
# start asks the user to input the positive integer number 10.
ans = 0 
# ans is where the answer started and what it would finally become, 1+2+3+4 and so on, up until number 10.
i = 1
# keeps track of where you are in the calculation 

if ans> 10: 
  print("Unfortunately this is not a positive integer")
# This will help the user get the desired sum 

while i <= start:
    ans = ans + i
    i = i + 1
# while i is less than or equal to start we kept adding the all the numbers until we reached 10
# this is called a loop statement 
print(ans)