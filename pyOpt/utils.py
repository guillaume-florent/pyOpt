#!/usr/bin/env python
# coding: utf-8

"""pyOpt utilities"""


def machine_precision():
    r"""Define a value for machine precision"""
    eps = 1.0  # define a value for machine precision
    while (eps / 2.0 + 1.0) > 1.0:
        eps /= 2.0

    eps *= 2.0

    return eps
