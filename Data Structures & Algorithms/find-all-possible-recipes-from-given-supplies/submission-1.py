class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = {}
        for recipe, ingredient in zip(recipes, ingredients):
            graph[recipe] = ingredient
        supply = set(supplies)
        ans = []
        visited = set()
        base = set()

        def canMake(recipe):
            if (recipe not in supply) and (recipe not in graph):
                return False
            visited.add(recipe)
            if recipe in graph:
                for ingre in graph[recipe]:
                    if ingre in visited:
                        return False
                    canMakeBool = canMake(ingre)
                    if canMakeBool == False:
                        return False
                    else:
                        base.add(ingre)
            visited.remove(recipe)
            return True

        for recipe in recipes:
            if recipe in base:
                ans.append(recipe)
            elif canMake(recipe) == True:
                ans.append(recipe)
        return ans