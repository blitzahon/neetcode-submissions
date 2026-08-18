class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = [c for c in s if c.isalnum()]
        c = ''.join(cleaned).lower()
        
        if c == c[::-1]:
            return True
        else:
            return False
        