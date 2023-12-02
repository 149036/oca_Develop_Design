def execute_param_fn(args, hosei, fn):
    return fn(args, hosei)


args = [1, 2, 3]
hosei = 4

print(execute_param_fn(args, hosei, lambda a, b: max(a) + b))
print(execute_param_fn(args, hosei, lambda a, b: min(a) - b))
