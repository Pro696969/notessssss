#1a i) True ii) True iii) False iv) True v) False vi) True

#1b i) Interpreter is a program that executes instructions written in a programming language. It reads the line of code from a program
# and decodes the instruction and executes it. Example of Interpreter is Python.

#1b ii) Logical error is an error that occurs when the syntax of the program is correct but the program does not produce expected result.
# Example of logical error :- when we want to add two numbers but instead of adding we multiply them.

#1c A module is a file containing definitions and statements. We import it in our program and use the functions defined in it. 
# 3 functions from random module are :- random(), randint(), randrange()

#1d) (i)Analysis - Understanding the problem and understanding the solutions for the necessary problem. (ii)Design - Designing the data 
# (iii) Implementation - Represent the above data in the form of code. (iv) Testing - Testing the code for errors. 

#2a) pgm to transpose a given matrix and display resultant matrix. 

def transpose(a):
    for i in range(len(a[0])):
        for j in range(len(a)):
            print(a[j][i], end = ' ')
        print()

matrix = [[1,2],[3,4],[5,6]]
transpose(matrix)

#2b) Range() is built-in function in python. It is used to generate sequence of numbers, and has 3 parameters. They are start, stop and step.
# Range() usually returns a list of numbers, starting with start value and stops before a specified number.
# By default it starts with 0. 
#Example of range():

for i in range(1,10,2): #1 is starting value, 10 is stop value and 2 is step value.
    print(i) #Output: 1 3 5 7 9

#2c) pgm to print this stupid pattern when n = 4
    
n = 4
for i in range(1,n):
    print(" "*(n-i),'* '*i)

#2d) (i) A tuple is a data-type in python. It is an ordered, immutable sequence of elements. It is represented by round brackets.
#Elements can be of any type and it can be repeated as well. We can access it using indexing. When the code is executed, we get (2,4).
# starts at index 1 and ends at second to the last element.
    
#2d) (ii) Output is ['pq','rs'] as we are not assigning the updated values back to the list.
    
#3a) (i) Output:- {2,3,4}. As n = 4, it will iterate from 2 to 4 and add it to the set.
#3a) (ii) 3 5
    
#3b) A list can be created in 2 ways. We can manually input values enclosed in square brackets. 
# Or we can use the keyword eval to create a list(The input would be [1,2,5,6]). Program to remove duplicates from a list :-
    
def remove_duplicates(l):
    return list(set(l)) #cuz set does not allow duplicates

l = eval(input("Enter a list: "))
print(remove_duplicates(l))
    
#3c) Default parameter is a parameter assigned to a default value. It is accessed by the function when no value is passed to it.
#Example of default parameter:- 

def add(a,b=10):
    return a+b

print(add(5)) #Output: 15

#Keyword arguments are arguments which are passed to the function with the name of the parameter. 
#Example of keyword arguments:-

def add(a,b):
    return a+b

print(add(b=5,a=10)) #b = 5 and a = 10 are the keyword arguments.

#3d) Recursion in python is a method of calling a function within the same function.
#Recursion can be used to solve problems in a simpler way.
#recursive pgm to find sum of digits of a number : 

def sum_digits(n):
    if n == 0:
        return 0
    else:
        return n%10 + sum_digits(n//10)
    
n = int(input("Enter a number: "))
print(sum_digits(n))

#4a) (i) [0, None]
#        [0, None, 1, None]

#4a) (ii) {1,2,3}

#4b) pgm to count number of 1s in a binary representation of integer

def count_bin(n):
    x = bin(n)[2:]
    print('Binary representation of',n,'is',x)
    return x.count('1')

a = int(input("Enter a number: "))
print(count_bin(a))

#4c) (i) Corrected code is :- 
def foo(x):
    def f1():
        print('f1 function')
        x()
    return f1  # Return f1 without calling it

def f2():
    print('f2 function')

p = foo(f2)  # p is now the function f1
p()  # Call p, which is f1

#Output is :- 
#f1 function
#f2 function

#4c) (ii) 1) Valid. 2) Invalid.

#4c) (iii) []. When we use range(-5), it creates a range of numbers from 0 to -5 which is an empty range 
#because the start value is greater than the stop value.

#4d) Lambda functions in Python are anonymous functions that are defined using the lambda keyword. 
#They are used when you need a small, one-time-use function that you don't want to define with a def statement.
#Pgm to use lambda function to add 2 integers :-

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

res = lambda x,y: x+y
print('The sum is : ',res(a,b))

#5a) (i) with the statement marked as question mark, the output is :- 
# In try

# Outside

#the spaces are due to "\n" in the print statement.

#without the statement marked as question mark, we get an error as the except block is not defined.

#5a) (ii) Output is :-
#False
#False (Since the loop is running twice, therefore False is printed twice.)

#5b) (i) Python iterators are objects that can be iterated upon. They are usually used in loops to iterate over a sequence of values.
#Example of iterator:-

l = [1,2,3,4,5]
for i in l:
    print(i)

#the loop iterates over each element of the list l and prints the values.
    
#5b) (ii) In python, A generator is a function that returns an iterator that produces a sequence of
#values when iterated over. One advantage of using generator is that Generators are useful when we want to produce a large sequence
#of values, but we don't want to store all of them in memory at once.

#5c) In python, class is a blueprint for creating objects. It is user-defined and contains attributes and methods, that are used to
#describe the objects. 3 fundamental features of OOP are :-
    
#1) Inheritance - It is a mechanism in which one class acquires the property of another class.
#2) Encapsulation - It is the process of binding the data and the functions that manipulate them.
#3) Polymorphism - It is the ability of an object to take on many forms.
    
#5d) (i) File concept is basically used to store data in different types of file, like text file, binary file, csv file etc.
# Data is permanently stored in the file and can be accessed whenever required.
    
#pgm to read contents of file line by line and display it :-
    
with open('Story.txt','r') as f:
    for i in f:
        print(i,end = '')
