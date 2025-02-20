def function_with_uncommon_error_solution(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# The iterative version works correctly even for large values of n
result = function_with_uncommon_error_solution(1000)