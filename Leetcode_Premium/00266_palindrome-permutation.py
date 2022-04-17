# Description
# Given a string, determine if a permutation of the string could form a palindrome.

# Example
# Example1

# Input: s = "code"
# Output: False
# Explanation: 
# No solution
# Example2

# Input: s = "aab"
# Output: True
# Explanation: 
# "aab" --> "aba"
# Example3

# Input: s = "carerac"
# Output: True
# Explanation: 
# "carerac" --> "carerac"

class Solution:
    def can_permute_palindrome(self, s: str) -> bool:
        st = set()
        for c in s:
            if c in st:
                st.remove(c)
            else:
                st.add(c)
        if len(st) <= 1:
            return True
        return False
