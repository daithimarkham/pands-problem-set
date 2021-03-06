# David Markham
# Data Analytics Problem Set 2019 - G.M.I.T.
# Pands Problem Set
# Lecturer: Ian McLoughlin

In this problem set we were asked to set out and achieve a number of problems over ten weeks. Below are a list of all the problems with a detailed analysis of how I achieved the outcome of each problem. 

# - Problem Number 1

## I was asked to get the user to input a positive integer of 10 and output the sum of all numbers between 0 and 10. 

First I wrote a simple statement to get the user to input a positive integer, int(input ("Please enter a positive integer: "))

Asks the user to input the positive integer number.

Then I wrote the following statement. 

if i <= 0:
  print("Unfortunately this is not a positive integer")

This will prevent the user from entering anything other than a positive integer.


I started the calculation with total 
 
  total = 0


I calculated the the sum by entering the following formula: 

 while i > 0:
    total = total + i
    i = i - 1

I used a compound statement here, using the while loop. While "i" was greater than 0, add the total plus "i".

The last line, i = i - 1. Whatever the user enters, subtract 1 and keep going until it reaches 0, adding all while looping.

Then I entered print(ans) which gave us the sum of 55 if the user enters the positive integer of ten. 


# - Problem Number 2

## This problem required me to write a program which outputs whether or not today begins with the letter "T". 

I started by importing the date and time by entering the following statement:

 if datetime.datetime.today().weekday() == 1:

    print("Yay! Today is a day that begins with the letter T")

Monday is 0, Tuesday is 1 and so on. 

I then entered an elif statement which helps us determine if there is more than one day which begins with the letter "T", such as Thursday. 

elif datetime.datetime.today().weekday() == 3:
    print("Yay! Today is a day that begins with the letter T")

To finish with I entered an else statement as follows to give me the answer: 

else:
    print("Unfortunately today does not begin with the letter T")


# - Problem Number 3

## In this problem I had to write a program that prints all the numbers between 1000 and 10,000 that are divisible by six but not by twelve. 

I found information relating to this problem on The Python tutorial. 

The program should start with 1002, 1014, 1026 etc and end up with 9990. 

I used the built in range function which generates arithmetic continuation from 1000 towards the final number I entered in the range which was 10,000.
This was for i in range (1000, 10000)

Next I came up with two maths formulas as follows which enabled me to do calculation: 

if i % 6 == 0 and i % 12!=0.
This stated for all the numbers in the range that could be divided by six but not by twelve. 

Finally I typed print(i), which gave all the numbers that could be divided by six in the range. 

Ref: The Python tutorial, viewed on the 2019-02-21, https://docs.python.org/3/tutorial/controlflow.html#the-range-function

# - Problem Number 4 

## This problem involved writing a program that asks the user to input any positive integer and outputs the successive values of the following calculation.
## At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one.


First I entered a statement which helps the user to input the appropriate integer, such as, 
n = int(input("Please input a positive integer"))
I then followed up with an if statement to notify the user if they had not entered a positive integer: if n < = 0:
               print("Unfortunately this is not a positive integer")

I then entered the Collatz conjecture. "The Collatz conjecture is a conjecture that a particular sequence always reaches 1. The sequence is defined as: start with a number n. The next number in the sequence is n/2 if n is even and 3*n + 1 if n is odd." 


I then created a while loop which which ensured the loop was ran from the number the user entered until number one, followed by an if statement. This was as follows;
    while n > 1:
      print(n, end = ' ')
      if (n % 2): The modulus sign determines if there is a remainder when n is divided by two.  
          n = n * 3 + 1 This calculation was done if the number was not even. The answer was multiplied by three and one was added on to it. 
Next I entered an else statement which instructed Python what to do if the number was even. If it was divisible by two, do the calculation until it reaches number one. 
      else: 
          n = n // 2
          print(1, end= '') 

Then I wrote the following to print out the answer at the end of the program. 
print("Sequence: ", end= '')

That was the solution to number four. 

Ref: Python Program to test Collatz Conjecture for a Given Number, viewed on 2019-03-21 https://www.sanfoundry.com/python-program-test-collatz-conjecture-given-number/ 

# - Problem Number 5 

## Write a program that asks the user to input a positive integer and tells the user whether or not the number is a prime. 

I asked the user to input a positive integer, with a simple statement:
n = int(input("Please enter a positive integer: ")) This will help the user to input a positive integer.
if n < 1:
    print("Unfortunately this is not a positive integer")
If the user put int the wrong integer, this will notify them. 


This checks for the factors, does the modulus give you a remainder when divided by the input. 
And states whether or not it is a prime number when it does the calculation. 
This is achieved by if and else statements.


Below are the factors in how how the calculation was done. Its states that the input has to be greater than one, and in the range from two to the input, and determines if there is a remainder when n (input) is divided by the modulus.  

if n > 1:
   for i in range(2,n):
       if (n % i) == 0:

 This will state if the number is a composite number, which has factors other than one and itself;
           print(n,"is not a prime number")
           break 

The break statement above is when the loop is terminated by a break statement. This is exemplified by the following loop, which searches for prime numbers.
Ref: Python Tutorial, break and continue statements, viewed on 2019-03-22 https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops 

   else:
       print(n,"is a prime number")
This will state if the integer entered is a prime number or not. 

Ref: Python by Programize, Program to check prime number. Viewed on 2013-03-22 https://www.programiz.com/python-programming/examples/prime-number


# - Problem Number 6 

## Write a program that takes a user input string and outputs every second word.

First of all write a simple statement to get the user to enter any string. This is done by;
sentence=(input("Please enter a sentence: "))

Next I split the sentence into spaces and output every second word using the splice function. So whatever the user enters, every second word will be displayed. This was done by the following; 

words = sentence.split(' ')
print(words[::2]

I found information which enabled me to complete this on the Python Tutorial, and also on Stackflow. 

Ref: Python Tutorial, viewed on 2019-03-23. https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str

# - Problem Number 7 

## Write a program that that takes a positive floating point number as input and outputs an approximation of its square root.

I started off with importing the maths function on Python. This is 'import math'.

Then I asked the user to please enter a floating positive integer. 
 n = float(input("Please enter a positive floating point number: ")). 

Next I wrote a simple while statement to to ensure the user inputs a positive floating point number. This was as follows,  while n <= 0:
    print("Unfortunately this is not a positive floating integer"). 

Then I used the the floating point computation to get the square root of the user input.
n_sqrt = n ** 0.5

Finally I entered print the square root, with one floating point. (%.1f) 
print('The square root of %0.1f is %0.1f'%(n ,n_sqrt))

That was my solution to problem number 7. I found information online and on The Python tutorial to help me. 

Ref; viewed on 2019-03-24,  https://www.programiz.com/python-programming/examples/square-root
Ref; viewed on 2019-03-24, https://docs.python.org/3/search.html?q=how+to+get+square+root&check_keywords=yes&area=default 


# - Problem Number 8 

## Write a program that outputs today’s date and time in the format, Monday, January 10th 2019 at 1:15pm.

I wrote a function built into Python to import today's date and time. This was done by: import datetime.

Next I entered a statement which outputs today's date and time: now = datetime.datetime.now() 

I was having trouble writing code for the st, nd, rd and th. I searched a number of sites where I found information and code which enabled me to write code to output this. I wrote an if, elif and else statements to achieve this. This is as follows;

day_month = int(now.strftime("%d"))
if day_month in (1,2,3):
    day_suffix = 'st'
elif day_month in (2,22):
    day_suffix = 'nd'
elif day_month in (3,23):
    day_suffix = 'rd'
else:
    day_suffix = 'th'

I then done some research online in The Python tutorial, which enabled me to put in the required code to output the input from the user, in the date and time format required to do this problem. This is as follows: 
print (now.strftime("%A %dth %B %Y %H:%Mpm")) Which prints out: Tuesday March 26th 2019 10:29 am

Ref: wEresource, viewed on 2019-03-25, # https://www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-1.php  

Ref: Python Tutorial, viewed on 2019-03-25, https://docs.python.org/3/library/datetime.html?highlight=how%20import%20date 

Ref: Python Tutorial, viewed on 2019-03-26, https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior 

Ref: Stackoverflow, viewed on 209-03-26, https://stackoverflow.com/questions/3644417/python-format-datetime-with-st-nd-rd-th-english-ordinal-suffix-like 


# - Problem Number 9 

## Write a program that reads in a text file and outputs every second line. 
## The program should take the filename from an argument on the command line.

For this problem I got information from lectures in week week seven, The Python Tutorial and from Stack Overflow. 

I started off using a statement which asks the user to input the file which data was required to be extracted from. 

user = input("Please open file: ") 

Then I found help online how to enter code to output every second line in a text file which the user enters. 
This I found on Stack Overflow. I entered code which made the program print every even line in the file that the user enters, and print it out.

I created a text file mobydick.txt, with the text from the first paragraph to ensure it was the correct data being extracted, which was required in this problem. The output was correct. 

This was the problem solved for number nine. 

with open(user, 'r') as f:
    count = 0
    for line in f:
        count+=1
        if count % 2 == 0:
            print(line) 

I ended with f.close() which is good practice to end a program when you've finished. 

Ref: The Python Tutorial, viewed on 2019-03-26, https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

Ref: Stack Overflow, viewed on 2019-03-26, https://stackoverflow.com/questions/30551945/how-do-i-get-python-to-read-only-every-other-line-from-a-file-that-contains-a-po 


# - Problem Number 10
## Write a program that displays a plot of the functions x, x2 and 2xin the range [0, 4].

I imported two functions from the Python library called Matplotlib and Numpy functions which generate data for the user.
I then wrote a simple statement to list the data for the functions on the x-axis; x = np.arange (0.0, 4.0, 0.5). 

Next I set values for the functions, x, x*2 and 2*x. 
y1 = x 
y2 = x**2
y3 = 2**x

Next I found information online which helped me plot the functions within the range 0 and 4.

pl.plot([0,4])
pl.xlabel('X-Axis')
pl.ylabel('Y-Axis')
Finally I entered pl.show() Which displays a graph when you enter the information on the ipython command line. 

Ref; Real Pyhton, viewed on 2019-03-30, https://realpython.com/python-matplotlib-guide/ 
Ref; Tutorialspoint, viewed on 2019-03-30, https://www.tutorialspoint.com/matlab/matlab_plotting.htm
  
Problem set completed on 2019-03-30,
David Markham. 