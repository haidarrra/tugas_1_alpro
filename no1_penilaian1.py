# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 17:04:16 2024

@author: ASUS
"""
n = int(input("Masukkan nilai n : "))
total = 0
i = 1
for i in range(1, n+1):
    total += i
    print(f"Jumlah bilangan dari 1 hingga {n} adalah {total}")
