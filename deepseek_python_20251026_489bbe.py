def union(a, b):
    return a | b

def intersection(a, b):
    return a & b

def difference(a, b):
    return a - b

def sym_diff(a, b):
    return a ^ b

def cartesian(a, b):
    return {(x, y) for x in a for y in b}