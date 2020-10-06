#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math


# TODO: Définissez vos fonction ici
def Volume_masse(a, b, c, masse_volumique):
    volume = 4/(3*math.pi*a*b*c)
    masse = masse_volumique* volume

    return volume, masse


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    pass
