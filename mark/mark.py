"""
@15:07
this is the freewriting python file that
i can run while i'm watching the course
"""

def split_amount(amount,n):
    """
    docstring
    """
    portion, remain = amount // n, amount % n
    portions = []
    for i in range(n):
        portions.append(portion)
        if remain > 1:
            portions[-1] += 1
            remain -= 1
    return portions


if __name__ == "__main__":
    print(split_amount(4,2))
