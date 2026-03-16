class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hmap = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in hmap:
                hmap[key] = []

            hmap[key].append(word)

        return list(hmap.values())