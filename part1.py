#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'Nats'
import timeit

def findMedian(l1, l2):
    l = sorted(l1 + l2)
    return (l[N-1]+l[N])/2.0

a = [1, 2, 3, 4]
b = [1, 4, 5, 6]
N = len(a)

def findM(q, w):
    N = len(q)
    s = [0] * 2 * N
    i = 0
    j = 0
    while i < N and j < N:
        if q[i] < w[j]:
            s[i+j] = q[i]
            i += 1
        else:
            s[i+j] = w[j]
            j += 1
    if i > j:
        s[i+j] = w[j:]
    else:
        s[i+j] = q[i:]
    return (s[N-1]+s[N])/2.0

print findMedian(a, b)
print findM(a, b)

print timeit.timeit('findMedian(a,b)', number=10000, setup="from __main__ import findMedian, a, b")
print timeit.timeit('findM(a, b)', number=10000, setup="from __main__ import findM, a, b")