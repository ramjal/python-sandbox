class Solution:
  def lengthOfLongestSubstring(self, s):
    myList = []
    longest = 0
    theLongList = []
    for char in s:
        if char in myList:
            if longest < len(myList):
                longest = len(myList)
                theLongList = myList
            myList = []
            continue
        myList.append(char)
    if longest < len(myList):
        longest = len(myList)
    print(''.join(theLongList))
    return longest


print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10