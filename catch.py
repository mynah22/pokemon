from roll import rrang
def catch(target, pl, ball):
    #if ptrainer batlle:
        #FAIL
    #if master ball:
        #return (1,0)
    #random number based on ball
    if ball=='pb':
        chanceValue=rrang(0,255)
    if ball=='gb':
        chanceValue=rrang(0,200)
    if ball=='ub':
        chanceValue=rrang(0,150)
    #status variable
    if (target.status['asleep'] == 'true' 
    or target.status['frozen'] == 'true'):
        statusVariable=25
    elif (target.status['poisoned']
    or target.status['paralyzed']
    or target.status['burned']):
        statusVariable=12 
    else:
        statusVariable=0
    fullChance= chanceValue - statusVariable
    if fullChance < 0:
        caught=1
    else:
        if ball=='gb':
            hpFactor=int(target.stats.stats['hp']*255)/12
        else:
            hpFactor=(target.stats.stats['hp']*255)/8
        if hpFactor>255:
            hpFactor==255
        if target.catchRate < fullChance:
            caught = 0
        else:
            secondChance=rrang(0,255)
            if secondChance <=hpFactor:
                caught=1
            else:
                caught=0
    #calc shakes
    shakes=target.catchRate*100
    if ball=='pb':
        shakes=shakes/255
    if ball=='gb':
        shakes=shakes/200
    if ball=='ub':
        shakes=shakes/150
    if shakes>=255:
        shakes=3
    else:
        shakes=(shakes*hpFactor)/255
        if (target.status['asleep'] 
        or target.status['frozen']):
            shakes+=10
        if (target.status['poisoned'] 
        or target.status['burned']
        or target.status['paralyzed']):
            shakes+=5
        if shakes < 10:
            shakes=0
        elif shakes > 9 and shakes< 30:
            shakes = 1
        elif shakes > 29 and shakes< 70:
            shakes=2
        elif shakes > 69:
            shakes = 3
    return (caught,shakes)