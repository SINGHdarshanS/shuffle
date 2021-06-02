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


def sequencer_rec(original, modified, maxlen):
    ret = {"runs": 1}
    print(original)
    for i in range(2, maxlen + 1):
        ret[i] = 0
        tester = original[:i]
        start = modified.index(tester[0])
        for p in range(start + 1, start + i + 1):
            print(p)
            print(list(range(start + 1, start + i + 1)))
            try:
                if p == start + i and original[p - start] == modified[p]:
                    ret[i] = 1
                    break
                elif original[p - start] != modified[p]:
                    break
            except:
                break
    return ret


def test(size, passes, repetitions=True, sequences=True, max_sequence_length=3):
    if max_sequence_length < 2:
        max_sequence_length = 2
    for run in range(passes):
        tester = gen_playlist(size)
        shuffle = rearrange(tester, gen_placements(size))
        for entry in tester:
            curr_loc = tester.index(entry)
            # print(curr_loc)
            if repetitions:
                if entry == shuffle[curr_loc]:
                    # this should be recorded later
                    pass
            if sequences and size - curr_loc >= max_sequence_length:
                ret = sequencer_rec(tester[curr_loc:], shuffle, max_sequence_length)
                print(ret)  # add cumulation and some data visualization
