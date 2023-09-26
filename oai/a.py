from typing import List 

def solution(n: int, x: int, y: int) -> int:
    # write your solution here
    
    """ Approach #1: Brute force recursion
    
    Step 1: Check if n is a base case
        Sub-step 1: if  n is equal to 0, return x.
            Input: n = 0, x = 1, y = 2
            Output: 1
    
        Sub-step 2: if n is equal to 1, return y.
            Input: n = 1, x = 1, y = 2
            Output: 2
    
    Step 2: Calculate the gibonacci value of n - 1 and store it in a variable, gb_n_1.
        Input: n = 3, x = 1, y = 2
        Output: gb_n_1 = gb_(3 - 1) = gb_2 = gb_1 - gb_0 = y - x = 2 - 1 = 1
    
    Step 3: Calculate the gibonacci value of n - 2 and store it in gb_n_2
        Input: n = 3, x = 1, y = 2
        Output: gb_n_2 = gb_(3 - 1) = gb_1 = y = 2
    
    Step 4: Calculate the gb_n with the recurive formula gb_n = gb_n_1 - gb_n_2
        Input: n = 3, x = 1, y = 2
        Output: gb_n = gb_n_1 - gb_n_2 = 1 - 2 = -1
    
    # Testing step 1
    if n == 0:
        return x
    
    if n == 1:
        return y
        
    # Testing step 2
    gb_n_1 = solution(n - 1, x, y)
    
    # Testign step 3
    gb_n_2 = solution(n - 2, x, y)
    
    # Testing step 4
    gb_n = gb_n_1 - gb_n_2
    if n == 3:
        print("gibonacci of 3 is", gb_n)
    return gb_n
    
    As can be seen gibonacci of 3 is computed many times and as the initial value of
    n increases so does the number of repetitions. Calling the function with the same 
    arguments repeatedly makes it inefficient and due to this the algorithm has exponential 
    asymptotic time complexity. 
    """
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    """  Approach #2: Recursion with memoization (Dynamic programming)
    
    To improve the previous approach, it is necessary to store the value of 
    each calculation so that recomputation can be avoided. For this purpose, we will 
    create a memo variable.
    
    The function is going to take one additional parameter, memo, to store the intermediate results. 
    In future calls, before it tries to compute it checks if it is already computed and stored.
    If already computed, return it from memo. If not, compute it, store it (for future use) and return it.
    
    Create a helper function, gibonacci, that computes the value. This function takes n, x, y, and memo 
    as arguments. The main function will create a memo dictionary and pass it, along with the values
    of n, x, and y, to the helper function. Finally, the main function will return the value returned 
    by the helper function.
    
    Steps (of the helper function, gibonacci)
        
        Step 1: If n is in the memo return the value that the memo holds for n:
            Input: n = 1, x = 1, y = 2
            Output: 2
        
        Step 2: Compute gb_n_1 and gb_n_2 ((n - 1)th and (n -2)th gibonacci number)
            Input: n = 3, x = 1, y = 2
            Output: gb_n_1 = 1, and gb_n_2 = 2
        
        Step 3: Calculate gb_n by subtracting gb_n_2 from gb_n_1, store it as memo[n] and then return it
            Input: n = 2, x = 1, y = 2
            Output: memo = {0: 1, 1: 2, 2: 1}, and final result = 1
    
    def gibonacci(n: int, x: int, y: int, memo: Dict[int, int]) -> int:
        
        # Testing Step 1
        if n in memo:
            return memo[n]
        
        # Testing step 2
        gb_n_1 = gibonacci(n - 1, x, y)
        gb_n_2 = gibonacci(n - 2, x, y)
        
        # Testing step 3 of gibonacci
        memo[n] = gb_n_1 - gb_n_2
        return memo[n]
    
    
    Steps (of the the solution)
        Step 1: Create a memo variable and set memo[0] and memo[1] to be x and y 
        respectively.
            Input: n = 2, x = 1, y = 2
            Output: memo = {0: 4, 1: 2}
    
        Step 2: call the gibonacci function and return its returned value
            Input: n = 2, x = 1, y = 2
            Output: final answer = gibonacci(n, x, y, memo) = 1
    
    # Testing step 1
    memo = {0: x, 1: y}

    # Testing step 1
    return gibonacci(n, x, y, memo)
    
    
    This algorithm has a linear asymptotic time complexity as it computes the values for each n at 
    most once. Additionally, it stores values for each n, resulting in linear space complexity.
    """
    
    
    
    
    
    
    
    
    """ Approach #3 Bottom up Dynamic Programming
    
    Rather than going from top to bottom, we will start by storing the first two values and successively 
    compute the following values by using the previous two values. We only need to keep track of the 
    previous two values which gets the space complexity down to being constant.
    
    Step 1: If n is 0, return x
        Input: n = 0, x = 1, y = 2
        Output: 1
    
    Step 2: If n is 1, return y
        Input: n = 1, x = 1, y = 2
        Output: 2
    
    Step 3: Initialize, gb_n_2 and gb_n_1 as x and y respectively
    
    Step 4: Starting from 2 calculate all gibonacci values upto n storing
    your results in a variable gb_n
        Sub-step 1: calculate gb_n = gb_n_1 - gb_n_2
        Sub-step 2: then, assign the value of gb_n_1 to gb_n_2 and the value of gb_n to gb_n_1
        
        Input: n = 4, x = 1, y = 2
        Output: gb_2 = 1, gb_3 = -1, gb_4 = -2
    
    Step 5: return the final value of gb_n
        Input: n = 4, x = 1, y = 2
        Output: -2
    
    # Testig Step 1
    if n == 0:
        return x
    
    # Testing Step 2
    if n == 1:
        return y
    
    # Testing step 3
    gb_n_2 = x
    gb_n_1 = y
    
    # Testing step 4
    for i in range(2, n + 1):
        gb_n = gb_n_2 - gb_n_1
        gb_n_2 = gb_n_1
        gb_n_1 = gb_n
        print("gb_{i} is ", gb_n)
    
    return gb_n
    
    I encountered a problem by swapping gb_n_2 and gb_n_1 while I was computing gb_n. 
    I will modify the above code by swapping the position of the two variables.
    
    for i in range(2, n + 1):
        gb_n = gb_n_1 - gb_n_2
        gb_n_2 = gb_n_1
        gb_n_1 = gb_n
    
    return gb_n
    """
    
    
    
    
    
    
    
    
    
    
    """ Approach #4 Constant Time & Space
    
    While printing the gibonacci sequence in the above approach, we noticed that the values repeat 
    themselves at intervals of 6. This means that the Fibonacci of n and the Fibonacci of n + 6 will
    have the same value. The common property among these numbers is the remainder when they are divided 
    by 6.
    
    Pattern:
        gb_0 = x gb_1 = y gb_2 = y - x gb_3 = -x gb_4 = -y gb_5 = -y + x
        gb_6 = x gb_7 = y gb_8 = y - x gb_9 = -x gb_10 = -y gb_11 = -y + x
        gb_12 = x gb_13 = y gb_14 = y - x gb_15 = -x gb_16 = -y gb_17 = -y + x
        gb_18 = x gb_19 = y gb_20 = y - x gb_21 = -x gb_22 = -y gb_23 = -y + x
    
    From the above pattern we notice that at maximum we will have only 6 different values.
    
    Step 1: Store the the precomputed 6 values inside of a dictionary 
        Input: n = 5, x = 1, y = 2
        Output: values = {0: x, 1: y, 2: y - x, 3: -x, 4: -y, 5: -y + x }
        
    Step 2: Find the group of n by finding n % 6
        Input: n = 5, x = 1, y = 2
        Output: group = n % 6 = 5
        
    Step 3: Return the value of the group n belongs
        Input: n = 5, x = 1, y = 2
        Output: final answer = values[group] = -y + x = -1
        
    # Testig Step 1
    values = { 0: x, 1: y, 2: y - x, 3: -x, 4: -y, 5: -y + x }
    
    # Testing Step 2
    group = n % 6
    
    # Testing Step 3
    return values[group]
    
    """