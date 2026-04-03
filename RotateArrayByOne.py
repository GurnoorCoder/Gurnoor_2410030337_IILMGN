class Solution:
    def rotate(self, arr):
        number=[]
        a=arr.pop()
        number.append(a)
        arr.insert(0,number[0])
        return number
