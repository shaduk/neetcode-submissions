class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        visited = set()
        trace = set()
        for node in prerequisites:
            graph[node[0]].append(node[1])

        def topologicalSort(i):
            if i in trace:
                return False
            visited.add(i)
            trace.add(i)
            for neighbor in graph[i]:
                if neighbor not in visited:
                    result = topologicalSort(neighbor)
                    if (result == False):
                        return False
                elif neighbor in trace:
                    return False
            trace.remove(i)

        for course in range(0, numCourses):
            if course not in visited:
                result = topologicalSort(course)
                if result == False:
                    return False
        return True