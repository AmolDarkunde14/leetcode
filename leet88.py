class solution:
    def merge(arr1,m,arr2,n):
        i = m - 1
        j = n - 1
        k = m + n -1

        while(j>=0):
            if(i>=0 and arr1[i] > arr2[j]):
                arr1[k] = arr1[i]
                k -= 1
                i -= 1
            else:
                arr1[k] = arr2[j]
                k -= 1
                j -= 1
        
        return arr1
    
obj = solution()
arr1 = [1,2,3,0,0,0]
arr2 = [2,5,6]


