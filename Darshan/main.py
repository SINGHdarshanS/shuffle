from lib import *

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
    ret = test(100, 100, max_sequence_length=5)
    print(ret)
