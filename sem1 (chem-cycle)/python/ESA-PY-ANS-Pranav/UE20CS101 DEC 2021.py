#1a) i) 0.5 ii) 4 (Right shift Left Shift again) iii) -8 iv) 1,True v) 4

#1b) i) 0 1 2 0 ii) No output iii) Error 

#1c) 
for i in range(4, 0, -1):
    for j in range(i, 5):
        print(j, end=' ')
    print()

#1d) i) False ii) False iii)True iv) True v) False
    
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

#2b)
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

#2c)i) Error ii) ABCD iii) {1,3,6,7} iv) [2,4,6,5] v) 0,1,2,2,
    
#3a)
def freq(filename, word):
    with open(filename, 'r') as f:
        a = f.read()
    w = a.split()
    return w.count(word)

filename = 'your_file.txt'  # replace with your file name
word = 'Bengaluru'
frequency = freq(filename, word)
print(f"'{word}' occurs {frequency} times in the file")

#3b)
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

a = int(input("Enter : "))
b = int(input("Enter : "))
print(gcd(a,b))

#3c) i) Label() :- Creates a label widget used to display text or image in tkinter.
#With this we can change the font, color, size of the text. Syntax, w = Label(parent, options)
# ii) Entry() :- It is used to create an input text field in tkinter. 
#Syntax, w = Entry(parent, options)

#3d) i) 9 ii) [3, 4, 2] 

#4a) i)
n = int(input("Enter : "))
print(0 not in [(n % j) for j in range(2, int(n**0.5) + 1)])

# ii) a) [-1,-2,-3] b) [2,3,0,1,6] (Bitwise XOR operator)
    
#4b) mimic filter

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

#4c) 0 1 1 2 3 (Fibonacci series)

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

#5b) ii) 5.0 

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
