#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 08:07:06 2020

@author: mads
"""

def inputNumberFilter(prompt):
# INPUTNUMBER Prompts user to input a number
#
# Usage: num = inputNumber(prompt) Displays prompt and asks user to input a
# number. Repeats until user inputs a valid number.
#
# Author: Mikkel N. Schmidt, mnsc@dtu.dk, 2015
# This version modified by Ivan Viemoes Cuevas s205823 og Mads Andersen s204137
    while True:
        num = input(prompt) #Tests if input is empty string and breaks if True
        if num == "":
            break
        try:
            num = float(num)
            break
        except ValueError:
            pass
    return num