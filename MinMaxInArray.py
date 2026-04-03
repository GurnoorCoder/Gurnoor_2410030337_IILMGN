class Solution:
    def getMinMax(self, arr):
        # code here
        min_val=arr[0]
        max_val=arr[0]
        
        for i in range(len(arr)):
            if(arr[i]<min_val):
                min_val=arr[i]
            if(arr[i]>max_val):
                max_val=arr[i]
        
        return min_val,max_val
