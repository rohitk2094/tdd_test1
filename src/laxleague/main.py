import math
import numpy as np
import sys


# def add_two_fractions(a, b):
#     # if a[1] is not None
#     if a[1] == 0 or b[1] == 0:
#         result = np.nan
#     elif a[1] is not None and b[1] is not None:
#         numerator = a[0] * b[1] + b[0] * a[1]
#         denominator = a[1] * b[1]
#         result = (numerator, denominator)
#     return result

# - ----------************  Sell one item **********----------
N_ITEMS = 10

class Sale:

    # def __init__(self):
    # def set_priceByBarcode(self, price, barcode):
    #     self.price_list[barcode] = price
    #
    # def get_price(self):
    #     if barcode in self.price_list:
    #         price = price_list[barcode]

    def get_price(self, barcode):
        if barcode == "12345":
            price = 'EUR: 10'
        elif barcode == "23456":
            price = 'EUR: 10.5'
        elif barcode == "99999":
            price = 'barcode not found: 99999'
        else:
            price = "scanning error"
        return price



def generate_price_list(N_ITEMS):
    price_list = dict()
    for i in range(1, N_ITEMS + 1):
        if i < N_ITEMS - 2:
            price_list[i] = "EUR: " + str(i * 10)
        else:
            price_list[i] = None

    print('price_list: \n', price_list)
    return price_list


def get_price(barcode):
    price_list = generate_price_list(N_ITEMS)
    barcode = int(barcode)
    if barcode in price_list:
        price = price_list[barcode]
        if price is None:
            print('No matching price found')
    elif barcode == "":
        price = None
        print('scanning error')
    else:
        price = None
        print('barcode not found')
    return price


N_ITEMS = 10
price_list = generate_price_list(N_ITEMS)

# # Get the user input on the barcode
# for j in range(0, 2):
#     barcode = input('Type barcode: ')
#     # barcode = '2'
#     print('barcode: ', barcode)
#     price = get_price(barcode)
#     print('price: ', price)

#
#
# if __name__ == "__main__":
#     result = add_two_fractions(5,2)
#     print(result)
#     print('Result is: ', result)
