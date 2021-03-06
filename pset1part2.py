'''
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2

For problems such as these, do not include raw_input statements or define 
the variable s in any way. Our automating testing will provide a value of 
s for you - so the code you submit in the following box should assume s is 
already defined. If you are confused by this instruction, please review L4 
Problems 10 and 11 before you begin this problem set.
'''

s = 'azcbobobegghakl'

count = 0
x = 0
y = 1
z = 2
while (z < len(s)):
    if s[x] == 'b' and s[y] == 'o' and s[z] == 'b':
        count += 1
    x += 1
    y += 1
    z += 1
print("Number of times bob occurs is:" + str(count))
