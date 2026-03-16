from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        groups = defaultdict(list)

        for word in strs:
            count = [0] * 26
            
            for c in word:
                count[ord(c) - ord('a')] += 1
            
            groups[tuple(count)].append(word)

        return groups.values()