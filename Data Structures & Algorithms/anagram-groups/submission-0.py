class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for stri in strs:
            anagrams[''.join(sorted(stri))].append(stri)
        ans = []
        for val in anagrams.values():
            ans.append(val)
        return ans