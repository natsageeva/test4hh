#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import timeit

__author__ = 'Nats'

import math

a = 1
b = 12
k = 10

def lengthPeriod(x, y):
    r = x
    for i in range(int(math.log(y)/math.log(2))):
        r = 10 * r % y
    q = r
    r = 10 * r % y
    l = 1;
    while r != q:
        r = 10 * r % y
        l += 1
    return l

def lengthPrePeriod(y):
    r = y % 2
    l = 0
    while r == 0:
        y = y // 2
        r = y % 2
        l += 1
    r = y % 5
    l1 = 0
    while r == 0:
        y = y // 5
        r = y % 5
        l1 += 1
    return max(l, l1)

def findFrackPart(x, y, lpp, lp):
    i = 0
    frackPart = "0."
    while i in range(lpp + lp):
        frackPart += str(10 * x // y)
        x = 10 * x % y
        i += 1
    return frackPart

def convertIntK(x, p):
    s = ""
    gotcha = True
    while gotcha:
        n = x % p
        if n >= 10:
            s += chr(87 + n)
        else:
            s += str(n)
        x = x // p
        if x == 0:
            gotcha = False
    s = s[::-1]
    return s

def convertFracK(x, p, lpp, lp):
    quantcha = 0
    flag = False
    s = "."
    while quantcha in range(lpp + lp):
        if x == 0:
            break
        if quantcha == lpp:
            s += "("
            flag = True
        m = math.modf(x * p)
        if int(m[1]) >= 10:
            s += chr(87 + int(m[1]))
        else:
            s += str(int(m[1]))
        x = m[0]
        quantcha += 1
    if flag:
        s += ")"
    return s

def divK(x, y, p):
    lp = lengthPeriod(x, y)
    lpp = lengthPrePeriod(y)
    answ = convertIntK(x // y, p)
    if x % y != 0:
        answ += convertFracK(float(findFrackPart(x % y, y, lpp, lp)), p, lpp, lp)
    return answ

try:
    print divK(a, b, k)
except ValueError:
    print "Введенное число некорректно!"

print timeit.timeit('divK(a, b, k)', number=10000, setup="from __main__ import divK, a, b, k")