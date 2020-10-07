# Problem 01

#If we list all the natural numbers (integers greater than 0) below 10
#that are multiples of 3 or 5, we get 3, 5, 6, and 9. The sum of these
#numbers is 23.

#Write a Python program that finds the sum of all the multiples of 3 or
#5 below a given number, and use that program to find the sum of all
#the multiples of 3 or 5 below 1000.


#Author: Ian Worthington

upperlim = 999
sum = 0;

for x in range(1,upperlim):
if (x mod 3) == 0:
sum = sum + x
elif (x mod 5) == 0:
sum = sum + x

#The variable sum is the sum
