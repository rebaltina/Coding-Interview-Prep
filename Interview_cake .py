#Problem 2,InterviewCake. Given an array arr[] of n integers, construct a Product Array prod[] (of same size) such that
#prod[i] is equal to the product of all the elements of arr[] except arr[i]. Solve it without division operator and in O(n).

arr=[2,4,-3,6,2,7]
def product(ar):
    n=len(ar)
    result = 1
    for i in range(0, n):
    result = result * ar[i]
    return result

def Product_Arr(arr, i):
    left=arr[:i]
    right=arr[(i+1):]
    return product(left)*product(right)

#Given an integer array nums, find the contiguous subarray within an array (containing at least one number)
#which has the largest product.

arr=[2,3,-2]
# first let's build the subarrays
# Python program to find maximum product subarray


#then let's make the product
test


#It's every caracters in the string unique?Cracking coding interview 1
s="abrodi"
def Is_Unique(s):
    sets=([i for i in s])
    return len(sets)==len(s)
#or
def Is_Unique(s):
    sets=set()
    for i in s:
    if i in sets:
    return False
    else:
    sets.add(i)
    return True


#Write a function that, given:#an amount of money
#an array of coin denominations
#computes the number of ways to make amount of money with coins of the available denominations.
money=4
coins=[1,2,3]


# Recursive Python3 program for
# coin change problem.


    # If n is less than 0 then no
    # solution exists
    if (n < 0):
        print('b')
        return 0;

    # If there are no coins and n
    # is greater than 0, then no
    # solution exist
    if (m <=0 and n >= 1):
        print('c')
        return 0

    # count is sum of solutions (i)
    # including S[m-1] (ii) excluding S[m-1]
    print('d')
    return count( S, m - 1, n ) + count( S, m, n-S[m-1] )

# Driver program to test above function
arr = [1, 2, 3]
m = len(arr)
print(count(arr, m, 4))
