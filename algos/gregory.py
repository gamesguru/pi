#!/usr/bin/env pypy
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 10:46:12 2020

@author: shane
"""

import math
import time
from decimal import Decimal, getcontext


def main(n=None, p=50):
    print("Gregory formula")
    print("Terms: " + str(n))
    print("Prec: " + str(p) + "\n")

    getcontext().prec = p

    t1 = time.time()

    result = 0
    for k in range(1, n):
        sign = 1 if k % 2 else -1
        term = sign / Decimal(2 * k - 1)
        result += term
        # Update every 100 terms
        if k and not k % 100:
            print("Done: " + str(k))

    result = result * 4
    error = (result - Decimal(math.pi)).copy_abs()

    print("\nPi:   " + str(result))
    print("Error: " + str(error))


if __name__ == "__main__":
    main(n=5000)
