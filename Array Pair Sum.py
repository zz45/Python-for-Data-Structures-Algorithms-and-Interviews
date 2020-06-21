# -*- coding: utf-8 -*-


# Array Pair Sum
'''
Problem
Given an integer array, output all the unique pairs that sum up to a specific value k.

So the input:

pair_sum([1,3,2,2],4)

would return 2 pairs:

 (1,3)
 (2,2)

NOTE: FOR TESTING PURPOSES CHANGE YOUR FUNCTION SO IT OUTPUTS THE NUMBER OF PAIRS
'''

def pair_sum(s,r):
    # Give all the possible pair of result in that list array to test if it is equal to the r
    result =set()
    count = 0
    for i in range(0,len(s)+1):
        for z in range(1,(len(s)-i)):
            print((s[i],s[i+z]))
            if s[i] + s[i+z] == r:
                result.add((s[i],s[i+z]))
                count += 1
    return count

# Jose's answer to check if it is in lookup
def pair_sum(arr,k):
    counter = 0
    lookup = set()
    for num in arr:
        if k-num in lookup:
            counter+=1
        else:
            lookup.add(num)
    return counter
    pass


from nose.tools import assert_equal

class TestPair(object):
    
    def test(self,sol):
        assert_equal(sol([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10),6)
        #assert_equal(sol([1,2,3,1],3),1)
        assert_equal(sol([1,3,2,2],4),2)
        print('ALL TEST CASES PASSED')
        
#Run tests
t = TestPair()
t.test(pair_sum)
    

