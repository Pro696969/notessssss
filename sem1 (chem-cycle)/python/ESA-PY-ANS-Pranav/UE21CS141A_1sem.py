#1a) i) True ii) False iii) True iv) False v) False

#1b) i) 20 1 ii) True iii) True iv) Error (b not defined) 

#1c) i) No output. ii) Compiler is a program which converts high level programming language to machine language all at a time.
# Interpreter is a program which converts high level programming language to machine language line by line. 
# Compiled codes are faster than interpreted codes. Errors are displayed in Compiler after the whole code is compiled, whereas
# in Interpreter, errors are displayed after each line is interpreted.

#1d)
n = 1
for i in range(3):
    for j in range(3):
        print(n, end = ' ')
        n += 2
    print()

#2a) i) [] ii) {True: 4, False: 3} iii) {'C', 'A', 'Z'} (can be of any order)

#2b) i) 
s = 'python';print(s[::-1])

#ii)
lst = []; lst.append(10)

#iii)
t = (11,22,33,44,55); print(len(t))

#iv)
var = 'Mississippi'; print(''.join(dict.fromkeys(var)))

#v)
d = {1:1, 2:4, 3:9, 4:16};print(' '.join(map(str, d.keys())))

#2c)
SRNS = ['21ECS003','21ECS013','21ECS036','21ECS033']
x_marks = [98,99,80,90]
y_marks = [91,90,84,92]

marks_dict = {srn: x + y for srn, x, y in zip(SRNS, x_marks, y_marks)}
print(marks_dict)

#2d)
total = 0
p_total = 0

with open('filename.txt','r') as f:
    for i in f:
        total += 1
        if i.lower().startswith('p'):
            p_total += 1
print(f'Total number of lines: {total}')
print(f'Total number of lines starting with p: {p_total}')

#3a) i) 150 ii) do it yoselff iii) [3,3,3,3] iv) python (for each element, the third value is calculated. so in python, its 't',
# in anaconda, its 'a', in kingcobra, its 'n' and in blackmamba, its 'a'. So, the output is 'python', as t has the highest ASCII value.)

#3b) A closure is a nested function which has access to a free variable from an enclosing function that has finished its execution.
#Three characteristics of a Python closure are:
# It is a nested function
# It has access to a free variable in outer scope
# It is returned from the enclosing function

#3c)
def print_even_length_words(s):
    a = s.split()
    for i in a:
        if len(i) % 2 == 0:
            print(i, end = ' ')


print_even_length_words("Indians stranded in Ukraine have been evacuated")

#3d)
def length(s):
    if s == '':
        return 0
    else:
        return 1 + length(s[1:])

a = input("Enter : ")
print(length(a))

#4a) i)
I = ['CR7','Messi','Naymar','Lewandowski']
print([x[0] + x[-1] for x in I if len(x) >= 3])

#ii)
string = 'This is final exam'
print(sum([1 for char in string if char == ' ']))

#4b) i) 30 16 ii) [1, 2, 3, 4] 4

#4c) Different ways to import module are as follows :- 
#1) import module 2) from module import * 3) from module import function 4) from module import function as fn

#4d) 
def divisible(n):
    for i in range(n+1):
        if i % 7 == 0:
            yield i

for i in divisible(50):
    print(i, end = ' ')

#5a)
#Exception
#this is try block
#Some error occured
#End of try
#That's all for the semester
    
#5b)
class myString:
    def __init__(self):
        self.s = ""
    def get_String(self):
        self.s = input("Enter a string : ").upper()
    def print_String(self):
        print(self.s.lower())
    
a = myString()
a.get_String()
a.print_String()

#5c) In python, inheritance is a way of creating a new class for using details of an existing class without modifying it. 
# In other words, we can say, a child class inherits from a parent class. It is used to represent real-world relationships.
#Example of inheritance in python:-

class Person:
    def __init__(self, name):
        self.name = name
    def print_name(self):
        print(self.name)
class Student(Person):
    def __init__(self, name):
        super().__init__(name)
        

s = Student('Prawns')
s.print_name()

#5d)
def main():
    val = int(input("Please enter a value from 0 to 100: "))
    if val > 100:
        raise ValueError("Error!The entered value is more than 100.")
    return val

try:
    print(main())
except ValueError as e:
    print(e)

