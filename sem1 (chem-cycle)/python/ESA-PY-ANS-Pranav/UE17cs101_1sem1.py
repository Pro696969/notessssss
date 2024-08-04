#1a) print("text") ' " ' was missing. 
#print("25"/"5") gives error because we cannot divide string by string.
# a = 10; b = 0; print(str(a*b)) gives output as "0".
# a = 10; b = 10; print(a === b) gives error cuz it shd be a == b.
# a = 10; print(++a) gives output as 10 cuz ++a is just treated as a by python interpreter.

#1b) x = 100; y = x; y = 200; print(x) Output is 100
#x = [100, 200]; y = x; y = [300, 400]; print(x) Output is [100,200]
#x = [100, 200]; y = x; y.extend([300, 400]); print(x) Output is [100,200,300,400]
#x = [100, [200]]; y = x; y[0] = [300, 400]; print(x) Output is [[300,400],[200]]
#x = [100, 200]; y = x; y += [300, 400]; print(x) Output is [100,200,300,400]

#1c) 5 == 5 == 5 Output is True
#(2 + 3, 3 + 2) * 2 Output is (5,5,5,5)
# 2 * "25" Output is "2525"
# True and True or not True Output is True
#5 in range(5) Output is False

#1d) (-25) ** 0.5 returns complex number. so type is <class 'complex'>
#"pes"[1] returns 'e' so type is <class 'str'>
# {"x" : 25, 25 : "y"}[25] == 'x' returns False so type is <class 'bool'>
#{} type is <class 'dict'>
#set({}) error as we cant convert empty dictionary to set.

#2a) (i) 2 ii) 2 The program finds remainded when a number n is divided by 2 using % operator which gives remainder. 
# now with the remainder, right shift of 2 bits is done and therefore, output is 2 for both the cases.
#2b) pgm for geometric progression

a = int(input("Enter first term : "))
r = int(input("Enter common ratio : "))
n = int(input("Enter the limit : "))
term = a
while term * r < n:
    term *= r
print(f'Biggest number in the progression less than {n} is {term}')

#2c) (i) This code is to find prime factors of a number. Output is 2 3 3 3 for 54, as 54 = 2 * 3 * 3 * 3. Similarly for 24, output is 2 2 2 3.

#2d) when n = 4, get the pattern. 
n = int(input("Enter : "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        min = i if i < j else j
        print(n- min + 1, end = " ")
    print()

#3a) [[0], [0, 1], [0, 1, 4], [0, 1, 4, 9]]

#3b) 
a = ['karnataka', 'tamilnad', 'karnataka', 'karnataka', 'tamilnad', 'kerala']
b = ['mysore', 'chennai', 'hassan', 'shimoga', 'madurai', 'trivandrum']

d = {}
for key, value in zip(a, b):
    if key in d:
        d[key].append(value)
    else:
        d[key] = [value]

print(d)

#3c) i) {'1','2','3','4'} is one example. as set is unordered, we cannot predict the output.
# ii) same as previous one.
# iii) {'34','12'} is one example. as set is unordered, we cannot predict the output lol.
# iv) {1,2,3,4} is one example. creating a set from a set doesn't change anything.
# v) first concatenation takes place. then it displays {'1','2','3','4'} but its jus an example.

#3d) 
a = ['m', 'i', 's', (2, 1), (1, 1), (2, 3), 'p', (8, 1), (1, 1)]
b = ''
for i in a:
    if type(i) == str:
        b += i
    elif type(i) == tuple:
        x = i[0]
        y = i[1]
        b += (b[x:x+y])
    else:
        print('invalid input')

print(b)

#4a) 
def foo(s):
    a = s.split(',')
    a.sort()
    return ','.join(a)

print(foo("hi,how,are,you?"))

#4b) In the case of foo((1, 2, 3), (4, 5)), there are 3 elements in x and 2 elements in y, so there are a total of 3 * 2 = 6 pairs.
#Therefore,output is 6.
#In the case of foo({10: "ten", 20: "twenty"}, {30: "thirty"}), it iterates over the keys of the dictionary.
#So, there are 2 keys in x and 1 key in y, so there are a total of 2 * 1 = 2 pairs. Therefore, the function returns 2.

#4c) 
a = [1,2,2,2,4]
b = [2,5,10,20,5]
# i) 
res = sum(a) > sum(b)
# ii)
c = [100 - i for i in a]
# iii)
from functools import reduce
print(reduce(lambda x,y: x*y,a))

#4d) for x = A(), output is ctor dtor.
# for y = x, no output is produced.
# z = A(), output is ctor ctor dtor dtor.
# del x, output is ctor dtor.
# y = 111, output is not produced.
# x = 222, output is not produced.

#5a) i)
points = [(1, 2), (0, 0), (-1, 2), (3, -4), (0, 5)] #example of points
print([(x, y) for x, y in points if x > 0 and y > 0]) #>0 cuz first quadrant all +ve.

#5a) ii)
#one
#three :  abc
#two :  __main__

#5b) with the statement marked as X, output is :-
#three
#ondu
#mooru
#idu
#aaru

#without the statement marked as X, output is :-
#three
#ondu
#nameerror

#5c)not sure about answer sori.

#5d) (i) 11 22 33 
#(ii) True False True False
