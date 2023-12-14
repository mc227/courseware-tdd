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
    for _ in range(n):
        portions.append(portion)
        if remain > 1:
            portions[-1] += 1
            remain -= 1
    return portions

def test_split_amount():
    """
    docstring
    """
    assert [1] == split_amount(1,1)
    assert [2, 2] == split_amount(4,2)
    assert [2, 2, 1] == split_amount(5,3)
    assert [3,3,2,2,2] == split_amount(12,5)
    print("All tests pass!")

if __name__ == "__main__":
    # print(split_amount(4,2))
    # print(split_amount(5,3))
    test_split_amount()
