from random import random, seed
import numpy as np


def init_shuffle(test=False):
    seed()
    return test


def gen_playlist(n):
    return list(range(n))


def gen_placements(size):
    shufflelist = list(np.zeros((size,), dtype=int))
    i = 0
    while i < size:
        shufflelist[i] = random() - 2
        i += 1
    for place in range(size):
        index = shufflelist.index(min(shufflelist))
        shufflelist[index] = place
    return shufflelist


def rearrange(target, placements):
    retlist = list(np.zeros((len(target),), dtype=int))
    for i in range(len(target)):
        retlist[i] = target[placements.index(i)]
    return retlist


def test():
    pass
