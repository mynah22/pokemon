from monsters import *
from menus import *
from player import *
from hunt import hunt
from clear import clear
from shop import shop
from heal import heal
from save import *
from bank import bank
from dex import *
from move import move
from party import party

def mainAct(pl):
    clear()
    choice=pMenu([
        'hunt','move','heal',
        'party','shop','dex',
        'bank', pl.name,'save',
        'leave',
        ])
    if choice=='hunt':
        if not pl.countawake():
            clear()
            print pl.name+' is out of usable pokemon!'
            xxx=raw_input('\n\npress enter')
        else:
            hunt(pl)
    if choice=='party':
        party(pl)
    if choice==pl.name:
        clear()
        print 'Status\n\n'
        print pl.name+'   $'+str(pl.money)
        for bt in pl.balls:
            if pl.balls[bt]>0:
                print bt+': '+str(pl.balls[bt])
        print '\n'
        raw_input('enter to return')
        return 0
    if choice=='shop':
        shop(pl)    
    if choice=='heal':
        heal(pl)
    if choice=='dex':
        dexui(pl)
    if choice=='bank':
        bank(pl)
    if choice=='save':
        save(pl)
    if choice=='leave':
        return 1
    if choice=='move':
        move(pl)


def starter(player):
    clear()
    print 'New Game\n\n'
    choice=pMenu(starterMen)
    if choice.startswith('B'):
        player.team.append(pokeclasses[0]())
    elif choice.startswith('C'):
        player.team.append(pokeclasses[3]())
    elif choice.startswith('S'):
        player.team.append(pokeclasses[6]())  
    player.money+=3000
    player.balls['pb']+=25
    player.balls['gb']+=5
    player.balls['ub']+=1
    player.dex=pokedex()
    player.dex.caught(player.team[0])
        
def startAct():
    selected=False
    while not selected:
        clear()
        choice=pMenu(startMen)
        if choice=='new':
            clear()
            print 'New Game\n\n'
            p=player(raw_input('enter name:'))
            starter(p)
            selected=True
        if choice=='load':
            clear()
            p=load()
            selected=True
        if choice=='exit':
            exit()
    inProgress=True
    while inProgress:
        if mainAct(p):
           inProgress=False 



    
 
 
 

    
        