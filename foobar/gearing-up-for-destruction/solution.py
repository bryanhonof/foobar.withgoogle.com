# I got really stuck on this one so here are the sources I took insperation from.
# https://stackoverflow.com/questions/40465866/google-foobar-gearing-up-for-destruction
# https://gist.github.com/jlacar/e66cd25bac47fab887bffbc5e924c2f5

# Lessons learned form this challenge: do more research before starting to program

from fractions import Fraction

def solution(pegs):
    n_pegs = len(pegs)
    n_pegs_even = True if (n_pegs % 2 == 0) else False
    
    awnser = (-pegs[0] + pegs[n_pegs - 1]) if n_pegs_even else (-pegs[0] - pegs[n_pegs -1])
    awnser += sum((2 * (-1)**(i + 1) * pegs[i]) for i in range(1, n_pegs - 1))
    
    first_gear_r = Fraction(2 * (float(awnser) / 3 if n_pegs_even else awnser)).limit_denominator()
    
    tmp_r = first_gear_r
    for i in range(n_pegs - 2):
        d = pegs[i + 1] - pegs[i]
        next_r = d - tmp_r
        if (tmp_r < 1 or next_r < 1):
            return [-1,-1]
        else:
            tmp_r = next_r
            
    return [first_gear_r.numerator, first_gear_r.denominator]
