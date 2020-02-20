#!/usr/bin/env pypy
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 10:46:12 2020

@author: shane
"""

import math
import os
import time
from decimal import Decimal, getcontext

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main(n=None, p=100):
    print("Sharp formula")
    print("Terms: " + str(n))
    print("Prec: " + str(p) + "\n")

    getcontext().prec = p

    pi = pi_()
    ln3 = Decimal(3).ln()
    t1 = time.time()

    result = 0
    for k in range(n):
        sign = -1 if k % 2 else 1
        pow = Decimal(0.5 - k) * ln3
        term = 2 * sign * Decimal(pow).exp() / Decimal(2 * k + 1)
        result += term
        # Update every 100 terms
        if k and not k % 100:
            print("Done: " + str(k))

    error = (result - Decimal(math.pi)).copy_abs()

    print("\nPi:   " + str(result))
    print("Error: " + str(error))


def pi_():
    text = open("../static/pi-1000.txt").read()
    return Decimal(text)


if __name__ == "__main__":
    main(n=100)
