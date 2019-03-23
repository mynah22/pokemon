def lvlxpcalc(rate, lvl):
    if rate == 1:
        return s(lvl)
    if rate == 2:
        return mf(lvl)
    if rate == 3:
        return mf(lvl)
    if rate == 4:
        return f(lvl)

def f(lvl):
    return(4*(lvl**3)/5)
    
def mf(lvl):
    return (lvl**3)

def ms(lvl):
    return int(((6/5.0)*(lvl**3))-(15*(lvl**2))+(100*lvl)-140)

def s(lvl):
    return (5*(lvl**3))/4

