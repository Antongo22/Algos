class Solution:
    """
    @param s: the given string
    @return: if a permutation of the string could form a palindrome
    """
    def can_permute_palindrome(self, s: str) -> bool:
        arr = [0 for _ in range(26)]

        for c in s:
            arr[ord(c) - ord("a")] += 1

        co = 0
        for c in arr:
            if c % 2 == 1:
                co+=1
            if co >= 2:
                return False

        return True

