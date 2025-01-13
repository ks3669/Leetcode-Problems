class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # If lengths differ, they cannot be isomorphic
        if len(s) != len(t):
            return False

        # Two dictionaries to maintain the mapping in both directions
        map_s2t = {}
        map_t2s = {}

        for i in range(len(s)):
            c1, c2 = s[i], t[i]

            # If there's a stored mapping for c1 but it doesn't match c2, fail
            if c1 in map_s2t and map_s2t[c1] != c2:
                return False

            # If there's a stored mapping for c2 but it doesn't match c1, fail
            if c2 in map_t2s and map_t2s[c2] != c1:
                return False

            # Store the mapping in both dictionaries
            map_s2t[c1] = c2
            map_t2s[c2] = c1

        # If we never found a mismatch, it's isomorphic
        return True
