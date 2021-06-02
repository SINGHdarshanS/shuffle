# -*- coding: utf-8 -*-
import random

def original_list():
    ranlist = list(range(10))
    return(ranlist)

def shuffle_list(original_list):
    length_list = len(original_list)
    for i in range(length_list):
        j = random.randint(0, i+1) 
        original_list[i], original_list[j] = original_list[j], original_list[i] 
