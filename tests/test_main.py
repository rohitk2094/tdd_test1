import numpy as np

# from laxleague.main import add_two_fractions

# def test_addition():
#     assert (3, 1) == add_two_fractions((1, 1), (2, 1))
#     assert (5, 4) == add_two_fractions((3, 2), (6, 4))

# def test_addition_nan():
#     assert np.nan == add_two_fractions((1, 2), (2, 0))


## Sell one item
from laxleague.main import generate_price_list, get_price, Sale


def test_get_price():
    # assert 50 == get_price('5', price_list)
    sale = Sale()
    price = sale.get_price("99999")

    assert price == "Not found"

    # assert 20 == get_price(2, price_list)
    # assert None == get_price(8, price_list)
    # assert None == get_price(11, price_list)


