# -*- coding: utf-8 -*-
from list_review import *

playlist = original_list()
print("this is your original list: " + str(playlist))

shuffle = shuffle_list(playlist)
print("this is your original list: " + str(shuffle))


percentage = random_percent(playlist, shuffle)
print("this is your percent similarity between the two lists: " + str(percentage))