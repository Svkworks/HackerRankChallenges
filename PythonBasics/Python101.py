# STRING PRINT
print("Hello World")  # Hello World
print("Hello \'World\'")  # Hello 'World'
print("Hello \n World")
# Hello
# World

# MULTILINE STRING
print("""
Hello 
World
Sai
""")
# Hello
# World
# Sai

print("""\
Hello \
World \
Sai 
""")
# Hello World Sai


print("*"*100)
# STRING CONCATINATION
print('Hello ' 'World')  # Hello World
print("Hello " + "Wolrd")  # Hello World
print('Hello ' 'World')  # Hello World
print()

# CHAR INDEXING IN STRINGS
word = "Hello"  # H = 0/-4 | e = 1/-3 | l = 2/-2 | l = 3/-1 | o  = 4/
print(word[:])  # Hello
print(word[2:])  # llo
print(word[0:2])  # He (which excludes the index 2)
print(word[-4:])  # ello

print()
print("*"*100)
# IF STATEMENTS

# input = str(input("Please Mention your City :  "))
input = str('Hyd')

if input.casefold() in ['Del', 'Gur', 'Noida']:
    print("You are from North india")
elif input.casefold() in ['Blr'.casefold(), 'Hyd'.casefold(), 'Che'.casefold()]:
    print("You are from South india")
else:
    print("you may from either west or east india")

# casefold() :- This function is useful to ignore the case-sensitivity of string
print()
print("*"*100)
# FOR LOOP

# List
list = ['Hyd', 'Del', 'Blr', 'Che', 'Mum', 'Kol', 'Amd', 'Kochi', 'Vizag', 'lacknow']
dict = {}

for name in list:
    print(name.casefold())

for index in range(len(list)):
    print("Id : " + str(index) + " -- Value : " + list[index])
    dict[index] = list[index]

print()
print(dict)
# {0: 'Hyd', 1: 'Del', 2: 'Blr', 3: 'Che', 4: 'Mum', 5: 'Kol', 6: 'Amd', 7: 'Kochi', 8: 'Vizag', 9: 'lacknow'}
print()

print("*"*100)
# Dictionary

for item in dict.items():
    print(item)
# (0, 'Hyd')
# (1, 'Del')
# (2, 'Blr')
# (3, 'Che')
# (4, 'Mum')
# (5, 'Kol')
# (6, 'Amd')
# (7, 'Kochi')
# (8, 'Vizag')
# (9, 'lacknow')

print()

for key in dict.keys():
    print("(" + str(key) + ", " + dict[key] + ")")

# (0, Hyd)
# (1, Del)
# (2, Blr)
# (3, Che)
# (4, Mum)
# (5, Kol)
# (6, Amd)
# (7, Kochi)
# (8, Vizag)
# (9, lacknow)
print()

# Range

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n // x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')


print("*"*100)

# FiBONACCI
print()

def fib(input):
    a, b = 0, 1
    c = 0
    while a < input:
        print(a, end=' ')
        c = a + b
        a = b
        b = c


fib(30)
print()
# 0 1 1 2 3 5 8 13 21

print("*"*100)

# KEYWORD ARGUMENTS
print()


def test(input1, *tuple, **keywords):
    print("Hi Currently We Are Printing Method Parameter Value : ", input1)
    print("-" * 40)
    a = 1
    for tuple_value in tuple:
        print("this is tuple value of S.No :", str(a), " and value is : ", tuple_value)
        a += 1

    print("-" * 40)
    for key in keywords:
        print("Key : ", key, " and Value : ", str(keywords[key]))


test("FirstParameterValue", "tuple1", "tuple2", key1="value1", key2="value2")
# Hi Currently We Are Printing Method Parameter Value :  FirstParameterValue
# ----------------------------------------
# this is tuple value of S.No : 1  and value is :  tuple1
# this is tuple value of S.No : 2  and value is :  tuple2
# ----------------------------------------
# Key :  key1  and Value :  value1
# Key :  key2  and Value :  value2

print("*"*100)

#RETURN VALUE ANNOTATIONS

def concatString(*args) -> str:     # Here str is just an annotation that states that method will return string value
    print(' '.join(str(arg) for arg in args))

concatString("sai","venkata")
#sai venkata

print()
print("*"*100)
print()

#DATA STRUCTURES

#List

a = [1,2,3,4,5]
a.append(10)     #[1, 2, 3, 4, 5, 10]
a.insert(6,12)   #[1, 2, 3, 4, 5, 10, 12]
a.remove(12)     #[1, 2, 3, 4, 5, 10]
a.pop(5)         #[1, 2, 3, 4, 5]
a.sort(reverse=True)  #[5, 4, 3, 2, 1]
print(a)

b = a.copy() #[5, 4, 3, 2, 1]
print(b)
print()


#for-Loop
for x in b:
    print(x)

print()

[print(i) for i in b]


#SET

a = set([1,2,3,2,3,1,1,2,3,4,5])  #{1, 2, 3, 4, 5}
print(a)
print()

#Array

a = (1,2,3,4,5,6)
print(type(a)) #<class 'tuple'>
print(a[0])

print()


#Dictionary

di = {1:"sai",2:"venkat",3:"krishna",4:"prasad"}

for i in di.items():
    print(i)
# (1, 'sai')
# (2, 'venkat')
# (3, 'krishna')
# (4, 'prasad')

print()

for i in di.keys():
    print("key : {0} and Value : {1}".format(i,di[i]))

print()

print("*"*100)


#FILE READING, WRITING,

with open("/Users/saim/Documents/Svk_Work/Learning_Documents/Spark_PySpark/Datasets/test.txt",'r+') as a: # r-read, w-write,r+ - Read and write
    a.write(" How are you doing ")



