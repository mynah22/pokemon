from clear import clear
from menus import *


def shop(pl):
    clear()
    print pl.name+'`s money:  $'+str(pl.money)
        
    inp=pMenu(shopMen)
    if inp.startswith('Poke'):
        maxq=pl.money/25
        clear()
        print 'buying pokeballs.\n'
        print pl.name+'`s money:  $'+str(pl.money)
        print '\nmax quantity: '+str(maxq)
        selq=raw_input()
        pl.money-=int(selq)*25
        pl.balls['pb']+=int(selq)

    if inp.startswith('Great'):
        maxq=pl.money/200
        clear()
        print 'buying greatballs.\n'
        print pl.name+'`s money:  $'+str(pl.money)
        print '\nmax quantity: '+str(maxq)
        selq=raw_input()
        pl.money-=int(selq)*200
        pl.balls['gb']+=int(selq)

    if inp.startswith('Ultra'):
        maxq=pl.money/750
        clear()
        print 'buying ultraballs.\n'
        print pl.name+'`s money:  $'+str(pl.money)
        print '\nmax quantity: '+str(maxq)
        selq=raw_input()
        pl.money-=int(selq)*750
        pl.balls['ub']+=int(selq)