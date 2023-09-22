#!/usr/bin/env python

S_1 = lambda x: 1 + x - x**3
S_2 = lambda x: 1 - 2*(x-1) -3 *(x-1)**2 + 4 * (x-1)**3
S_3 = lambda x: 4 *(x-2) + 9 *(x-2)**2 - 3 * (x-2)**3
print(S_1(0), S_1(1))
print(S_2(1), S_2(2))
print(S_3(2), S_3(3))