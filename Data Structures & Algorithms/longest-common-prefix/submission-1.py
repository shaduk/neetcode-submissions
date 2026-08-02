class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        for i in range(len(strs[0])):
            for stri in strs:
                if i == len(stri) or strs[0][i] != stri[i]:
                    return res
            res += stri[i]
        return res