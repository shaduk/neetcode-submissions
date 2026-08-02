class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        ans = []
        def recurse(i, combination):
            if i > n:
                if len(combination) == k:
                    ans.append(combination[:])
                return
            combination.append(i)
            recurse(i+1 , combination)
            combination.pop()
            recurse(i+1, combination)

        recurse(1, [])
        return ans



    