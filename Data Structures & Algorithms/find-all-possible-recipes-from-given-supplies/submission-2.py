class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supply = set(supplies)
        graph = {recipes[i]: ingredients[i] for i in range(len(recipes))}
        set_recipes = set(recipes)

        memo = {}       # recipe -> True / False (final answer)
        visiting = set()  # current DFS path (for cycle detection)

        def canMake(recipe):
            if recipe in supply:
                return True
            if recipe in memo:
                return memo[recipe]
            if recipe in visiting:        # cycle on current path
                return False
            if recipe not in graph:       # not a recipe and not a supply
                return False

            visiting.add(recipe)
            ok = True
            for ingre in graph[recipe]:
                if not canMake(ingre):
                    ok = False
                    break
            visiting.discard(recipe)      # always clean up, even on failure

            memo[recipe] = ok
            return ok

        ans = []
        for recipe in recipes:
            if canMake(recipe):
                ans.append(recipe)
        return ans