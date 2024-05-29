class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        num = 0
        j = 0
        for i in range(len(s)):
            if s[i]>=g[j]:
                num = num + 1
                j = j + 1
            if j == len(g):
                break
        return num