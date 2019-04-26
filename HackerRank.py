#Task
#You are given a string .
#Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
#In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
#In the second line, print True if  has any alphabetical characters. Otherwise, print False.
#In the third line, print True if  has any digits. Otherwise, print False.
#In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
#In the fifth line, print True if  has any uppercase characters. Otherwise, print False.
s = "qA2"

first_line = second_line = third_line = fourth_line = fifth_line =  False

for i in range (len(s)+1):
    if s[i].isalnum():
        first_line = True
    if s[i].isalpha():
        second_line = True
    if s[i].isdigit():
        third_line = True
    if s[i].islower():
        fourth_line = True
    if s[i].isupper():
        fifth_line = True

print(str(first_line) + "\n" + str(second_line) + "\n" + str(third_line) + "\n" + str(fourth_line) + "\n" + str(fifth_line))

#12.Let's learn about list comprehensions! You are given three integers  and  representing the #dimensions of a cuboid along with an integer . You have to print a list of all possible #coordinates given by  on a 3D grid where the sum of  is not equal to .
x = int ( raw_input()) y = int ( raw_input()) n = int ( raw_input())


print ([ [ i, j, k] for i in range( x + 1) for j in range( y + 1) for k in range (z+1) if ( ( i + j +z ) != n )])


#13. Swap cASE. You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.


def swap_case(s):
     s=list(s)
     for i in range (len(s)):
             if s[i].isupper():
                     s[i]=s[i].lower()
             else:
                     s[i]=s[i].upper()
     return ("".join(s))
             else:
                     s[i]=s[i].upper()
    return ("".join(s))

    return

#14

from string import ascii_lowercase
n=5
hyphen = list("-" * ((n -1) *4))
first_part=range(n)
output=""
j=0
for i in reversed(first_part):
     line= hyphen
     line[n+2]=ascii_lowercase[i]
     line[n+3]=ascii_lowercase[n-1]
     output=output+("".join(line)+"\n")

for i in reversed(first_part):
	line= hyphen
	line[n+2]=ascii_lowercase[i]
	flag=True
	while (j in (first_part)) & ((i+1)<n):
		line[n+i]=ascii_lowercase[i+1]
		line[n+i+1]=ascii_lowercase[(i)]
		line[n+i+2]=ascii_lowercase[(i-1)]
		line[n+i+3]=ascii_lowercase[(i)]

	output=output+("".join(line)+"\n")


	for j in output:
	if n> (i+1):
	line[n+i]=ascii_lowercase[i]
		#line[n-i+1]=ascii_lowercase[(i+1)]
		#line[n+i+4]=line[n-i+1]

#15sum of 2 numbers of the list =target
def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup={}
        for index, element in enumerate(nums):
            if (lookup.get(element) != None):
                return [lookup[element],index]
            else:
                lookup[(target-element)] = index
        return []
