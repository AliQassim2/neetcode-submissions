class Solution:
    
    def encode(self, strs: List[str]) -> str:
        en=''
        for i in strs:
            en += str(len(i))+'@'+i
        return en
    def decode(self, s: str) -> List[str]:
        count=i=j=0
        l=[]
        c=''
        while(j<len(s)):
            c=''
            while(s[j]!='@'):
                c+=s[j]
                j+=1
            count=int(c)
            j+=1
            st=s[j:j+count]
            l.append(st)
            j+=count
        return l