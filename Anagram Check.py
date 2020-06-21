# -*- coding: utf-8 -*-


# Check whether it is anagram 
def anagram(s, t):
    if type(s) != type(t):
        return False 
    else:
        # Create a list
        s_list = [i.lower() for i in s if i !=' ']
        t_list = [i.lower() for i in t if i !=' ']
        if len(s_list) != len(t_list):
            return False
        else:
            s_list.sort()
            t_list.sort()
            for i in range(0, len(s_list) - 1): 
                if (s_list[i] != t_list[i]): 
                    return False
                else:
                    return True
        
        # Then remove spaces 
        
    
anagram('aabbcc','aabbc')
anagram('clint eastwood','old west action')
anagram('aa','bb')

# Here is the testing part

from nose.tools import assert_equal

class AnagramTest(object):
    
    def test(self,sol):
        assert_equal(sol('go go go','gggooo'),True)
        assert_equal(sol('abc','cba'),True)
        assert_equal(sol('hi man','hi     man'),True)
        assert_equal(sol('aabbcc','aabbc'),False)
        assert_equal(sol('123','1 2'),False)
        print('ALL TEST CASES PASSED')

# Run Tests
t = AnagramTest()
t.test(anagram)


