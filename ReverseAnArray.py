class Solution:
    def reverseArray(self, arr):
        # code here
        for i in range(len(arr)//2):
            arr[i],arr[len(arr)-1-i]=arr[len(arr)-1-i],arr[i]
            
