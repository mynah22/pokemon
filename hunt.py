from time import time
from monsters import pokeclasses
from clear import clear
from menus import *
from roll import *
from swap import *
from zones import zonelist
from attacks import Struggle
from catch import catch
from time import sleep

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
    #select wild pokemon
    if selectedTup[2] == selectedTup[3]:
        rmon=pokeclasses[selectedTup[0]-1](lvl=selectedTup[3])
    else:
        rmon=pokeclasses[selectedTup[0]-1](lvl=rrang(selectedTup[2],selectedTup[3]))      
    encfin=False #encounter finished flag set to untrue
    if pl.dex.icn[rmon.pokedexid][0]<1:
        pl.dex.icn[rmon.pokedexid][0]=1 #set encountered flag in dex for wild monster
    for mon in [rmon, pl.team[0]]:
        #reset comnbat stat stages
        mon.stats.combatStages={
            'hp':0,'speed':0, 
            'atk':0,'def':0,
            'spAtk':0,'spDef':0,
        }
    while not encfin:
        clear()
        #monster appears
        #print 'Wild '+rmon.name+' appears!\n'
        #monster gui
        print 'wild '+rmon.name+'\n'
        print hpbar(100*(float(rmon.hp)/rmon.stats.stats['hp'])) +'   ('+str(rmon.hp)+')   lvl  '+str(rmon.level)+'\n\n'
        #player gui
        print pl.name+"'s "+pl.team[0].name+'\n'
        print hpbar(100*(float(pl.team[0].hp)/pl.team[0].stats.stats['hp'])) +'   ('+str(pl.team[0].hp)+')   lvl  '+str(pl.team[0].level)+'\n\n'
        
        inp=pMenu(huntMen)
        #if user selection = attack
        if inp=='attack':
            #move select phase
            atkid=atkMenu(pl.team[0])
            clear()
            rmonAtkID=rmon.wildAttack()
            #select first attacker based on move speed priority and atkstat speed
            if pl.team[0].moveset[atkid].speedPriority == rmon.moveset[rmonAtkID].speedPriority:
                if (pl.team[0].stats.stats['speed'] * pl.team[0].statStageCoefficient(pl.team[0].stats.combatStages['speed']) 
                > rmon.stats.stats['speed'] * rmon.statStageCoefficient(rmon.stats.combatStages['speed'])):
                    firstAttacker=pl.team[0]
                elif (pl.team[0].stats.stats['speed'] * pl.team[0].statStageCoefficient(pl.team[0].stats.combatStages['speed']) 
                < rmon.stats.stats['speed'] * rmon.statStageCoefficient(rmon.stats.combatStages['speed'])):    
                    firstAttacker=rmon
                elif (pl.team[0].stats.stats['speed'] * pl.team[0].statStageCoefficient(pl.team[0].stats.combatStages['speed']) 
                == rmon.stats.stats['speed'] * rmon.statStageCoefficient(rmon.stats.combatStages['speed'])):
                    firstAttacker=[rmon,pl.team[0]][rrang(2)]
            elif pl.team[0].moveset[atkid].speedPriority > rmon.moveset[rmonAtkID].speedPriority:
                firstAttacker=pl.team[0]
            elif pl.team[0].moveset[atkid].speedPriority < rmon.moveset[rmonAtkID].speedPriority:
                firstAttacker=rmon
            #select second attacker and moveid by reference
            if firstAttacker == pl.team[0]:
                firstMoveID = atkid
                secondAttacker = rmon
                secondMoveID = rmonAtkID
            elif firstAttacker == rmon:
                firstMoveID = rmonAtkID
                secondAttacker = pl.team[0]
                secondMoveID = atkid
            #
            ####first atk   
            #
            clear()                     
            if firstMoveID != 5:
            #if at least 1 move with positive PP
                firstPreAtkHP=firstAttacker.hp
                secondPreAtkHP=secondAttacker.hp
                castResult= firstAttacker.moveset[firstMoveID].cast(firstAttacker, secondAttacker) 
                #rmon gui
                print 'wild '+rmon.name+'\n'
                print hpbar(100*(float(rmon.hp)/rmon.stats.stats['hp'])) +'   ('+str(rmon.hp)+')   lvl  '+str(rmon.level)+'\n\n'
                #player gui
                print pl.name+"'s "+pl.team[0].name+'\n'
                print hpbar(100*(float(pl.team[0].hp)/pl.team[0].stats.stats['hp'])) +'   ('+str(pl.team[0].hp)+')   lvl  '+str(pl.team[0].level)+'\n\n'
                #move display
                print firstAttacker.name+' uses '+firstAttacker.moveset[firstMoveID].name+"!"
                #hit/miss display
                if castResult:
                    print secondAttacker.name +' took '+str(secondPreAtkHP-secondAttacker.hp)+' damage!'
                    if not firstPreAtkHP == firstAttacker.hp: 
                        print firstAttacker.name +' took '+str(firstPreAtkHP - firstAttacker.hp)+' damage!'
                else:
                    print firstAttacker.name+' missed!'                
            elif atkid == 5:
            #if no moves left, struggle
                firstPreAtkHP=firstAttacker.hp
                secondPreAtkHP=secondAttacker.hp
                castResult = Struggle().cast(firstAttacker, secondAttacker)
                #rmon gui
                print 'wild '+rmon.name+'\n'
                print hpbar(100*(float(rmon.hp)/rmon.stats.stats['hp'])) +'   ('+str(rmon.hp)+')   lvl  '+str(rmon.level)+'\n\n'
                #player gui
                print pl.name+"'s "+pl.team[0].name+'\n'
                print hpbar(100*(float(pl.team[0].hp)/pl.team[0].stats.stats['hp'])) +'   ('+str(pl.team[0].hp)+')   lvl  '+str(pl.team[0].level)+'\n\n'
                #hit/miss display
                print firstAttacker.name+' has no moves left!'
                print firstAttacker.name+' struggles!'
                if castResult:
                    print secondAttacker.name +' took '+str(secondPreAtkHP-secondAttacker.hp)+' damage!'
                    if not firstPreAtkHP == firstAttacker.hp: 
                        print firstAttacker.name +' took '+str(firstPreAtkHP - firstAttacker.hp)+' damage!'        
                else:
                    print firstAttacker.name+' missed!'  
            wait=raw_input('press enter...')
            ##
            ########## after atk eval
            ##
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
                        pl.team[0].wildMovesetFill()
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
            ##########
            #second atk
            ##
            ##
            if secondAttacker.hp > 0:
                clear()
                if secondMoveID != 5:
                #if at least 1 move with positive PP
                    secondPreAtkHP=secondAttacker.hp
                    firstPreAtkHP=firstAttacker.hp
                    castResult=secondAttacker.moveset[secondMoveID].cast(secondAttacker, firstAttacker)
                    #rmon gui
                    print 'wild '+rmon.name+'\n'
                    print hpbar(100*(float(rmon.hp)/rmon.stats.stats['hp'])) +'   ('+str(rmon.hp)+')   lvl  '+str(rmon.level)+'\n\n'
                    #player gui
                    print pl.name+"'s "+pl.team[0].name+'\n'
                    print hpbar(100*(float(pl.team[0].hp)/pl.team[0].stats.stats['hp'])) +'   ('+str(pl.team[0].hp)+')   lvl  '+str(pl.team[0].level)+'\n\n'
                    #move display
                    print secondAttacker.name+' uses '+secondAttacker.moveset[secondMoveID].name+"!"
                    #hit/miss display
                    if castResult:
                        print firstAttacker.name +' took '+str(firstPreAtkHP-firstAttacker.hp)+' damage!'
                        if not secondPreAtkHP == secondAttacker.hp: 
                            print secondAttacker.name +' took '+str(secondPreAtkHP - secondAttacker.hp)+' damage!'
                    else:
                        print secondAttacker.name+' missed!'                
                elif atkid == 5:
                #if no moves left, struggle
                    secondPreAtkHP=secondAttacker.hp
                    firstPreAtkHP=firstAttacker.hp
                    castResult = Struggle().cast(secondAttacker, firstAttacker)
                    #rmon gui
                    print 'wild '+rmon.name+'\n'
                    print hpbar(100*(float(rmon.hp)/rmon.stats.stats['hp'])) +'   ('+str(rmon.hp)+')   lvl  '+str(rmon.level)+'\n\n'
                    #player gui
                    print pl.name+"'s "+pl.team[0].name+'\n'
                    print hpbar(100*(float(pl.team[0].hp)/pl.team[0].stats.stats['hp'])) +'   ('+str(pl.team[0].hp)+')   lvl  '+str(pl.team[0].level)+'\n\n'
                    #move display
                    print secondAttacker.name+' has no moves left!'
                    print secondAttacker.name+' struggles!'
                    #hit/miss display                    
                    if castResult:
                        print firstAttacker.name +' took '+str(firstPreAtkHP-firstAttacker.hp)+' damage!'
                        if not secondPreAtkHP == secondAttacker.hp: 
                            print secondAttacker.name +' took '+str(secondPreAtkHP - secondAttacker.hp)+' damage!'        
                    else:
                        print secondAttacker.name+' missed!'  
                wait=raw_input('press enter...')
            ##
            ##Attacks over
            ##
            #If enemy monster dies
            if not encfin:
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
            print rmon.name+'  '+str(rmon.hp)+'/'+str(rmon.stats.stats['hp'])
            for status in rmon.status:
                if rmon.status[status]:
                    print status
            ball=pbMenu(pl)
            if ball:
                pl.balls[ball]-=1
                caughtTup=catch(rmon, pl, ball)
                #if capture fails
                if not caughtTup[0]:
                    if not caughtTup[1]:
                        pass
                    elif caughtTup[1]==1:
                        print rmon.name+' resists...'
                        sleep(1)
                    elif caughtTup[1]==2:
                        print rmon.name+' resists...'
                        sleep(1)
                        print rmon.name+' resists...'
                        sleep(1)
                    elif caughtTup[1]>2:
                        print rmon.name+' resists...'
                        sleep(1)
                        print rmon.name+' resists...'
                        sleep(1)
                        print rmon.name+' resists...'
                        sleep(1)        
                    print rmon.name+' escaped!'
                    inp=raw_input('press enter...')
                #if capture succeeds
                if caughtTup[0]:
                    if not caughtTup[1]:
                        pass
                    elif caughtTup[1]==1:
                        print rmon.name+' resists...'
                        sleep(1)
                    elif caughtTup[1]==2:
                        print rmon.name+' resists...'
                        sleep(1)
                        print rmon.name+' resists...'
                        sleep(1)
                    elif caughtTup[1]>2:
                        print rmon.name+' resists...'
                        sleep(1)
                        print rmon.name+' resists...'
                        sleep(1)
                        print rmon.name+' resists...'
                        sleep(1)
                    print rmon.name+' was captured!!'
                    rmon.caught(pl)  
                    pl.dex.caught(rmon) 
                    inp=raw_input('press enter...')                         
                    encfin=True
        if inp=='run':
            clear()
            print pl.name+' got away safely!'
            xxx=raw_input('\npress enter')
            encfin=True
    return True
        
    