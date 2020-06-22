# -*- coding: utf-8 -*-


# Array Pair Sum
'''
Problem
Given an array of integers (positive and negative) find the largest continuous sum.

Solution
Fill out your solution below:
'''
# My answer
def large_cont_sum(arr):
    # continue to add and compare the sum
    add = 0
    maximum = 0
    for i in arr:
        if add > add + i and maximum < add: # can use max function instead
            maximum = add
            add += i
        else:
            add += i
    if maximum < sum(arr):
        return sum(arr)
    else:
        return maximum
         
# Jose's answer for this 

def large_cont_sum(arr):
    if len(arr) == 0:
        return 0
    
    max_num = sum = arr[0]# max=sum=arr[0] bug: TypeError: 'int' object is not callable. (Do not use the keyword!)
    
    for n in arr[1:]:
        sum = max(sum+n, n)
        max_num = max(sum, max_num)
    return max_num
    pass

large_cont_sum([-1,1])

# Testing 
from nose.tools import assert_equal

class LargeContTest(object):
    def test(self,sol):
        assert_equal(sol([1,2,-1,3,4,-1]),9)
        assert_equal(sol([1,2,-1,3,4,10,10,-10,-1]),29)
        assert_equal(sol([-1,1]),1)
        print ('ALL TEST CASES PASSED')
        
#Run Test
t = LargeContTest()
t.test(large_cont_sum)

