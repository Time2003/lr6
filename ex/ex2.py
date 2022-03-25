#!/usr/bin/env python3
# -*- кодирование: utf-8 -*-

если __name__ == '__main__':
    word = input("Введите слово: ")

    idx = len(слово) // 2
    если len(word) % 2 == 1:
        # Длина слова нечетная.
        r = word[:idx] + word[idx+1:]
    ещё:
        # Длина слова четная.
        r = word[:idx-1] + word[idx+1:]

    печать(r)