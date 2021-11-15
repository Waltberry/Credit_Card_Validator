# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 17:37:05 2021

@author: Walt
"""

#Request input from customer
card_number = input('Please enter your credit card number:>> ')

#Checking Credit card validation
''' Credit Card Validation using Luhn's algorithm'''

num_list = [int(char) for char in card_number]
num_len = len(num_list)
num_list_rev = num_list[::-1]
double = 0
single = 0
for i in range(0,num_len):
    if i%2 != 0:
        if 2*num_list_rev[i]>9:
            double = double + 2*num_list_rev[i] - 9
        else:
            double = double + 2 * num_list_rev[i]
    else:
        single = single + num_list_rev[i]

if (double+single)%10 == 0:
    print(f'{card_number} is a valid credit card number.')
else:
    print(f'{card_number} is not a valid credit card number.')
