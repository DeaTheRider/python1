import hashlib
from itertools import groupby


def rabin_karp(s, dictionary):
    for key in dictionary:
        len_sub = len(key)
        h_subs = hashlib.sha1(key.encode('utf-8')).hexdigest()
        for i in range(len(s) - len_sub + 1):
            if h_subs == hashlib.sha1(s[i:i + len_sub].encode('utf-8')).hexdigest():
                dictionary[key] += 1
        return dictionary


def is_eq_str(a, b):
    ha = hashlib.sha1(a.encode('utf-8')).hexdigest()
    hb = hashlib.sha1(b.encode('utf-8')).hexdigest()
    return ha == hb


def substrings(s, dictionary):
    for char, group in groupby(s):
        substr = ''
        for i in group:
            substr += i
            dictionary[substr] = 1
    return dictionary


def main():
    s = input()
    dictionary = {}
    dictionary = substrings(s, dictionary)
    print(rabin_karp(s, dictionary))


if __name__ == "__main__":
    main()
