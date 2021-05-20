#
# The hiker first enters a valley  units deep. Then they climb out and up onto a mountain  units high.
# Finally, the hiker returns to sea level and ends the hike.
#
# Function Description
#
# Complete the countingValleys function in the editor below.
#
# countingValleys has the following parameter(s):
#
# int steps: the number of steps on the hike
# string path: a string describing the path
#
# Function Description
#
# Complete the countingValleys function in the editor below.
#
# countingValleys has the following parameter(s):
#
# int steps: the number of steps on the hike
# string path: a string describing the path
# Returns
#
# int: the number of valleys traversed
# Input Format
#
# The first line contains an integer Steps, the number of steps in the hike.
# The second line contains a single string ,paths of Steps characters that describe the path.
#
# Sample Input:
# 8
# UDDDUDUU
#
# Sample output:
# 1
#
# graphical representaion
#
# _/\      _
#    \    /
#     \/\/

# 12
# DDUUDDUDUUUD
#
# D, D, U, U, D, D, U, D, U, U, U, D
#
# _          /\
#  \  /\    /
#   \/  \/\/
#
# Result 2 for above example


def countingValleys(steps, path):
    seaLevel = 0
    trip =0
    for step in range(0,steps):
        if path[step]=='U':
            seaLevel += 1
        else:
            seaLevel -= 1

        if path[step]=='U' and seaLevel==0:
            trip += 1

    return trip

print(countingValleys(12,"DDUUDDUDUUUD")) # 2
print(countingValleys(8,"UDDDUDUU")) #1