class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def isPalindrome(s):
            return s==s[::-1]
    
        def backtrack(start, sol):
            if start == len(s):
                result.append(sol)
            for end in range(start+1, len(s)+1):
                if isPalindrome(s[start:end]):
                    backtrack(end, sol + [s[start:end]])
        
        result = []
        backtrack(0, [])
        return result
