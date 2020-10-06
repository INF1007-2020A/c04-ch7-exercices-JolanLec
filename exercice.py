#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math


# TODO: Définissez vos fonction ici
def Volume_masse(a=2, b=4, c=2, masse_volumique=10):
    volume = 4/3*math.pi*a*b*c
    masse = masse_volumique* volume

    return volume, masse


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(Volume_masse(5, 2))
    pass
