
# Link - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

# Space: 
# Time: O(n + m + E) :-> n = len(recipes), m = len(supplies), E = sum(len(ing) for ing in ingredients)

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        supplies = set(supplies)
        
        dependents, num_of_reqs = defaultdict(set), defaultdict(int)
        for i, recipe in enumerate(recipes):
            for ingredient in ingredients[i]:
                if ingredient not in supplies:
                    dependents[ingredient].add(recipe)
                    num_of_reqs[recipe] += 1
        
        answer, q = set(), deque()
        for i, recipe in enumerate(recipes):
            if num_of_reqs[recipe] == 0 and recipe not in answer:
                q.append(recipe)
                while q:
                    can_be_created = q.popleft()
                    answer.add(can_be_created)
                    for dependent in dependents[can_be_created]:
                        num_of_reqs[dependent] -= 1
                        if num_of_reqs[dependent] == 0:
                            q.append(dependent)
        
        return list(answer)