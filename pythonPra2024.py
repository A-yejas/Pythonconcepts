'''a= [1, 2, 3]
b = ["a", "b", "c", "d", "e", "f", "i"]
print([i%len(a) for i in range(len(b))])
print([(i,i%len(a)) for i in range(9)])
And:- [0, 1, 2, 0, 1, 2, 0]
[(0, 0), (1, 1), (2, 2), (3, 0), (4, 1), (5, 2), (6, 0), (7, 1), (8, 2)]
'''
###
# inp = ["a", "b", "c", "d", "a"]
# a = {}
# for i in inp:
#     a[i] = a.get(i, -1)+1
#     # print(a[i])
# print(a)
# # {'a': 1, 'b': 0, 'c': 0, 'd': 0}
# d=[k if v==0 else v for k, v in a.items()]
# print(d)
##
# arr = [[1,2,3], [4,5,6],[7,8,9]]
# mid = len(arr[0])/2
#
# mid = len(arr[0])/2 if len(arr)>0 else 0
# print([ i[mid] for i in arr])
###
# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# middle_elements = [row[2] for row in a]  # List comprehension to extract middle elements
# print(middle_elements)  # Outputs: [2, 5, 8]

# a=[1,2,3]
# a.pop(1)
# print(a)
######
# def shout(text):
#     return text.upper()
#
# def whisper(text):
#     return text.lower()
#
# def greet(func):
#     # storing the function in a variable
#     greeting = func("""Hi, I am created by a function passed as an argument.""")
#     print (greeting)
#
# greet(shout)
# greet(whisper)
#####
# Python program to illustrate functions
# Functions can return another function

# def create_adder(x):
#     def adder(y):
#         return x+y
#
#     return adder
#
# add_15 = create_adder(15)
#
# print(add_15(10))

# Python program to illustrate functions
# Functions can return another function

def create_adder(x):
    def adder(y):
        return x+y

    return adder

add_15 = create_adder(10)

print(add_15(15))
# l1=[1,2,3]
# l2=[4,5,6]
# a=list(map(lambda a,b:a+b,l1,l2))
# print(a)
# d=[i for i in range(10) if i%2==0]
# print(d)
# a=5
# b=6
# c=7
# a,b,c = c,b,a
# print(a,b,c)

# temp = a
# a =b
# b=temp
# print(a, b)
l=[2, 4, 1, 3, 10, 6, 7]
l1=[]
l2=[]
for i in l:
    for j in range(len(l)):
        if i < l:
            l1 = i
        else:
            l2 > j

