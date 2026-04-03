class Solution:    
    def findUnion(self, a, b):
        union_set=set(a+b)
        return sorted(union_set)
