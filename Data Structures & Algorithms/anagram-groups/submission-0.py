class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        di=defaultdict(list)
        for i in strs:
            ke=[0]*26
            for j in tuple(i):
                ke[ord(j)-97]+=1
            di[tuple(ke)].append(i)
        return list(di.values())
