#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Applying Arbitrary Arguments"""

import pet


class Dog(pet.Pet):
    """A subclass from Pet class in pet.py"""

    def __init__(self, has_shots=False, **kargs):
        """Constructor for Dog Class.

        Args:
            has_shots(bool): defaults to False
            **kargs: arbitrary argument dictionary.

        Attributes:
            has_shots(bool): boolean, has a default: False.

        """
        self.has_shots = has_shots
        pet.Pet.__init__(self, **kargs)
