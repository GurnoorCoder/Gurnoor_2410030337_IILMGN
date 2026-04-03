class Solution:
    def maxSubarraySum(self, arr):
        # Code here
        max_sum=float('-inf')
        sum=0
        for i in arr:
            sum+=i
            max_sum=max(max_sum,sum)
            
            if(sum<0):
                sum=0
                
        return max_sum
