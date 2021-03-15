# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 22:24:07 2021

@author: Sabrina Marques
"""

def Fatorial(num):
    produto = 1

    while(num > 0):
        produto = produto * num

        num = num - 1

    return produto