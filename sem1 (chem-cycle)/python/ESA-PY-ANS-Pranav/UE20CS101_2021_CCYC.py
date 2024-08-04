#1a) i) 0.5
# ii) 4
# iii) -10
# iv) 1 True
# v) 4

#1b) 
for i in range(4, 0, -1):
    for j in range(i, 5):
        print(j, end=' ')
    print()

#1c) i) False ii) True iii) False iv) False v) True
    
#1d) i) Error ii) 2 4 iii) a a a a a a 

#2a)
def freq(s):
    a = s.split()
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d

a = "how much wood would a wood chuck chuck if a wood chuck could chuck wood"
print(freq(a))

#2b) i) Error ii) ['ab','cd'] iii) {8,10} iv) [2,5,7] v) h,n,o,p,t,y,

#2c) func which returns all prime numbers from 2 to n

def prime(n):
    l = []
    for i in range(2,n+1):
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            l.append(i)
    return l
a = int(input("Enter limit : "))
print(prime(a))

#3a) GCD of 2 numbers using recursion

#3b)
def freq(filename, word):
    with open(filename, 'r') as f:
        a = f.read()
    w = a.split()
    return w.count(word)

filename = 'your_file.txt'  # replace with your file name
word = 'chuck'
frequency = freq(filename, word)
print(f"'{word}' occurs {frequency} times in the file")

#3c) i) 9 ii) [3,4,2]

#3d) i) Syntax for button is :- w=Button(parent,options), 
#where parent is the window in which button is to be placed and 
#options are the different parameters of the button which can be set to change the look of the button.
# Example of button :- w = Button(root, text = 'Click Me !', bd = '5', command = main)

#3d) ii) pack() packs widgets in rows or columns. grid() places widgets in a 2D table. 
#pack() is mainly used for simple layouts and grid() is used for complex layouts.
#Example of pack() :- w = Button(root,text = 'Hello!)
#w.pack()

#Example of grid() :- W = Button(root,text = 'Hello!')
#w.grid(row = 1, column = 1)

#4a) i) 
print([x for x in range(7,51) if x%7 == 0 and x%2 == 0])

#ii) a) [-1,-2,-3] b) [2,3,0,1,6] (Bitwise XOR operator)

#4b) 
def real_reduce(fn,seq):
    r = seq[0]
    for i in seq[1:]:
        r = fn(r,i)
    return r

print(real_reduce(lambda x, y: x*y, [1, 2, 3, 4]))

#using reduce to find shortest string from list of strings 

from functools import reduce
strings = ['this','is','the','endgame']
print(reduce(lambda x,y: x if len(x) < len(y) else y, strings))

#4c) 0 1 1 2 3 (Fibonacci series)

#4d) will edit soon.

#5a) 
class Stack():
    def __init__(self):
        self.limit = 0
        self.plate_stack = []

    def add2stack(self,plate_id):
        if len(self.plate_stack) >= self.limit:
            return "Stack is full. Unable to add more plates."
        else:
            self.plate_stack.append(plate_id)
            return "Plate added."
        
    def popStack(self):
        if len(self.plate_stack) == 0:
            return "Stack is empty. No more plates to remove." 
        else:
            return self.plate_stack.pop()
        
s = Stack()
print(s.add2stack(1))  
print(s.add2stack(2)) 
print(s.popStack())

#5b) i) # Inheritance in python is the process by which one class takes on the attributes and methods of another.
#Basically a child class inherits the methods and attributes of the parent class. Object composition is used when
# you want to use some methods and attributes of a class in another class without using inheritance.

#ii) a) 2 b) 2 

#5c) 
def get_numbers():
    numbers = []
    for i in range(10):
        num = int(input("Enter a non-zero number: "))
        if num == 0:
            raise ValueError("Zero is not allowed.")
        numbers.append(num)
    return numbers

try:
    print(get_numbers())
except ValueError as e:
    print(e)

