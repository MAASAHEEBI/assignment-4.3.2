'''Write a Python program to square the elements of a list using map() function.

Sample List: [4, 5, 2, 9]
Square the elements of the list:

[16, 25, 4, 81]'''

def list1():
    n=int(input('number of elements: '))
    l=[] 
    for i in range(n):
        m=int(input('enter numbers: '))
        l.append(m)
    return l

print(list(map((lambda x:x**2),list1())))





