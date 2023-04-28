"""
Split a number into portions, as evenly as possible.
(But it has a bug.)
"""
def split_amount(amount, n):
    """
    doc string here
    """
    portion, remain = amount // n, amount % n
    portions = []
    for i in range(n):
        portions.append(portion)
        if remain > 0:
            portions[-1] += 1
            remain -= 1
    return portions

def test_split_amount():
    assert [1] == split_amount(1,1)
    assert [2,2] == split_amount(4, 2)
    assert [2,2,1] == split_amount(5, 3)
    assert[3,3,2,2,2] == split_amount(12, 5)
if __name__ == "__main__":
    print(split_amount(5, 3))
    # test_split_amount()

