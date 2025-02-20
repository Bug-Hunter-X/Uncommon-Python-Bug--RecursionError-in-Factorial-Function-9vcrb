def function_with_uncommon_error(n):
    if n == 0:
        return 1
    else:
        return n * function_with_uncommon_error(n-1)

# This will cause a RecursionError for large values of n
result = function_with_uncommon_error(1000)