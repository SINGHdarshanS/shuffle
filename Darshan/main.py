from shuffle import *
import matplotlib.pyplot as plt

gate = init_shuffle(test=True)

# # generating a playlist of length n #####################
# print('shuffling...')
# playlist = gen_playlist(20)
# print("Original playlist: {}".format(playlist))
#
# # generating a list of randoms of equal size to playlist and using that to order the new list
# shufflelist = gen_placements(len(playlist))
#
# # rearranging playlist based on order specified by shufflelist
# playlist = rearrange(playlist, shufflelist)
# print("Shuffled playlist: {}".format(playlist))

# run optional tests here if gate boolean is set to True during init at start of script
if gate:  # run testing spectrum here
    summy = 0
    lenny = 1001
    seq = np.zeros(lenny)
    for i in range(2, lenny):
        ret = test(i, 100, max_sequence_length=2)
        print("There were a total of {} in-place repetitions over {} test runs. (Avg {} IPRs per run)".format(ret['ipr'], ret['runs'], ret['ipr'] / ret['runs']))
        print(ret)
        summy += ret['ipr']
        seq[i] = ret[2]
    print(summy)
    print(seq)
    plt.plot(list(range(1, len(seq)+1)), seq)
    plt.show()


    # ret = test(102, 50, max_sequence_length=3)
    # # print(ret)
    # print("There were a total of {} in-place repetitions over {} test runs. (Avg {} IPRs per run)".format(ret['ipr'], ret['runs'], ret['ipr'] / ret['runs']))
