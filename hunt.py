from time import time
from monsters import pokeclasses
from clear import clear
from menus import *
from roll import *
from swap import *
from zones import zonelist

def hpbar(per=50):
    if per < 1:
        return "[__________]"
    elif per < 10:
        return "[=_________]"
    elif per < 20:
        return "[==________]"
    elif per < 30:
        return "[===_______]"
    elif per < 40:
        return "[====______]"
    elif per < 50:
        return "[=====_____]"
    elif per < 60:
        return "[======____]"
    elif per < 70:
        return "[=======___]"
    elif per < 80:
        return "[========__]"
    elif per < 90:
        return "[=========_]"
    else:
        return "[==========]"



def hunt(pl):
    zone = zonelist[pl.zone] # get player zone
    clear()
    if zone.nullflag:
        print 'No monsters here! Move somewhere else.'
        inp = raw_input('Press any key...')
        return
    selectedTup=pokeSelect(zone.pokelist)
    #tup[]: 0-id, 1-encounter chance, 2-low lvl, 3-high lvl
    rmon=pokeclasses[selectedTup[0]-1](lvl=rrang(selectedTup[2],selectedTup[3]))      
    print 2
    encfin=False #encounter finished flag set to untrue
    if pl.dex.icn[rmon.pokedexid][0]<1:
        pl.dex.icn[rmon.pokedexid][0]=1 #set encountered flag in dex for wild monster
    while not encfin:
        clear()
        #monster appears
        print 'Wild '+rmon.name+' appears!\n'
        #monster gui
        print 'wild '+rmon.name+'\n'
        print hpbar(100*(float(rmon.hp)/rmon.stats.stats['hp'])) +'   ('+str(rmon.hp)+')   lvl  '+str(rmon.level)+'\n\n'
        #player gui
        print pl.name+"'s "+pl.team[0].name+'\n'
        print hpbar(100*(float(pl.team[0].hp)/pl.team[0].stats.stats['hp'])) +'   ('+str(pl.team[0].hp)+')   lvl  '+str(pl.team[0].level)+'\n\n'
        
        inp=pMenu(huntMen)
        
        #user selection = attack
        if inp=='attack':
            pl.team[0].attack(rmon)
            rmon.attack(pl.team[0])

            #If enemy monster dies
            if rmon.hp<1:
                clear()
                #add evs
                for stat in pl.team[0].stats.statNames:
                    if pl.team[0].stats.ev[stat]<100:
                        pl.team[0].stats.ev[stat]+=1
                        if stat=='hp':
                            pl.team[0].stats.calchp(pl.team[0].level)
                        else:
                            pl.team[0].stats.calcstat(stat, pl.team[0].level)
                    #hold evs at max (100)
                    else:
                        pl.team[0].stats.ev[stat]=100
                #display
                print rmon.name+' K.O.'
                #add xp
                if pl.team[0].level<100:    
                    xpg = (rmon.stats.faintxp*rmon.level)/7
                    pl.team[0].xp+=xpg
                    print pl.team[0].name+' Gained '+str(xpg)+'xp!'
                    print str(pl.team[0].xp)+' / '+str(pl.team[0].nextxp) +' ('+str(pl.team[0].nextxp-pl.team[0].xp)+'   remaining) '
                    #level up process
                    while pl.team[0].xp >= pl.team[0].nextxp and pl.team[0].level<100:
                        pl.team[0].level += 1
                        if pl.team[0].level==100:
                            pl.team[0].xp=pl.team[0].nextxp
                            pl.team[0].nextxp=pl.team[0].xp+1
                        else:
                            pl.team[0].nextxpcalc()
                        for stat in pl.team[0].stats.statNames:
                            if stat == 'hp':
                                pl.team[0].stats.calchp(pl.team[0].level)
                                pl.team[0].hp=pl.team[0].stats.stats['hp']
                            else:
                                pl.team[0].stats.calcstat(stat, pl.team[0].level)
                     
                        print pl.team[0].name+' grew to level '+str(pl.team[0].level)+'!'
                    #evolve process
                    if pl.team[0].evolvable:
                        if pl.team[0].level>=pl.team[0].evlvl:
                            print pl.team[0].name +' has evolved into '+pokeclasses[pl.team[0].pokedexid]().name+'!'
                            tmpevmon = pokeclasses[pl.team[0].pokedexid]()
                            pl.dex.caught(tmpevmon)
                            tmpevmon.xp = pl.team[0].xp
                            tmpevmon.level = pl.team[0].level
                            tmpevmon.nextxpcalc()
                            tmpevmon.stats.ev = pl.team[0].stats.ev
                            tmpevmon.stats.iv = pl.team[0].stats.iv
                            for stat in tmpevmon.stats.statNames:
                                if stat == 'hp':
                                    tmpevmon.stats.calchp(tmpevmon.level)
                                    tmpevmon.hp=tmpevmon.stats.stats['hp']
                                else:
                                    tmpevmon.stats.calcstat(stat, tmpevmon.level)
                            pl.team[0]=tmpevmon
                #$$$$$ boieeee
                reward=rrang(1000)
                pl.money+=reward
                print pl.name+' found $'+str(reward)+'!\n'
                raw_input('press return')
                #break loop
                encfin=True
            
            #if player monster is dead
            if pl.team[0].hp<1:
                clear()
                #if player has usable monsters
                if pl.countawake():
                    print pl.name+"'s "+pl.team[0].name+' K.O.!'
                    xxx=raw_input('\npress enter')
                    pl.team.head(pl.team.index(swapMen(pl)))
                    print 'keep fighing '+rmon.name+'?'
                    swapch=pMenu(binMen)
                    if swapch=='yes':
                        pass
                    elif swapch=='no':
                        print pl.name+' got away safely!'
                        xxx=raw_input('\npress enter')
                        encfin=True
                #blackout if no monsters usable
                else:
                    print pl.name+' is out of usable pokemon!'
                    xxx=raw_input('\npress enter')
                    encfin=True



        if inp.startswith('swap'):
            pl.team.head(pl.team.index(swapMen(pl)))



        if inp=='catch':
            clear() 
            print pl.team[0].name+'  '+str(pl.team[0].hp)
            print rmon.name+'  '+str(rmon.hp)
            ball=pbMenu(pl)
            pl.balls[ball]-=1
            if ball=='pb':   
                if roll(20):
                    rmon.caught(pl)  
                    pl.dex.caught(rmon)                          
                    encfin=True
            if ball=='gb':
                if roll(30):
                    rmon.caught(pl)
                    pl.dex.caught(rmon)                           
                    encfin=True
            if ball=='ub':
                if roll(40):
                    rmon.caught(pl)
                    pl.dex.caught(rmon)                            
                    encfin=True           
                        



        if inp=='run':
            clear()
            print pl.name+' got away safely!'
            xxx=raw_input('\npress enter')
            encfin=True
    return True
        
    