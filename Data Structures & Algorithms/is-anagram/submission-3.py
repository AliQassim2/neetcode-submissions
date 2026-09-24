class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        di=defaultdict(int)
 
        
        for i in range(len(t)) :
            di[s[i]] += 1
            di[t[i]] -= 1
        return not any(di.values())
        