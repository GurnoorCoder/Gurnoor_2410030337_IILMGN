class Solution:
    def kthSmallest(self, arr, k):
        def quickselect(left, right, k_index):
            if left == right:
                return arr[left]
            
            # Partition the array
            pivot_index = partition(left, right)
            
            # Check if pivot is the kth element
            if k_index == pivot_index:
                return arr[k_index]
            elif k_index < pivot_index:
                return quickselect(left, pivot_index - 1, k_index)
            else:
                return quickselect(pivot_index + 1, right, k_index)
        
        def partition(left, right):
            pivot = arr[right]
            i = left
            
            for j in range(left, right):
                if arr[j] <= pivot:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
            
            arr[i], arr[right] = arr[right], arr[i]
            return i
        
        return quickselect(0, len(arr) - 1, k - 1)
