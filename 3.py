#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Дано слово. Переставить его первую букву на место последней. При этом вторую, третью, ...,
# последнюю буквы сдвинуть влево на одну позицию.
string1 = input("Введите слово")
a = len(string1)
b = string1[0]
string2 = string1 + b
string3 = string2[1:a+1]
print(string3)