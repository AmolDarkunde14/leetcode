# reverse Integer
class Solution:

    def reverseinteger(self, number):
        new_num = ""

        for num in str(number):
            new_num = num + new_num
            
        return new_num

obj = Solution()
print(obj.reverseinteger(123))