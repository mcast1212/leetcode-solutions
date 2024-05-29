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
        for j in range(len(s)):
            for i in range(len(g)):
                if s[j]>=g[i]:
                    num = num + 1
                    break
        return num
