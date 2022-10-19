class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = []
        s = s.lower()
        for ele in s:
            if(ele.isalnum()):
                temp.append(ele)
        print(temp)
        left,right = 0,len(temp) - 1
        while(left <= right):
            if(temp[left] != temp[right]):
                return False
            left = left + 1
            right = right - 1
        return True