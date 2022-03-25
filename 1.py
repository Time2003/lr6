#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Дано предложение. Вывести «столбиком» его первый, второй, пятый, шестой, девятый,
# десятый и т. д. символы.
string1 = input("Введите строку")
i = 0
j = 1
temp = len(string1)
while (temp):
    print(string1[i], string1[j], "\n")
    i += 4
    j += 4
    temp -= 4