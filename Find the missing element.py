# -*- coding: utf-8 -*-


# Array Pair Sum
'''
Problem
Consider an array of non-negative integers. A second array is formed by 
shuffling the elements of the first array and deleting a random element. 
Given these two arrays, find which element is missing in the second array.

Here is an example input, the first array is shuffled and 
the number 5 is removed to construct the second array.

Input:

finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])

Output:

5 is the missing number
'''
# My answer
def finder(arr1,arr2):
    # sort the number to compare arr1 with arr2
    arr1_list = sorted(arr1)
    arr2_list = sorted(arr2)
    for i in range(0, len(arr1_list)):
        if arr1_list[i] != arr2_list[i]:
            break
    return arr1_list[i]

# Jose's answer for this 
def finder(arr1,arr2):
    num = 0
    for n in arr1:
        num += n
    for n in arr2:
        num -= n
    return num
    pass

from nose.tools import assert_equal

class TestFinder(object):
    
    def test(self,sol):
        assert_equal(sol([5,5,7,7],[5,7,7]),5)
        assert_equal(sol([1,2,3,4,5,6,7],[3,7,2,1,4,6]),5)
        assert_equal(sol([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]),6)
        print('ALL TEST CASES PASSED')

# Run test
t = TestFinder()
t.test(finder)
    

