class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Returns the longest palindromic substring in the given string `s`.
        Uses the 'Expand Around Center' approach with O(n^2) time complexity.
        """
        
        # If the string is very short, it's already a palindrome of itself
        if len(s) < 2:
            return s
        
        def expand_around_center(left: int, right: int) -> str:
            """
            Expands around the center indices (left, right) while characters are equal
            and returns the palindrome substring found.
            """
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            # when the loop ends, (left, right) are one step beyond the palindrome boundaries
            return s[left + 1 : right]
        
        longest_palindrome = ""
        
        for i in range(len(s)):
            # Check for odd-length palindrome (centered at i)
            odd_pal = expand_around_center(i, i)
            # Check for even-length palindrome (center between i and i+1)
            even_pal = expand_around_center(i, i + 1)
            
            # Update the longest palindrome if we find a bigger one
            if len(odd_pal) > len(longest_palindrome):
                longest_palindrome = odd_pal
            if len(even_pal) > len(longest_palindrome):
                longest_palindrome = even_pal
        
        return longest_palindrome
