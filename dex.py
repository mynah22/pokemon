from monsters import *
from clear import clear
from menus import pMenu

def dexui(pl):
    saw = 0
    caught = 0
    sawlist=[]
    caughtlist=[]
    for poke in pl.dex.icn:
        if pl.dex.icn[poke][0]>0:
            saw+= 1
            sawlist.append(poke)
        if pl.dex.icn[poke][0]>1:
            caught+=1
            sawlist.remove(poke)
            caughtlist.append(poke)
    clear()
    print pl.name+'\n\n'
    print 'Pokemon seen: '+str(saw)
    print 'Pokemon captured: '+str(caught)
    print '\n\n'
    inp=pMenu([
        'list uncaptured pokemon', 
        'list successfully captured pokemon', 'exit'
        ])
    if inp.startswith('list u'):
        clear()
        print 'Seen but uncaptured pokemon:'
        print '('+str(len(pl.dex.icn)-saw)+' unseen)\n'
        for poke in sawlist:
            print str(poke).zfill(3)+'  '+pl.dex.icn[poke][1]
        xxx=raw_input()

    if inp.startswith('list s'):
        clear()
        print 'Captured pokemon:'
        print str(caught)+' species captured'
        for poke in caughtlist:
            print pl.dex.icn[poke][1]
        xxx=raw_input()
    elif inp.startswith('exit'):
        pass

class pokedex(object):
    def __init__(self):
        pclasscpy=[]
        for pclass in pokeclasses:
            pclasscpy.append(pclass)
        pclasscpy.reverse()
        self.icn={}
        #ID, capture status, name
        for number in range(152)[1:]:
            self.icn[number]=[-1, pclasscpy.pop()().name]
    def saw(self, poke):
        pass
    def caught(self, poke):
        self.icn[poke.pokedexid][0]=2
