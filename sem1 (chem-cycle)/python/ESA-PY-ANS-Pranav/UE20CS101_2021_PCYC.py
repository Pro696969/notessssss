#1a) i) -6 ii) 7 (Bitwise OR operator) 
#iii) Pro tip:- ~~ always gives the same number, so jus directly do the operation,  but in this case output is -12
#iv) False v) 8

#1b) 
problem = input("Do you have a problem? (yes/no): ")
if problem.lower() == "yes":
    print("Then why worry?")
elif problem.lower() == "no":
    action = input("Can you do something about it? (yes/no): ")
    if action.lower() == "yes" or action.lower() == "no":
        print("Then why worry?")
    else:
        print("Invalid input. Please answer with 'yes' or 'no'.")
else:
    print("Invalid input. Please answer with 'yes' or 'no'.")

#1c) i) False ii) False iii)True iv) True v) False
    
#1d) i) 0 1 2 0 ii) No output iii) Error 
    
#2a)
def first(s):
    a = s.split()
    d = {}
    for i in a:
        if i[0] in d:
            d[i[0]].add(i)
        else:
            d[i[0]] = {i}
    return d

s = 'how much wood would a woodchuck chuck if a woodchuck could chuck wood'
print(first(s))

#2b) i) Error ii) ABCD iii) {1,3,6,7} iv) [2,4,6,5] v) 0,1,2,2,

#2c) 
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

a = int(input("Enter limit : "))
for i in range(a):
    print(fib(i),end = ' ')

#3a) reverse string using recursion
    
def string_rev(s):
    if len(s) == 0:
        return s
    else:
        return string_rev(s[1:]) + s[0]

s = input("Enter string : ")
print(string_rev(s))    

#3b) read a file and display lines from life with line numbers

with open('filename.txt','r') as f:
    for i,j in enumerate(f,start = 1):
        print(i,j)

#3c) i) 15 ii) different ways to import test.py wud be import test, from test import * or import test as t. 
#now to use the increment function in a python program, we can use it this way:-
# n = 5
# print(t.increment(n))
        
#3d) i) Label() :- Creates a label widget used to display text or image in tkinter.
#With this we can change the font, color, size of the text. Syntax, w = Label(parent, options)
# ii) Entry() :- It is used to create an input text field in tkinter. 
#Syntax, w = Entry(parent, options)
        
#4a) i)
num = int(input("Enter : "))
is_prime = True

for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        is_prime = False
        break

if is_prime and num != 1:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

# ii) a) [-1,-2,-3] b) 4 (all integers converted to strings, then joined and then length is found)

#4b)
def filter(f,l):
    a = []
    for i in l:
        if f(i):
            a.append(i)
    return a

l = eval(input("Enter : "))
print(filter(lambda x : x<2,l))

#using filter to remove numbers divisible by 3

numbers = [1,2,3,4,5,6]
print(list(filter(lambda x: x%3 != 0, numbers)))

#4c)0 1 0 1

#4d) i) a) list command - lists entire code with -> symbol to the left of a line at which program has halted.
# b) step command - move line by line, will cause a program to stop within a function.
# c) break command - set breakpoints within a program. Line number must be given.

# ii) python -m pdb fileName.py

#5a) 
class Queue:
    def __init__(self):
        self.limit = 10
        self.people_queue = []

    def enter_queue(self, name):
        if len(self.people_queue) < self.limit:
            self.people_queue.append(name)
            print(f"{name} entered the queue.")
        else:
            print("The queue is full.")

    def exit_queue(self):
        if len(self.people_queue) > 0:
            name = self.people_queue.pop(0)
            print(f"{name} exited the queue.")
        else:
            print("The queue is empty.")

q = Queue()
q.enter_queue("Hitler")
q.enter_queue("Stalin")
q.exit_queue()

#5b) i) try-except-else is mainly used to handle exceptions that might occur in the try clause. 
#Else block is executed only if no exception is raised in the try block.
#But in try-except-finally, the block of code in finally always gets executed regardless of whether an exception is raised or not.

#try:
    # Code that might raise an exception
#except SomeException:
    # Code to run if SomeException is raised
#else:
    # Code to run if no exception was raised

#try:
    # Code that might raise an exception
#except SomeException:
    # Code to run if SomeException is raised
#finally:
    # Code to run no matter what

# ii) a) 5.0 b) No Error

#5c)
k = [1,4,0,5,3]
reciprocal = []

for i in k:
    try:
        reciprocal.append(1/i)
    except ZeroDivisionError:
        reciprocal.append('undefined')

print(reciprocal)




