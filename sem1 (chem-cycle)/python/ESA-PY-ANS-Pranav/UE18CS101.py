#1a) i) False ii) iii) True iv) False v) True

#1b) i) 13 (Bitwise OR operator) ii) 5 (Left shift and right shift operator) iii) 3 (Bitwise XOR operator) 
#iv) i) Error (Its trying to divide zero, but python dont know how to do that.) ii) True (cuz one of the condition is true)

#1c) i) Infinite loop of numbers incremented by 1 everytime loop runs ii)aaaaaaaaaaaaaaaaaaaaa x infinity lmao (basically till the loop runs)
#iii) 4321 iv) No output cause the parameters of range function are not set properly. 

#1d) 
def check(pwd):
    if 6 <= len(pwd) <= 12:
        digit = lower = upper = special = False
        for i in pwd:
            if i.isdigit(): digit = True
            elif i.islower(): lower = True
            elif i.isupper(): upper = True
            elif i in '$#@': special = True
        return digit and lower and upper and special
    return False

pwd = input("Enter a password: ")
print("Password is valid." if check(pwd) else "Password is not valid.")


#2a) 
a = 'abcd'
for i in range(len(a)):
    print(a[i:])

#2b) i) [10,20,30,40] ii) Empty string iii) Error iv) {'a1': 'a', 'a2': 'aa', 'a3': 'aaa'}
    
#2c) s1 = set(range(5)) output is {0,1,2,3,4}
# s2 = set(range(0,10,2)) output is {0,2,4,6,8}
# s3 = s1-s2; print(s3) output is {1,3} (elements in s1 but not in s2)
# s4 = s2-s1; print(s4) output is {8,6} (elements in s2 but not in s1)
# s5 = s3&s4; print(s5) output is set(), which is nothing but empty set(elements common in s3 and s4)
# s6 = s3 | s4; print(s6) output is {1,3,6,8} (elements in s3 and s4)

#2d) 
n = 6 
d = {i: i*i for i in range(1, n+1)}
print(d)  

#3a) i) #[10] [123]
# ii) total =  22
#[15, 0, 5, 2, 0, 0] (It goes thru each element in the list, if its -ve, its replaced by 0.)

#3b) a to the power b using recursion

def power(a,b):
    if b == 0:
        return 1
    else:
        return a*power(a,b-1)
    
a = int(input("Enter : "))
b = int(input("Enter : "))
print(power(a,b))

#3c)
def main(s1,s2):
    if len(s1)>len(s2):
        return s1
    elif len(s1)<len(s2):
        return s2
    else:
        return s1,s2
    
s1 = input("Enter string 1: ")
s2 = input("Enter string 2: ")
print(main(s1,s2))
    
#3d)
def sort_dict(d):
    return dict(sorted(d.items(), key=lambda item: item[1][-1]))

d = {1:[100,1,1003],3:[300,3,1002],2:[200,2,1001]}
sortedd = sort_dict(d)
print(sortedd)

#4a) #i) <filter object at .....> ii)[['a'], ['b'], ['c'], ['d']]
#iii)
from functools import reduce

lst = eval(input("Enter list : "))
print(reduce(lambda x,y: x if x>y else y, lst))

#4b) i) 
print([i for i in range(20,100+1) if i % 2 != 0 and str(i) == str(i)[::-1]])

#ii)
n1= [1,2,3,4,5]
a1 = ['one','two','three','four','five']
print([(n,a)for n,a in zip(n1,a1)])

#4c) 0,2,4,6,8,10

#4d) i) 1) import module 2) from module import * 3) from module import function 4) from module import function as fn
#ii) this is with in a.py (1st statement in a.py)
#this is with in abc.py (abc module is imported so this statement is printed)
#abc abc (__name__ variable is 'abc' as abc.py is imported so it prints this)
#a __main__ (__name__ variable is __main__ as a.py is the main file so it prints this)

#5a)
class Shape:
    def __init__(self):
        self.length = 0

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

aSquare = Square(3)
print(aSquare.area())  #Output is 9
aShape = Shape()
print(aShape.area())  #Output is 0

#5b) I) i) try : contains the code which might cause an exception. it can have more than one except block. at most one except block is executed.
# ii) except : the exception in the try block, is handled in the except block. if no exception occurs, except block is skipped.
# iii) finally : this block is executed regardless of the exception. it is used to release external resources.

#II) i) 2 ii) "someError" is wrong, so therefore TypeError occurs.

#5c) 
def countt(f1,f2):
    with open(f1,'r') as f:
        a = f.read()
    
    up = sum(1 for c in a if c.isupper())
    down = sum(1 for c in a if c.islower())

    with open(f2,'w') as f:
        f.write(f'Uppercase letters: {up}\n')   
        f.write(f'Lowercase letters: {down}\n')

countt('file1name.txt','file2name.txt')



