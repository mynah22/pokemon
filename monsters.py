from roll import *
from stats import statholder
from xpmap import lvlxpcalc
from attacks import attackClasses

class mon(object):
    def __init__(self, name='MissingNo.', lvl=5, base=[50,50,50,50,50,50],xpr=3):
        self.name=name
        self.level = lvl
        self.xprate=xpr
        self.xp = lvlxpcalc(self.xprate,self.level)
        self.nextxpcalc()
        self.stats=statholder()
        self.stats.base['hp']=base[0]
        self.stats.base['atk']=base[1]
        self.stats.base['def']=base[2]
        self.stats.base['spAtk']=base[3]
        self.stats.base['spDef']=base[4]
        self.stats.base['speed']=base[5]
        self.stats.faintxp=100
        self.moveset={1:None,2:None,3:None,4:None}
        self.moveladder={-1:143}
        for st in self.stats.statNames:
            self.stats.iv[st]=riv()
        self.calcAllStats()
        self.hp=int(self.stats.stats['hp'])
        self.types=['Normal']
   
    def calcAllStats(self):
        for st in self.stats.statNames:
            if st=='hp':
                self.stats.calchp(self.level)
            else:
                self.stats.calcstat(st,self.level)


    def attack(self, target):
        if roll(60):
            dmg=self.stats.stats['atk']
            dmg-=target.stats.stats['def']/1.25
            dmg+=1
            if dmg < 0:
                dmg = 0
            target.hp-=int(dmg)
            if target.hp<0:
                target.hp=0
    def wildAttack(self):
        usableAtks=[]
        for movekey in self.moveset:
            if self.moveset[movekey] and self.moveset[movekey].remainingUsagePoints:
                usableAtks.append(movekey)
        if len(usableAtks)<1:
            return 5
        else:
            return usableAtks[rrang(len(usableAtks))]
    def caught(self, pl):
        print self.name+' was caught!\n\n'     
        pl.dex.icn[self.pokedexid][0]=2
        if len(pl.team)<6:
            pl.team.append(self)
            xxx=raw_input('press enter')
        else:
            print 'Party full.'
            print self.name+'sent to bank.'                        
            pl.bank.append(self)

    def nextxpcalc(self):
        self.nextxp = lvlxpcalc(self.xprate,self.level+1)
    def xpcalc(self):
        pass
    def levelcalc(self):
        while self.xp > self.nextxp:
            self.level =+ 1
            self.nextxpcalc()
    def wildMovesetFill(self):
        levelkeys=[]
        for level in self.moveladder.keys():
            if level <= self.level:
                levelkeys.append(level)
        levelkeys.sort()
        levelkeys = levelkeys[-4:]
        movelist = []
        for key in levelkeys:
            for move in self.moveladder[key]:
                movelist.append(move)
        movelist=movelist[-4:]
        c=0
        for moveid in movelist:
             self.moveset[c]=attackClasses[moveid]()
             c+=1


class bulbasaur(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=1
        self.xpcalc()
        self.stats.faintxp=64
        self.evolvable=1
        self.evlvl=16
        self.types=['Grass','Poison']
        self.moveladder={
            -1:[52,143], 7:[72],13:[158],20:[93],
            27:[101], 34:[53], 41:[121], 48:[126]
            }
        self.wildMovesetFill()

class ivysaur(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(base=[60,62,63,80,80,60])
        self.name=self.__class__.__name__.title()
        self.pokedexid=2
        self.xprate=2
        self.stats.faintxp=141
        self.evolvable=1
        self.evlvl=32
        self.types=['Grass','Poison']
        self.moveladder={
            -1:[52,143,72], 13:[158], 22:[93],
            30:[101], 38:[53], 46:[121], 54:[126]
            }
        self.wildMovesetFill()


class venusaur(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=3
        self.xprate=2
        self.evolvable=0
        self.stats.faintxp=208
        self.types=['Grass','Poison']
        self.moveladder={
            -1:[52,143,72], 13:[158], 22:[93],
            30:[101], 43:[53], 55:[121], 65:[126]
            }
        self.wildMovesetFill()

class charmander(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=4
        self.xprate=2
        self.evolvable=1
        self.evlvl=16
        self.stats.faintxp=65
        self.types=['Fire']
        self.moveladder={
            -1:[111,52],9:[39],15:[73],22:[100],
            30:[120],38:[45],46:[43]
            }
        self.wildMovesetFill()


class charmeleon(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=5
        self.xprate=2
        self.evolvable=1
        self.evlvl=36
        self.stats.faintxp=142
        self.types=['Fire']
        self.moveladder={
            -1:[111,52,39],15:[73],24:[100],
            33:[120],42:[45],56:[43]
            }
        self.wildMovesetFill()
class charizard(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=6
        self.xprate=2
        self.evolvable=0
        self.stats.faintxp=209
        self.types=['Fire', 'Flying']
        self.moveladder={
            -1:[111,52,39],15:[73],24:[100],
            36:[120],46:[45],55:[43]
            }
        self.wildMovesetFill()
class squirtle(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=7
        self.xprate=2
        self.evolvable=1
        self.evlvl=16
        self.stats.faintxp=66
        self.types=['Water']        
        self.moveladder={
            -1:[143,144],8:[15],15:[160],22:[10],
            28:[163],35:[117],42:[62]
            }
        self.wildMovesetFill()

class wartortle(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=8
        self.xprate=2
        self.evolvable=1
        self.evlvl=36
        self.stats.faintxp=143
        self.types=['Water']        
        self.moveladder={
            -1:[143,144,15],15:[160],24:[10],
            31:[163],39:[117],47:[62]
            }
        self.wildMovesetFill()
class blastoise(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=9
        self.xprate=2
        self.evolvable=0
        self.stats.faintxp=210
        self.types=['Water']        
        self.moveladder={
            -1:[143,144,15,160],24:[10],
            31:[163],42:[117],52:[62]
            }
        self.wildMovesetFill()
class caterpie(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,30,35,20,20,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=10
        self.xprate=3
        self.evolvable=1
        self.evlvl=7
        self.stats.faintxp=53
        self.moveladder={-1:[143,133]}
        self.wildMovesetFill()
class metapod(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=11
        self.xprate=3
        self.evolvable=1
        self.evlvl=10    
        self.stats.faintxp=72
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class butterfree(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=12
        self.xprate=3
        self.evolvable=0
        self.stats.faintxp=160
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class weedle(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=13
        self.xprate=3
        self.evolvable=1
        self.evlvl=7
        self.stats.faintxp=52
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class kakuna(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=14
        self.xprate=3
        self.evolvable=1
        self.evlvl=10
        self.stats.faintxp=71
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class beedrill(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=15
        self.xprate=3
        self.evolvable=0
        self.stats.faintxp=159
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class pidgey(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=16
        self.xprate=2
        self.evolvable=1
        self.evlvl=18
        self.stats.faintxp=55
        self.types=['Normal', 'Flying']        
        self.moveladder={
            -1:[55], 5:[110], 12:[99], 19:[161],
            28:[162], 36:[4], 44:[85]
            }
        self.wildMovesetFill()

class pidgeotto(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=17
        self.xprate=2
        self.evolvable=1
        self.evlvl=36     
        self.stats.faintxp=113
        self.types=['Normal', 'Flying']
        self.moveladder={
            -1:[55, 110], 5:[110], 12:[99], 21:[161],
            31:[162], 40:[4], 49:[85]
            }
        self.wildMovesetFill()
class pidgeot(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=18
        self.xprate=2
        self.evolvable=0
        self.stats.faintxp=172
        self.types=['Normal', 'Flying']
        self.moveladder={
            -1:[55, 110, 99], 5:[110], 12:[99], 21:[161],
            31:[162], 44:[4], 54:[85]
            }
        self.wildMovesetFill()
class rattata(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=19
        self.xprate=3
        self.evolvable=1
        self.evlvl=20
        self.stats.faintxp=57
        self.moveladder={
            -1:[143, 144], 7:[99], 14:[64], 23:[48], 34:[138]
            }
        self.wildMovesetFill()
class raticate(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=20
        self.xprate=3
        self.evolvable=0
        self.stats.faintxp=116
        self.moveladder={
            -1:[143, 144, 99], 7:[99], 14:[64], 27:[48], 41:[138]
            }
        self.wildMovesetFill()
class spearow(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=21
        self.xprate=3
        self.evolvable=1
        self.evlvl=20
        self.stats.faintxp=58
        self.types=['Normal', 'Flying']
        self.moveladder={
            -1:[89, 52], 9:[72], 15:[49], 22:[85], 
            29:[36], 36:[4]
            }
        self.wildMovesetFill()
class fearow(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=22
        self.xprate=3
        self.evolvable=0
        self.evlvl=20
        self.stats.faintxp=162
        self.types=['Normal', 'Flying']
        self.moveladder={
            -1:[89, 52, 72], 9:[72], 15:[49], 22:[85], 
            29:[36], 36:[4]
            }
        self.wildMovesetFill()
class ekans(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=23
        self.xprate=3
        self.evolvable=1
        self.evlvl=22
        self.stats.faintxp=62
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class arbok(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=24
        self.xprate=3
        self.evolvable=0
        self.stats.faintxp=147
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class pikachu(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=25
        self.xprate=3
        self.evolvable=1
        self.evlvl=101 # stone evolve bypss
        self.stats.faintxp=82
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class raichu(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=26
        self.xprate=3
        self.evolvable=0
        self.stats.faintxp=122
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class sandshrew(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=27
        self.xprate=3
        self.evolvable=1
        self.evlvl=22
        self.stats.faintxp=93
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class sandslash(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=28
        self.xprate=3
        self.evolvable=0
        self.stats.faintxp=163
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class nidoranF(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name="Nidoran(f)"
        self.gender='f'
        self.pokedexid=29
        self.xprate=2
        self.evolvable=1
        self.evlvl=16
        self.stats.faintxp=59
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class nidorina(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.gender='f'
        self.pokedexid=30
        self.xprate=2
        self.evolvable=1
        self.evlvl=101 #stone evolve bypass
        self.stats.faintxp=117
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class nidoqueen(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.gender='f'
        self.pokedexid=31
        self.xprate=2
        self.evolvable=0
        self.stats.faintxp=194
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class nidoranM(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[46,57,40,40,40,50],xpr=2)
        self.name="Nidoran(m)"
        self.gender='m'
        self.pokedexid=32
        self.xprate=2
        self.evolvable=1
        self.evlvl=16
        self.stats.faintxp=60
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class nidorino(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.gender='m'
        self.pokedexid=33
        self.xprate=2
        self.evolvable=1
        self.evlvl=101 #stoneevl bypass
        self.stats.faintxp=118
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class nidoking(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.gender='m'
        self.pokedexid=34
        self.xprate=2
        self.evolvable=0
        self.stats.faintxp=195
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class clefairy(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=35
        self.xprate=4
        self.stats.faintxp=68
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class clefable(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=36
        self.xprate=4
        self.stats.faintxp=129
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class vulpix(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=37
        self.xprate=3
        self.stats.faintxp=63
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class ninetails(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=38
        self.xprate=3
        self.stats.faintxp=178
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class jigglypuff(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=39
        self.xprate=4
        self.stats.faintxp=76
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class wigglytuff(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=40
        self.xprate=4
        self.stats.faintxp=106
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class zubat(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=41
        self.xprate=3
        self.stats.faintxp=54
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class golbat(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=42
        self.xprate=3
        self.stats.faintxp=171
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class oddish(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=43
        self.xprate=2
        self.stats.faintxp=78
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class gloom(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=44
        self.xprate=2
        self.stats.faintxp=132
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class vileplume(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=45
        self.xprate=2
        self.stats.faintxp=184
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class paras(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=46
        self.xprate=3
        self.stats.faintxp=70
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class parasect(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=47
        self.xprate=3
        self.stats.faintxp=128
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class venonat(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=48
        self.xprate=3
        self.stats.faintxp=75
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class venomoth(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=49
        self.xprate=3
        self.stats.faintxp=138
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class diglett(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=50
        self.xprate=3
        self.stats.faintxp=81
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class dugtrio(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=51
        self.xprate=3
        self.stats.faintxp=153
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class meowth(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=52
        self.xprate=3
        self.stats.faintxp=69
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class persian(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=53
        self.xprate=3
        self.stats.faintxp=148
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class psyduck(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=54
        self.xprate=3
        self.stats.faintxp=80
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class golduck(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=55
        self.xprate=3
        self.stats.faintxp=174
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class mankey(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=56
        self.xprate=3
        self.evolvable=1
        self.evlvl=28
        self.stats.faintxp=74
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class primeape(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=57
        self.xprate=3
        self.stats.faintxp=149
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class growlith(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=58
        self.xprate=1
        self.stats.faintxp=91
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class arcanine(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=59
        self.xprate=1
        self.stats.faintxp=213
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class poliwag(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=60
        self.xprate=2
        self.stats.faintxp=77
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class poliwhirl(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=61
        self.xprate=2
        self.stats.faintxp=131
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class poliwrath(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=62
        self.xprate=2
        self.stats.faintxp=185
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class abra(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[25,20,15,105,55,90],xpr=2)#gen3 base stats. g1=45,49,49,65,65,45
        self.name=self.__class__.__name__.title()
        self.pokedexid=63
        self.xprate=2
        self.stats.faintxp=73
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class kadabra(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=64
        self.xprate=2
        self.stats.faintxp=145
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class alakazam(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=65
        self.xprate=2
        self.stats.faintxp=186
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class machop(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=66
        self.xprate=2
        self.stats.faintxp=88
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class machoke(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=67
        self.xprate=2
        self.stats.faintxp=146
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class machamp(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=68
        self.xprate=2
        self.stats.faintxp=193
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class bellsprout(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=69
        self.xprate=2
        self.stats.faintxp=84
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class weepinbell(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=70
        self.xprate=2
        self.stats.faintxp=151
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class victreebel(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=71
        self.xprate=2
        self.stats.faintxp=191
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class tentacool(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=72
        self.xprate=1
        self.stats.faintxp=105
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class tentacruel(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=73
        self.xprate=1
        self.stats.faintxp=205
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class geodude(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=74
        self.xprate=2
        self.stats.faintxp=86
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class graveler(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=75
        self.xprate=2
        self.stats.faintxp=134
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class golem(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=76
        self.xprate=2
        self.stats.faintxp=177
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class ponyta(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=77
        self.xprate=3
        self.stats.faintxp=152
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class rapidash(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=78
        self.xprate=3
        self.stats.faintxp=192
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class slowpoke(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=79
        self.xprate=3
        self.stats.faintxp=99
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class slowbro(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=80
        self.xprate=3
        self.stats.faintxp=164
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class magnemite(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=81
        self.xprate=3
        self.stats.faintxp=89
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class magneton(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=82
        self.xprate=3
        self.stats.faintxp=161
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class farfetchd(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name="Farfetch'd"
        self.pokedexid=83
        self.xprate=3
        self.stats.faintxp=94
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class doduo(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=84
        self.xprate=3
        self.stats.faintxp=96
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class dodrio(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=85
        self.xprate=3
        self.stats.faintxp=158
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class seel(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=86
        self.xprate=3
        self.stats.faintxp=100
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class dewgong(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=87
        self.xprate=3
        self.stats.faintxp=176
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class grimer(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=88
        self.xprate=3
        self.stats.faintxp=90
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class muk(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=89
        self.xprate=3
        self.stats.faintxp=157
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class shellder(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=90
        self.xprate=1
        self.stats.faintxp=97
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class cloyster(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=91
        self.xprate=1
        self.stats.faintxp=203
        self.moveladder={-1:[143]}
        self.wildMovesetFill()
class ghastly(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=92
        self.xprate=2
        self.stats.faintxp=95
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class haunter(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=93
        self.xprate=2
        self.stats.faintxp=126
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class gengar(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=94
        self.xprate=2
        self.stats.faintxp=190
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class onix(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=95
        self.xprate=3
        self.stats.faintxp=108
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class drowzee(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=96
        self.xprate=3
        self.stats.faintxp=102
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class hypno(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=97
        self.xprate=3
        self.stats.faintxp=165
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class krabby(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=98
        self.xprate=3
        self.stats.faintxp=115
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class kingler(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=99
        self.xprate=3
        self.stats.faintxp=206
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class voltorb(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=100
        self.xprate=3
        self.stats.faintxp=103
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class electrode(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=101
        self.xprate=3
        self.stats.faintxp=150
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class exeggcute(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=102
        self.xprate=1
        self.stats.faintxp=98
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class exeggutor(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=103
        self.xprate=1
        self.stats.faintxp=212
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class cubone(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=104
        self.xprate=3
        self.stats.faintxp=87
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class marowak(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=105
        self.xprate=3
        self.stats.faintxp=124
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class hitmonlee(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=106
        self.xprate=3
        self.stats.faintxp=139
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class hitmonchan(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=107
        self.xprate=3
        self.stats.faintxp=140
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class lickitung(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=108
        self.xprate=3
        self.stats.faintxp=127
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class koffing(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=109
        self.xprate=3
        self.stats.faintxp=114
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class weezing(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=110
        self.xprate=3
        self.stats.faintxp=173
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class rhyhorn(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=111
        self.xprate=1
        self.stats.faintxp=135
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class rhydon(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=112
        self.xprate=1
        self.stats.faintxp=204
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class chansey(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=113
        self.xprate=4
        self.stats.faintxp=255
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class tangela(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=114
        self.xprate=3
        self.stats.faintxp=166
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class kangaskhan(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__(lvl=lvl, base=[45,49,49,65,65,45],xpr=2)
        self.name=self.__class__.__name__.title()
        self.pokedexid=115
        self.xprate=3
        self.stats.faintxp=175
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class horsea(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__()
        self.name=self.__class__.__name__.title()
        self.pokedexid=116
        self.xprate=3
        self.stats.faintxp=83
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class seadra(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__()
        self.name=self.__class__.__name__.title()
        self.pokedexid=117
        self.xprate=3
        self.stats.faintxp=155
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class goldeen(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__()
        self.name=self.__class__.__name__.title()
        self.pokedexid=118
        self.xprate=3
        self.stats.faintxp=111
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class seaking(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__()
        self.name=self.__class__.__name__.title()
        self.pokedexid=119
        self.xprate=3
        self.stats.faintxp=170
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class staryu(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__()
        self.name=self.__class__.__name__.title()
        self.pokedexid=120
        self.xprate=1
        self.stats.faintxp=106
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class starmie(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__()
        self.name=self.__class__.__name__.title()
        self.pokedexid=121
        self.xprate=1
        self.stats.faintxp=207
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class mrmime(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__()
        self.name="Mr.Mime"
        self.pokedexid=122
        self.xprate=3
        self.stats.faintxp=136
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class scyther(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__()
        self.name=self.__class__.__name__.title()
        self.pokedexid=123
        self.xprate=3
        self.stats.faintxp=187
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class jynx(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__()
        self.name=self.__class__.__name__.title()
        self.pokedexid=124
        self.xprate=3
        self.stats.faintxp=137
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class electabuzz(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__()
        self.name=self.__class__.__name__.title()
        self.pokedexid=125
        self.xprate=3
        self.stats.faintxp=156
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class magmar(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__()
        self.name=self.__class__.__name__.title()
        self.pokedexid=126
        self.xprate=3
        self.stats.faintxp=167
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class pinsir(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__()
        self.name=self.__class__.__name__.title()
        self.pokedexid=127
        self.xprate=1
        self.stats.faintxp=200
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class tauros(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__()
        self.name=self.__class__.__name__.title()
        self.pokedexid=128
        self.xprate=1
        self.stats.faintxp=211
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class magikarp(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__()
        self.name=self.__class__.__name__.title()
        self.pokedexid=129
        self.xprate=1
        self.stats.faintxp=20
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class gyarados(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__()
        self.name=self.__class__.__name__.title()
        self.pokedexid=130
        self.xprate=1
        self.stats.faintxp=214
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class lapras(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__()
        self.name=self.__class__.__name__.title()
        self.pokedexid=131
        self.xprate=1
        self.stats.faintxp=219
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class ditto(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__()
        self.name=self.__class__.__name__.title()
        self.pokedexid=132
        self.xprate=3
        self.stats.faintxp=61
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class eevee(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__()
        self.name=self.__class__.__name__.title()
        self.pokedexid=133
        self.xprate=3
        self.stats.faintxp=92
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class vaporeon(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__()
        self.name=self.__class__.__name__.title()
        self.pokedexid=134
        self.xprate=3
        self.stats.faintxp=196
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class jolteon(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__()
        self.name=self.__class__.__name__.title()
        self.pokedexid=135
        self.xprate=3
        self.stats.faintxp=197
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class flareon(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__()
        self.name=self.__class__.__name__.title()
        self.pokedexid=136
        self.xprate=3
        self.stats.faintxp=198
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class porygon(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__()
        self.name=self.__class__.__name__.title()
        self.pokedexid=137
        self.xprate=3
        self.stats.faintxp=130
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class omanyte(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__()
        self.name=self.__class__.__name__.title()
        self.pokedexid=138
        self.xprate=3
        self.stats.faintxp=120
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class omastar(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__()
        self.name=self.__class__.__name__.title()
        self.pokedexid=139
        self.xprate=3
        self.stats.faintxp=199
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class kabuto(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__()
        self.name=self.__class__.__name__.title()
        self.pokedexid=140
        self.xprate=3
        self.stats.faintxp=119
 
class kabutops(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__()
        self.name=self.__class__.__name__.title()
        self.pokedexid=141
        self.xprate=3
        self.stats.faintxp=201
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class aerodactyl(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__()
        self.name=self.__class__.__name__.title()
        self.pokedexid=142
        self.xprate=1
        self.stats.faintxp=202
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class snorlax(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__()
        self.name=self.__class__.__name__.title()
        self.pokedexid=143
        self.xprate=1
        self.stats.faintxp=154
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class articuno(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__()
        self.name=self.__class__.__name__.title()
        self.pokedexid=144
        self.xprate=1
        self.stats.faintxp=215
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class zapdos(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__()
        self.name=self.__class__.__name__.title()
        self.pokedexid=145
        self.xprate=1
        self.stats.faintxp=216
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class moltres(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__()
        self.name=self.__class__.__name__.title()
        self.pokedexid=146
        self.xprate=1
        self.stats.faintxp=217
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class dratini(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__()
        self.name=self.__class__.__name__.title()
        self.pokedexid=147
        self.xprate=1
        self.stats.faintxp=67
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class dragonair(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__()
        self.name=self.__class__.__name__.title()
        self.pokedexid=148
        self.xprate=1
        self.stats.faintxp=144
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class dragonite(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__()
        self.name=self.__class__.__name__.title()
        self.pokedexid=149
        self.xprate=1
        self.stats.faintxp=218
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class mewtwo(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__()
        self.name=self.__class__.__name__.title()
        self.pokedexid=150
        self.xprate=1
        self.stats.faintxp=220
        self.moveladder={-1:[143]}
        self.wildMovesetFill()

class mew(mon):
    def __init__(self, lvl=5):
        super(self.__class__, self).__init__()
        self.name=self.__class__.__name__.title()
        self.pokedexid=151
        self.xprate=2
        self.stats.faintxp=64
        self.moveladder={-1:[143]}
        self.wildMovesetFill()


pokeclasses=[
    bulbasaur, ivysaur, venusaur, charmander, charmeleon,
    charizard, squirtle, wartortle, blastoise, caterpie, 
    metapod, butterfree, weedle, kakuna, beedrill, pidgey, 
    pidgeotto, pidgeot, rattata, raticate, spearow, fearow,
    ekans, arbok, pikachu, raichu, sandshrew, sandslash,
    nidoranF, nidorina, nidoqueen, nidoranM, nidorino, 
    nidoking, clefairy, clefable, vulpix, ninetails,
    jigglypuff, wigglytuff, zubat, golbat, oddish, gloom,
    vileplume, paras, parasect, venonat, venomoth, diglett,
    dugtrio, meowth, persian, psyduck, golduck, mankey, 
    primeape, growlith, arcanine, poliwag, poliwhirl, 
    poliwrath, abra, kadabra, alakazam, machop, machoke, 
    machamp, bellsprout, weepinbell, victreebel, tentacool, 
    tentacruel, geodude, graveler, golem, ponyta, rapidash,
    slowpoke, slowbro, magnemite, magneton, farfetchd, 
    doduo, dodrio, seel, dewgong, grimer, muk, shellder, 
    cloyster, ghastly, haunter, gengar, onix, drowzee,
    hypno, krabby, kingler, voltorb, electrode, exeggcute,
    exeggutor, cubone, marowak, hitmonlee, hitmonchan, 
    lickitung, koffing, weezing, rhyhorn, rhydon, chansey,
    tangela, kangaskhan, horsea, seadra, goldeen, seaking,
    staryu, starmie, mrmime, scyther, jynx, electabuzz, 
    magmar, pinsir, tauros, magikarp, gyarados, lapras, 
    ditto, eevee, jolteon, vaporeon, flareon, porygon,
    omanyte, omastar, kabuto, kabutops, aerodactyl, 
    snorlax, articuno, zapdos, moltres, dratini, dragonair, 
    dragonite, mewtwo, mew
    ]