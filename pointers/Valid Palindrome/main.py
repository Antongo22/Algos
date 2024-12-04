from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        pointer_start = 0
        pointer_end = len(s) - 1
                       
        while pointer_start <= pointer_end:
            if not s[pointer_start].isalnum():
                pointer_start += 1
                continue
            if not s[pointer_end].isalnum():
                pointer_end -= 1
                continue
        
            if s[pointer_start].lower() == s[pointer_end].lower():
                pointer_start += 1
                pointer_end -= 1 
            else:
                return False
        
        return True         