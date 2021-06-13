# This is a library for a shuffle that I'm implementing to achieve a more random shuffle, meaning that I will avoid all
# in-place repetitions and identical 2-3 item consecutive sequences with this shuffle. File will be similar to lib.py
# except that the rearrange() and gen_placements() functions will be deleted in favor of shuffle_rec() and shuffle_mt()

from random import random, seed
import numpy as np
import time
from math import floor


def init_shuffle(test=False):
    seed()
    return test


def gen_playlist(n):
    return list(range(n))


def shuffle_rec(sequence, first=False):
    length = len(sequence)
    retlist = np.zeros(length)

    if first:
        i = length % 3
        retlist = list(retlist[-i:]) + list(retlist[:-i])

    if length > 3:
        if length == 4:
            list0 = shuffle_rec(sequence[0:2])
            list1 = shuffle_rec(sequence[2:4])
            retlist = list(list1) + list(list0)
        elif length == 5:
            split = random()
            if split > .5:
                list0 = shuffle_rec(sequence[0:2])
                list1 = shuffle_rec(sequence[2:5])
                retlist = list(list1) + list(list0)
            else:
                list0 = shuffle_rec(sequence[0:3])
                list1 = shuffle_rec(sequence[3:5])
                retlist = list(list1) + list(list0)
        else:
            section = floor(length/3)
            split = random()
            list0 = shuffle_rec(sequence[0:section])
            list1 = shuffle_rec(sequence[section:section*2])
            list2 = shuffle_rec(sequence[section*2:])
            if split > .5:
                retlist = list(list1) + list(list2) + list(list0)
            else:
                retlist = list(list2) + list(list0) + list(list1)
        if first:
            # i = length % 3
            # retlist = list(retlist[-i:]) + list(retlist[:-i])
            if sequence[floor(length*(2/3))] == retlist[floor(length * (2 / 3))]:
                i1 = retlist[floor(length * (2 / 3))]
                i2 = retlist[floor(length * (1 / 3))]
                retlist[floor(length * (2 / 3))] = i2
                retlist[floor(length * (1 / 3))] = i1
            if sequence[floor(length*(2/3))-1] == retlist[floor(length * (2 / 3))-1]:
                i1 = retlist[floor(length * (2 / 3))-1]
                i2 = retlist[floor(length * (1 / 3))-1]
                retlist[floor(length * (2 / 3))-1] = i2
                retlist[floor(length * (1 / 3))-1] = i1
        return retlist

    else:
        if length == 3:
            split = random()
            if split > .5:
                retlist[0] = sequence[2]
                retlist[1] = sequence[0]
                retlist[2] = sequence[1]
            else:
                retlist[0] = sequence[1]
                retlist[1] = sequence[2]
                retlist[2] = sequence[0]
            return retlist

        elif length == 2:
            retlist[0] = sequence[1]
            retlist[1] = sequence[0]
            return retlist

        else:
            return sequence



def shuffle_mt(sequence):
    pass


def sequencer_rec(original, modified, maxlen):
    ret = {"runs": 1}
    for i in range(len(original) - 1):  # shifts start position by 1 over each loop
        for j in range(2 + i, maxlen + i + 1):  # widens tester by 1 over each loop
            if i + 2 <= j:
                if j - i not in ret.keys():
                    ret[j - i] = 0
                tester = original[i:j]
                if j - i > len(tester):
                    break
                for k in range(len(modified)):  # shifts start position by 1 over each loop
                    if modified[k:k + len(tester)] == tester:
                        ret[j - i] += 1
                        break

    return ret


def test(size, passes, repetitions=True, max_sequence_length=3):
    tick_init = time.time_ns()
    if max_sequence_length < 2:
        max_sequence_length = 2
    if max_sequence_length > size:
        max_sequence_length = size
    cum_tests = {'ipr': 0}
    for run in range(passes):
        tick = time.time_ns()
        tester = gen_playlist(size)
        shuffle = shuffle_rec(tester, first=True)
        reps = 0
        for entry in tester:
            curr_loc = tester.index(entry)
            if repetitions:
                if entry == shuffle[curr_loc]:
                    reps += 1
        ret = sequencer_rec(tester, shuffle, max_sequence_length)
        for key in ret.keys():
            if key not in cum_tests.keys():
                cum_tests[key] = ret[key]
            else:
                cum_tests[key] += ret[key]
        cum_tests['ipr'] += reps

    #     print("run completed in {} seconds".format((time.time_ns() - tick) / 1000000000))
    # print("ALL TESTING COMPLETED IN {} SECONDS.".format((time.time_ns() - tick_init) / 1000000000))
    return cum_tests
