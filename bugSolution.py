def function_with_uncommon_error(a, b):
    if b == 0:
        return "Division by zero is not allowed"
    else:
        return a / b

result = function_with_uncommon_error(10, 0)
print(result)

result2 = function_with_uncommon_error(10, 2)
print(result2)