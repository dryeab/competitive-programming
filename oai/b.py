def solution(n: int, m: int, k) -> bool:
    # write your solution here
    
    """  Approach #1
    
    With this approach, we aim to determine if each player has played against every other player.
    If every player has indeed played against all other players, then the number of opponents 
    for each player would be n - 1, where n is the total number of players. To verify this, 
    we create an array called opponents with a length of n + 1 to accommodate accessing the nth index.

    Each element in the opponents array represents a player and contains a set of distinct opponents 
    that the player has played against. Storing opponents as a set ensures that we only keep track of 
    unique opponents, even if a player plays against the same opponent multiple times.

    To check if each player has n - 1 opponents, we iterate through the opponents array. If we find any
    player with a different number of opponents, we return false. However, if all players have exactly 
    n - 1 opponents, we return true.

    Step 1: Create an array with n + 1  empty set elements
        Input: n = 2, m = 1, k = [[1, 2]]
        Output: opponents = [{}, {}, {}]
    
    Step 2: For each round of the game and for every pair i, j where, 0 <= i < n / 2 and n / 2 <= j < n, 
    add i to the opponents set of j and j to the opponents of i
        Input: n = 2, m = 1, k = [[1, 2]]
        Output: opponents = [{}, {2}, {1}]
    
    Step 3: Go through each position/index in the opponents array, starting from 1 up to n. Calculate the 
    number of opponents for each player by counting the unique elements (using a set) at that index. If the
    count is not equal to n - 1, then return false as the final result.
        Input: opponents = [{}, {2}, {1}]
        Output: number of opponents of player 1 is 1,  player 2 is also 1
    
    Step 4: If the execution reaches step 4 without returning false, it means that every player has 
    competed against n - 1 players. Therefore, we will return true as the final result.
        Input: opponents = [{}, {2}, {1}]
        Output: True
    
    """
    
    # Testing Step 1
    opponents = [set() for _ in range(n + 1)]
    
    # Testing Step 2
    for game in k:
        for i in range(n//2):
            for j in range(n // 2, n):
                opponents[game[i]].add(game[j])
                opponents[game[j]].add(game[i])
    
    # Testing Step 3
    for i in range(1, n + 1):
        if len(opponents[i]) != n - 1:
            return False 
    
    return True 