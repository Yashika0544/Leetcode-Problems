class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        '''m=0
        for i in range(len(citations)):
            if citations[i]>len(citations)-1:
                m=max(m,len(citations)-1)
        return m
        '''
        m=len(citations)
        for i in citations:
            if i<m:
                m-=1
        return m
