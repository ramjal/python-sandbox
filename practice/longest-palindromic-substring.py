"""
A palindrome is a sequence of characters that reads the same backwards and forwards. Given a string, s, find the longest palindromic substring in s.

Example:
Input: "banana"
Output: "anana"

Input: "million"
Output: "illi"

"""

class Solution: 
    def isPalindorme(self, s):
        if len(s) == 0 or len(s) == 1:
            return True
        elif s[0] == s[-1]:
            return self.isPalindorme(s[1:-1]) #remove head and tail characters
        else:
            return False

    def longestPalindrome(self, s):
        longest = 0
        longestStr = ""
        for i in range(0, len(s)):
            for j in range(i+1, len(s)+1):
                if self.isPalindorme(s[i:j]):
                    if (len(s[i:j]) > longest):
                        longestStr = s[i:j]
                        longest = len(longestStr)
        return longestStr

        #print(self.isPalindorme("anana"))
        #print(self.isPalindorme("ramin"))
        

# Test program
s = "tracecars"
print(str(Solution().longestPalindrome(s)))
# racecar
s = "million"
print(str(Solution().longestPalindrome(s)))
s = "banana"
print(str(Solution().longestPalindrome(s)))


