"""
copied from the course
"""

def split_amount(amount,n):
    """
    docstring
    """
    portion, remain = amount // n, amount % n
    portions = []
    for _ in range(n):
        portions.append(portion)
        if remain > 0:
            portions[-1] += 1
            remain -= 1
    return portions

if __name__ == "__main__":
    print(split_amount(5,3))
