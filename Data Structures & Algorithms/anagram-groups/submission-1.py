class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for stri in strs:
            anagrams[''.join(sorted(stri))].append(stri)
        
        return list(anagrams.values())