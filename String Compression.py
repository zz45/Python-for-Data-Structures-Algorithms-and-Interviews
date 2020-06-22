# -*- coding: utf-8 -*-


'''
Problem
Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'.
 For this problem, you can falsely "compress" strings of single or double letters. 
 For instance, it is okay for 'AAB' to return 'A2B1' even though this technically takes more space.

The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.
'''
# My answer
def compress(s):
    # Need to count for how many letter in the whole string
    # Need to get the unique letters in one string
    string = ''
    unique_letters = sorted(''.join(set(s)))
    # This method count the letters
    for i in unique_letters:
        count = s.count(i)
        string += i + str(count)
    return string
         
# Jose's answer for this 
def compress(s):
    r = ""
    l = len(s)
    
    if l==0:
        return ''
    if l==1:
        return s+'1'
    
    last = s[0]
    cnt = 1
    i=1
    
    while i<l:
        if s[i]==s[i-1]:
            cnt += 1
        else:
            r=r+s[i-1]+str(cnt)
            cnt=1
        i+=1
    r = r+s[i-1]+str(cnt)
    return r
    pass

# Testing 
from nose.tools import assert_equal


class TestCompress(object):

    def test(self, sol):
        assert_equal(sol(''), '')
        assert_equal(sol('AABBCC'), 'A2B2C2')
        assert_equal(sol('AAABCCDDDDD'), 'A3B1C2D5')
        print ('ALL TEST CASES PASSED')

# Run Tests
t = TestCompress()
t.test(compress)