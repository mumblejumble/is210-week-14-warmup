#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Applying Arbitrary Arguments"""

from data import FRUIT


def get_cost_per_item(shoplist):
    """This function gives price for the fruit.

    Args:
        shoplist(dict): a set of dictionary.

    Returns:
        A dictionary with fruit name as key and their price as value.

    Example:
        >>> get_cost_per_item({'Lime': 12, 'Red Pear': 4, 'Peach': 24,
        'Beet': 1, 'Yellow Plantain': 10})
        {'Lime': 7.08, 'Peach': 95.76, 'Yellow Plantain': 9.9, 'Red Pear': 9.96}
    """
    return {fname: FRUIT[fname]*shoplist[fname]
            for fname in shoplist.iterkeys() if fname in FRUIT}


def get_total_cost(shoplist):
    """This function calculates the sum of the price for each fruit.

    Args:
        shoplist(dict): a set of dictionary.

    Returns:
        A total price for all fruits given, if found in FRUIT.

    Example:
        >>> get_total_cost({'Lime': 12, 'Red Pear': 4, 'Peach': 24, 'Beet': 1,
        'Yellow Plantain': 10})
        122.70000000000002
    """
    mysum = sum(f_price for f_price in get_cost_per_item(shoplist).itervalues())
    return mysum
