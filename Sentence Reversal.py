# -*- coding: utf-8 -*-


'''
Given a string of words, reverse all the words. For example:

Given:

'This is the best'

Return:

'best the is This'

As part of this exercise you should remove all leading and trailing whitespace. So that inputs such as:

'  space here'  and 'space here      '

both become:

'here space'
'''
# My answer
def rev_word(s):
    word_list = s.split()
    word_list.reverse()
    # get the reversed list into a string
    rev_String = ' '.join(word_list)
    return rev_String

         
# Jose's answer for this 
# The same

# Testing 
from nose.tools import assert_equal

class ReversalTest(object):
    
    def test(self,sol):
        assert_equal(sol('    space before'),'before space')
        assert_equal(sol('space after     '),'after space')
        assert_equal(sol('   Hello John    how are you   '),'you are how John Hello')
        assert_equal(sol('1'),'1')
        print ("ALL TEST CASES PASSED")
        
# Run and test
t = ReversalTest()
t.test(rev_word)