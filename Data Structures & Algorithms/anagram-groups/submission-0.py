class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)==0 or len(strs)==1:
            return [strs]
        d={}
        for str in strs:
            c=[0]*26
            for i in str:
                c[ord(i)-ord('a')]+=1
            key=tuple(c)
            if key not in d:
                d[key]=[]
            d[key].append(str)
        return list(d.values())