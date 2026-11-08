class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for crs, pre in prerequisites:
            graph[crs].append(pre)

        visited = set()
        trace = set()

        def dfs(i):
            if i in trace:
                return False
            if i in visited:
                return True
            visited.add(i)
            trace.add(i)
            for neighbor in graph[i]:
                if not dfs(neighbor):
                    return False
            trace.remove(i)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True