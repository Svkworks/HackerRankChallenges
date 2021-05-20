#Factorials Program
def getFactorial(a):
    if(a==1 or a==0):
        return 1
    else:
       return getFactorial(a-1)*a

#print(getFactorial(5))

#chris alan
# Chris Alan
str = "hello world lol" #Hello   World  Lol

str1 = str.split()
a_string = str.split(' ')
print(' '.join((word.capitalize() for word in a_string)))

#test =" "
# for i in str1:
#     result = " "
#     result =  i[0].capitalize()+i[1:]
#     test += " " + result
#
# print(test.lstrip())

