# Remove Duplicates from Sorted Array

class solution:
    def removeduplicates(self, nums):

        i = 2

        for j in range(2, len(nums)):
            if(nums[i - 2] != nums[j]):
                nums[i] = nums[j]
                i += 1
        
        return i
    
obj = solution()
nums = [0,0,0,1,1,1,2,3,3]
print(obj.removeduplicates(nums))
print(nums[:7])