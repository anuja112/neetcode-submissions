class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ns=set(nums)
        m=0
        for n in ns:
            if n-1 not in ns:
                l=1
                while n+l in ns:
                    l+=1
                m=max(m,l)
        return m