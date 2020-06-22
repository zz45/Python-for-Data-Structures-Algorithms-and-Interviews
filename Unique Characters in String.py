# -*- coding: utf-8 -*-


'''
Problem
Given a string,determine if it is compreised of all unique characters. 
For example, the string 'abcde' has all unique characters and should return True.
 The string 'aabcde' contains duplicate characters and should return false.
'''
# My answer
def uni_char(s):
    # Need to count for how many letter in the whole string
    # Need to get the unique letters in one string
    unique_letters = sorted(''.join(set(s)))
    # This method count the letters
    for i in unique_letters:
        count = s.count(i)
        if count > 1:
            return False
    return True

# I consider as count number while Jose considers if it exists in one set
         
# Jose's answer for this 
# One line solution for this
def uni_char2(s):
    return len(set(s)) == len(s)
    pass

# Another solution for Jose's 
def uni_char(s):
    u = set()
    for c in s:
        if c in u:
            return False
        else:
            u.add(c)
    return True
    pass

# Testing 
from nose.tools import assert_equal


class TestUnique(object):

    def test(self, sol):
        assert_equal(sol(''), True)
        assert_equal(sol('goo'), False)
        assert_equal(sol('abcdefg'), True)
        print ('ALL TEST CASES PASSED')
        
# Run Tests
t = TestUnique()
t.test(uni_char)