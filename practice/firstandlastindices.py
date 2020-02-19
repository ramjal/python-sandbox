"""
Input: A = [1,3,3,5,7,8,9,9,9,15], target = 9
Output: [6,8]

Input: A = [100, 150, 150, 153], target = 150
Output: [1,2]

Input: A = [1,2,3,4,5,6,10], target = 9
Output: [-1, -1]
Here is a function signature example:

"""

class Solution: 
    def getRange(self, arr, target):
        ret = []
        index = 0
        for value in arr:            
            if value == target:
                if len(ret) < 2:
                    ret.append(index)
                else:
                    ret[1] = index
            index += 1
        return ret

        
  


# Test program 
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 2
print(Solution().getRange(arr, x))
# [1, 4]