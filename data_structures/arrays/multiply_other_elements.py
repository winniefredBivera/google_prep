"""
MULTIPLY OTHER ELEMENTS
q. given an array, replace each element with the multiplication product of every other element in the array
dont ruin it by putting 0 in the array
WINNIEFRED BIVERA
"""


def multiples_of_every_other_element_no_zeroes(arr):
    product_non_zeroes = 1
    for element in arr:
        product_non_zeroes = product_non_zeroes * \
            element if element != 0 else product_non_zeroes
    output_arr = [product_of_every_other_element(
        product_non_zeroes, element, 0 in arr) for element in arr]
    return output_arr


def product_of_every_other_element(product_non_zeros, element, zero_is_present):
    if zero_is_present is True:
        if element != 0:
            return 0
        else:
            return product_non_zeros
    else: 
        return product_non_zeros/element
