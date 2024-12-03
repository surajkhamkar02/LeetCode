class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Using Two Pointers
        # Time O(n)
        # Space O(1)
        left, right = 0, len(s) - 1
        
        while left < right:
            # Skip non-alphanumeric characters
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Compare characters case-insensitively
            if s[left].lower() != s[right].lower():
                return False
            
            # Move pointers inward
            left += 1
            right -= 1
        
        return True
