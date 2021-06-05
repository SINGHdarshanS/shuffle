# -*- coding: utf-8 -*-
import random

def original_list():
    ranlist = list(range(10))
    return ranlist

def shuffle_list(original_list):
    length_list = len(original_list)
    for i in range(length_list):
        j = random.randint(0, i+1) 
        original_list[i], original_list[j] = original_list[j], original_list[i]
    return original_list

def random_percent(original_list, shuffled_list):
    count = 0
    for i in range(len(original_list)):
        if i==shuffled_list[i]:
            count += 1
    percent = (count/len(original_list))*100
    return percent
