class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        di=defaultdict(int)
        sis=len(s)
        sit=len(t)
        if sis != sit:
            return False
        for i in range(sis) :
            di[s[i]] += 1
            di[t[i]] -= 1
        return not any(di.values())
        