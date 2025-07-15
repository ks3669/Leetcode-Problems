class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in s_dict:
                s_dict[s[i]] += 1
            else:
                s_dict[s[i]] = 1
            if t[i] in t_dict:
                t_dict[t[i]] += 1
            else:
                t_dict[t[i]] = 1
        try:
            for key in s_dict:
                if s_dict[key] == t_dict[key]:
                    continue
                else:
                    return False   
            return True
        except KeyError:
            return False
#just wanted to do something different so used a try except block for this simple problem.
