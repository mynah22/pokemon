from random import randrange as rrang
def riv():
    return rrang(1,16)
def roll(weight):
    res=rrang(100)
    if res<weight:
        return True
    else:
        return False
def pokeSelect(pokeTupList):
    #tup[]: 0-id, 1-encounter chance, 2-low lvl, 3-high lvl
    bigPokeList = []
    for pokeTup in pokeTupList:
        c=0
        while c<pokeTup[1]:
            bigPokeList.append(pokeTup)
            c+=1
    return bigPokeList[rrang(len(bigPokeList))-1]#obtain rand monster