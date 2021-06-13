from random import random, seed
import numpy as np
import time


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
        shuffle = rearrange(tester, gen_placements(size))
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

        print("run completed in {} seconds".format((time.time_ns() - tick) / 1000000000))
    print("ALL TESTING COMPLETED IN {} SECONDS.".format((time.time_ns() - tick_init) / 1000000000))
    return cum_tests
