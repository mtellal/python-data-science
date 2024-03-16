
"""
    From a list, count the number of time a specific object is inside
"""

def count_in_list(l: list, obj) -> int:
    return len([x for x in l if obj == x])

