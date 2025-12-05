# Remove Duplicates from Sorted Array

class solution:
    def removeduplicate(self, arr):

        if not arr:
            return 0
        
        i = 0 # points to the unique number

        for j in range(1, len(arr)):
            if(arr[i] != arr[j]):
                i += 1
                arr[i] = arr[j]

        return i + 1
    
obj = solution()
arr = [1,1,1,2,3,3,4,4]
print(obj.removeduplicate(arr))
print(arr[:4])
