class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # Convert the dictionary list into a set for O(1) lookup time
        root_set = set(dictionary)

        # Helper function to find the shortest root for a word
        def find_root(word: str) -> str:
            # Iterate through increasing prefixes of the word
            for i in range(1, len(word) + 1):
                prefix = word[:i]
                # If prefix exists in the root set, return it as replacement
                if prefix in root_set:
                    return prefix
            # If no root is found, return the original word
            return word

        # Split sentence into words and replace each word with its shortest root
        return " ".join(find_root(word) for word in sentence.split())
