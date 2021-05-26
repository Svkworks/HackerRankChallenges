# Complete the jumpingOnClouds function in the editor below.
#
# jumpingOnClouds has the following parameter(s):
#
# int c[n]: an array of binary integers
# Returns
#
# int: the minimum number of jumps required
# Input Format
#
# The first line contains an integer , the total number of clouds. The second line contains  space-separated binary integers describing clouds  where .
#
# Constraints
#
# Output Format
#
# Print the minimum number of jumps needed to win the game.
#
# Sample Input 0
#
# 7
# 0 0 1 0 0 1 0
# Sample Output 0
# 4
# Explanation 0:
# The player must avoid  and . The game can be won with a minimum of  jumps:
#
# Sample Input 1
#
# 6
# 0 0 0 0 1 0
# Sample Output 1
# 3
# Explanation 1:
# The only thundercloud to avoid is . The game can be won in  jumps:

import math
import os
import random
import re
import sys

c = [0,0,0,0,1,0]
d = [0,0,1,0,0,1,0]

def jumpingOnClouds(c):
    cnt = 0
    i = 0
    while i < len(c):
        if (i+2 < len(c) and c[i+2]==0):
            print("entered 1 line")
            cnt += 1
            i += 2
        elif (i+1 < len(c) and c[i+1]==0):
            print("entered 2 line")
            cnt +=1
            i +=1
        else:
            print("entered 3 line")
            i += 1
    return cnt



print(jumpingOnClouds(d))