'''
Leetcode 49. Group Anagrams
So basically my first thought was to compute and compare the ASCII values of each character
and in that way if the sum in same then it will be a anagram.But later when I explored 
different scenarios then I found out mistake. For example this method wont work for repeating consecutive letters like "aaa", or even "aab"
So my next thought was to have some kind of a mapping for each character and if it is consistent then we can for sure tell that it is an anagram.
So I implimented the same logic with dictionaries in python.

Time Complexity - O(n)
Space Complexity - O(n * k) where 'n' is the number of strings in the list and 'k' is the length of each string
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary to map a character-count key to a list of anagrams
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Create a frequency array for 26 lowercase English letters
            count = [0] * 26
            
            for char in s:
                count[ord(char) - ord('a')] += 1
                
            # Convert the list to a tuple so it can be used as a dictionary key
            key = tuple(count)
            anagram_map[key].append(s)
        
        # Return all grouped anagrams
        return list(anagram_map.values()) 
