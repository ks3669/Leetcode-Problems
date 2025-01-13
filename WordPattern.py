class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_arr = list(pattern)
        s_arr = []
        pattern_s = {}
        s_pattern = {}
        temp_string = ""
        for i in range(len(s)):
            if s[i] == " ":
                s_arr.append(temp_string)
                temp_string = ""
            else:
                temp_string += s[i]
        s_arr.append(temp_string)

        if len(pattern_arr) != len(s_arr):
            return False
        
        for i in range(len(pattern_arr)):
            if pattern_arr[i] in pattern_s:
                if pattern_s.get(pattern_arr[i]) != s_arr[i]:
                    return False
            pattern_s[pattern_arr[i]] = s_arr[i]

            if s_arr[i] in s_pattern:
                if s_pattern.get(s_arr[i]) != pattern_arr[i]:
                    return False
            s_pattern[s_arr[i]] = pattern_arr[i]

        return True
