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
