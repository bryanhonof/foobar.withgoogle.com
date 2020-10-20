#!/usr/bin/env python3

import itertools

def solution(l):
    try:
        for i in range(len(l), -1, -1):
            combinations = list(itertools.permutations(l, i))
            combinations.sort(reverse=True)
            
            for combo in combinations:
                number = int(''.join(str(i) for i in combo))
                if (number % 3) == 0:
                    return number
    except ValueError:
        return 0
