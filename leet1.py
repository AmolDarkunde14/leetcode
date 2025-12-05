# two sum problem

def two_sum(nums, target):
    left = 0
    right = len(nums) - 1

    while(left < right):
        curr_sum = nums[left] + nums[right]

        if(curr_sum == target):
            return left,right
        elif(curr_sum < target):
            left += 1
        else:
            right -= 1
        
nums = [2,4,6,7,8,9]
target = 6
print(two_sum(nums,target))
        

        






