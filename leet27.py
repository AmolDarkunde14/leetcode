# remove element

class solution:
    def remove(self, nums, val):

        k = 0
        for i in range(len(nums)):
            if(nums[i] != val):
                nums[k] = nums[i]
                k += 1
            
        return k
    
obj = solution()
nums = [1,2,3,4,5,6,7]
print(obj.remove(nums,5))
