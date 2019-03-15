def pMenu(tarmen):
    numb=1
    for item in tarmen:
       if numb<10:
          print str(numb)+':   '+item
          numb+=1
       else:
          print str(numb)+':  '+item
          numb+=1
    fin=0
    while fin != 1:
       inval=0
       inp=raw_input('enter menu #:')
       try: 
           t=int(inp)
           if t<1 or t>len(tarmen):
               inval=1
       except:
           inval=1
       if inval==1:
           print 'invalid selection.\n'
       else:
           fin=1         
    return tarmen[int(inp)-1]

def pbMenu(player):
    numb=1
    mendic={}
    for item in player.balls:
        if player.balls[item] > 0:
            mendic[numb]=item
            print str(numb)+':   '+item
            numb+=1
        if len(mendic)<1:
            print 'no pokeballs!\n\n'
            xxx=raw_input('press enter')
    fin=0
    while fin != 1:
       inval=0
       inp=raw_input('enter menu #:')
       try: 
           t=int(inp)
           if t<1 or t>len(mendic):
               inval=1
       except:
           inval=1
       if inval==1:
           print 'invalid selection.\n'
       else:
           fin=1         
    return mendic[int(inp)]


def bankMenu(pl, mode='d'):
    numb=1
    if mode.lower()=='d':
      target=pl.team
    elif mode.lower()=='w':
      target=pl.bank

    for poke in target:
        print str(numb)+':   '+poke.name
        numb+=1
    fin=0
    while fin != 1:
       inval=0
       inp=raw_input('enter menu #:')
       try: 
           t=int(inp)
           if t<1 or t>len(target):
               inval=1
       except:
           inval=1
       if inval==1:
           print 'invalid selection.\n'
       else:
           fin=1         
    return target[int(inp)-1]

def swapMen(pl):
# clear()
  print "Select lead pokemon:"
  numb=1
  pokemap=[]
  for poke in pl.awakeList():
      print str(numb)+':   '+poke.name+' ('+str(poke.hp)+')'
      numb+=1
      pokemap.append(poke)
  fin=0
  while fin != 1:
     inval=0
     inp=raw_input('enter menu #:')
     try: 
         t=int(inp)
         if t<1 or t>len(pokemap):
             inval=1
     except:
         inval=1
     if inval==1:
         print 'invalid selection.\n'
     else:
         fin=1         
  return pokemap[t-1]


def atkMenu(castingMon):
    #returns the dict key that corresponds to the selected move.
    #returns 5 if no moves available
    numb=1
    usableAtks=[]
    for movekey in castingMon.moveset:
      if castingMon.moveset[movekey]:
        if castingMon.moveset[movekey].remainingUsagePoints:
          usableAtks.append(movekey)
    if len(usableAtks)<1: 
      return 5
      #returns 5 if no moves available
    for moveID in usableAtks:
      move = castingMon.moveset[moveID]
      print str(moveID+1)+':  '+move.name+'   '+str(move.remainingUsagePoints)+'/'+str(move.maxUsagePoints)
    fin=0
    while fin != 1:
       inval=0
       inp=raw_input('enter menu #:')
       try: 
           t=int(inp)
           if t<1 or not usableAtks.count(t-1):
               inval=1
       except:
           inval=1
       if inval==1:
           print 'invalid selection.\n'
       else:
           fin=1         
    return int(inp)-1
    #returns the dict key that corresponds to the selected move.
    #returns 5 if no moves available


startMen=[
    'load','new','exit'
]

starterMen=[
    'Squirtle', 
    'Charmander',
    'Bulbasaur'
]

binMen=[
  'yes','no'
]

huntMen=[
    'attack','catch',
    'swap poke', 'run'
]

shopMen=[
    'Poke balls:    $25',
    'Great balls:   $200',
    'Ultra balls:    $750'
]
    
partyMen=[
    'swap', 'details'
]