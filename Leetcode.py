#But for multiples of three it should output �Fizz� instead
#of the number and for the multiples of five output �Buzz�.
#For numbers which are multiples of both three and five
#output �FizzBuzz�.
def FizzBuzz(n):
  for i in range(n+1):
    if i%3==0:
      print("Fizz")
    if i%5==0:
      print("Buzz")
    if i%5==0 and i%3==0:
      print("FizzBuzz")
    else:
      print(i)
#this is faster
      class Solution:
      def fizzBuzz(self, n: 'int') :
      ans=[]
      for num in range(n+1) :
      divisible_by_3 = (num % 3 == 0)
      divisible_by_5 = (num % 5 == 0)

      if divisible_by_3 and divisible_by_5:
      # Divides by both 3 and 5, add FizzBuzz
      ans.append("FizzBuzz")
      elif divisible_by_3:
      # Divides by 3, add Fizz
      ans.append("Fizz")
      elif divisible_by_5:
      # Divides by 5, add Buzz
      ans.append("Buzz")
      else:
      # Not divisible by 3 or 5, add the number
      ans.append(str(num))
      return ans
      #common prefix in list of words
      words=['flower', 'flour','flexible']

      for index, word in enumerate (words):
        for i in range(len(word)):
          word_i=word[i]
          x=''
          if word[i+1]!=word_i:
            print( x)
          else:
          x=x+word[i]
        return x

            x=x+word[i]
            i=i+1
      return x

      def longestCommonPrefix(strs):
          if not strs:
          return ''
          first_word = strs[0]
          for i in range(len(first_word)):
          for j in range(1,len(strs)):
          if i >= len(strs[j]): # first_word larger than current_word
          return first_word[:i]
          if strs[j][i] != first_word[i]: # letters don't equal
          return first_word[:i]

      # Returns the product of max product subarray.
      # Assumes that the given array always has a subarray
      # with product more than 1
      def maxsubarrayproduct(arr):

          n = len(arr)

          # max positive product ending at the current position
          max_ending_here = 1

          # min positive product ending at the current position
          min_ending_here = 1

          # Initialize maximum so far
          max_so_far = 1

          # Traverse throughout the array. Following values
          # are maintained after the ith iteration:
          # max_ending_here is always 1 or some positive product
          # ending with arr[i]
          # min_ending_here is always 1 or some negative product
          # ending with arr[i]
          for i in range(0,n):

          # If this element is positive, update max_ending_here.
          # Update min_ending_here only if min_ending_here is
          # negative
          if arr[i] > 0:
          max_ending_here = max_ending_here*arr[i]
          min_ending_here = min (min_ending_here * arr[i], 1)

          # If this element is 0, then the maximum product cannot
          # end here, make both max_ending_here and min_ending_here 0
          # Assumption: Output is alway greater than or equal to 1.
          elif arr[i] == 0:
          max_ending_here = 1
          min_ending_here = 1

          # If element is negative. This is tricky
          # max_ending_here can either be 1 or positive.
          # min_ending_here can either be 1 or negative.
          # next min_ending_here will always be prev.
          # max_ending_here * arr[i]
          # next max_ending_here will be 1 if prev
          # min_ending_here is 1, otherwise
          # next max_ending_here will be prev min_ending_here * arr[i]
          else:
          temp = max_ending_here
          max_ending_here = max (min_ending_here * arr[i], 1)
          min_ending_here = temp * arr[i]
          if (max_so_far < max_ending_here):
          max_so_far = max_ending_here
          return max_so_far

      # Driver function to test above function
      arr = [1, -2, -3, 0, 7, -8, -2]
      print "Maximum product subarray is",maxsubarrayproduct(arr)

      # This code is contributed by Devesh Agrawal
      h
      ls=[]
      def maxProduct(nums):
        if len(nums)>1:
          prod=nums[len(nums)-1]
          for ind in reversed(range (len(nums))):
          prod=nums[ind]*prod
          res=max(max(nums), prod)
          maxProduct(nums.pop())
        else:
          res=nums[0]
        return res

##RECURSIONS
##Write a program that outputs the string representation
#of numbers from 1 to n.

def getMinSquares(n):

    # base cases
    if n <= 3:
    return n;

    # getMinSquares rest of the table
    # using recursive formula
    res = n # Maximum squares required
    # is n (1*1 + 1*1 + ..)

    # Go through all smaller numbers
    # to recursively find minimum
    for x in range(1, n+1):
    temp = x * x;

    if temp > n:
    break
    else:
    res = min(res, 1 + getMinSquares(n
      - temp))

    return res;

#oivot to quicksort
A=[2,4,5,6,1]
n=1
B=[]
C=[]
def quicksort (A, n):
  p=A[n]
  for j in A:
    if j < p:
      B.append(j)
    else:
      C.append(j)
  return B+C
quicksort (A, n)

#merge and sort
A=[2,4,5,6,1]
B=[3, 7]
def sort (A,B):
  a=A+B
  for j in range(len(a)-1):
    for l in range((j+1),len(a)):
      if a[j]>a[l]:
    a[j], a[l] = a[l], a[j]
  return a
sort (A,B)

 def reversing(n):
   rev=0
   while n>rev:
     rev=rev*10+n%10
     n=round(n/10)
   return rev

 def ispal(n):
   rev=0
   while n>=rev:
     rev=rev*10 + round(n)%10
     n=n//10
   print(n,rev)
   if n==rev or n==rev//10:
     return True
   else:
     return False


   if n!=rev:
     return False
   return True
   for i in range(m//2):
     if s[i] != s[m-i-1]:
   return False
   return True


def reverse(m):
 return m[::-1]
def palindrome(n):
 m=str(n)
 return m==reverse(m)
