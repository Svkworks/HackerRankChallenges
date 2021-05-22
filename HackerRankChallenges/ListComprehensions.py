# Input Format
#
# Four integers  and , each on a separate line.
#
# Constraints
#
# Print the list in lexicographic increasing order.
#
# Sample Input 0
#
# 1
# 1
# 1
# 2
# Sample Output 0
#
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
# Explanation 0
# Each variable  and  will have values of 0 or 1 . All permutations of lists in the form .
# Remove all arrays that sum to  to leave only the valid permutations.
# #
# Each variable  and  will have values of  or . All permutations of lists in the form .
# Remove all arrays that sum to  to leave only the valid permutations.
#
# Sample Input 1
#
# 2
# 2
# 2
# 2
# Sample Output 1
#
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1]


x=1
y=1
z=1
n=2

def listComprehension(x,y,z,n):
    lst2 = []
    for i in range(0, x + 1):
        for j in range(0, y + 1):
            for k in range(0, z + 1):
                lst1 = []
                lst1.append(i)
                lst1.append(j)
                lst1.append(k)
                lst2.append(lst1)

    print(lst2)
    lst3 = []
    for i in range(len(lst2)):
        if sum(lst2[i]) == n:
            lst3.append(lst2[i])

    return list(filter(lambda x: x not in lst3, lst2))


print(listComprehension(x,y,z,n))
#[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]




