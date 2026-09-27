class Solution:
    
    def encode(self, strs: List[str]) -> str:
        en=''
        for i in strs:
            en += str(len(i))+'@'+i
        return en
    def decode(self, s: str) -> List[str]:
        j=0
        l=[]
        while(j<len(s)):
            i=s.find('@',j)
            po=i+1
            count=int(s[j:i])
            st=s[po:po+count]
            l.append(st)
            j=po+count
        return l