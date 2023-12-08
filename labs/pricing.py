"""pricing.py"""
def calculate(price, tax=0, discount=0):
    """calculate method"""
    return round((price - discount) * (1+tax), 2)
    