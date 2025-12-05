# Palindrome number

class soluiton:
    def palindrome(self, number):

        n = str(number)
        new_num = ""

        for num in n:
            new_num = num + new_num

        if(new_num == n):
            print("its a palindrome")
        else:
            print("its not a palindrome")
        
        return new_num

obj = soluiton()
print(obj.palindrome(121))