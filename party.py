from time import time
from monsters import pokeclasses
from clear import clear
from menus import *
from roll import roll, rrang, riv, pokeSelect

from zones import zonelist

def party(pl):
    clear()
    for poke in pl.team:
        print poke.name+'  '+str(poke.hp)+'/'+str(poke.stats.stats['hp'])+'  lvl '+str(poke.level)
    print '\n'
    inp=pMenu(partyMen)
    clear()
    if inp == 'swap':
        pl.team.head(pl.team.index(swapMen(pl)))
    if inp == 'details':
        print "Select a Pokemon"
        numb=1
        pokemap=[]
        for poke in pl.team:
            print str(numb)+':   '+poke.name+'  '+str(poke.hp)+'/'+str(poke.stats.stats['hp'])+'  lvl '+str(poke.level)
            numb+=1
            pokemap.append(poke)
        fin=False
        while fin == False:
            invalidInput=0
            inp=raw_input('enter menu #:')
            try: 
                selection=int(inp)
                if selection<1 or selection>len(pokemap):
                    invalidInput=1
            except:
                invalidInput=1
            if invalidInput==1:
                print 'invalid selection.\n'
            else:
                fin=True
        examinee=pokemap[selection-1]
        clear()
        print examinee.name+':   '+str(examinee.pokedexid).zfill(3)
        print 'level: '+str(examinee.level)
        print 'experience: '+str(examinee.xp)+' / '+str(examinee.nextxp) +' ('+str(examinee.nextxp-examinee.xp)+'   remaining) '
        print 'stats:'
        for stat in examinee.stats.stats:   
            print '    '+stat+'    '+str(examinee.stats.stats[stat])
        print '\n'
        print 'advanced details:'
        print 'initial values:'
        for iv in examinee.stats.iv:    
            print '    '+iv+'    '+str(examinee.stats.iv[iv])
        print '\n'
        print '    experience values:'
        for ev in examinee.stats.ev:    
            print '    '+ev+'    '+str(examinee.stats.ev[ev])
        print '\n'
        raw_input('enter to return')