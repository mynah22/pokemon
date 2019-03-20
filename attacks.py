from roll import rrang, roll
from atkeffectiveness import calcEffect 
bugEffect={
	'Bug':'norm', 'Dragon':'norm', 'Electric':'norm',
	'Fighting':'norm', 'Fire':'nve', 'Flying':'nve',
	'Ghost':'norm', 'Grass':'super', 'Ground':'norm',
	'Ice':'norm', 'Normal':'norm', 'Poison': 'super',
	'Psychic':'super', 'Rock':'nve', 'Water':'norm'
}
dragonEffect={
	'Bug':'norm', 'Dragon':'norm', 'Electric':'norm',
	'Fighting':'norm', 'Fire':'norm', 'Flying':'norm',
	'Ghost':'norm', 'Grass':'norm', 'Ground':'norm',
	'Ice':'norm', 'Normal':'norm', 'Poison': 'norm',
	'Psychic':'norm', 'Rock':'norm', 'Water':'norm'
}
electricEffect={
	'Bug':'norm', 'Dragon':'norm', 'Electric':'nve',
	'Fighting':'norm', 'Fire':'norm', 'Flying':'super',
	'Ghost':'norm', 'Grass':'nve', 'Ground':'none',
	'Ice':'norm', 'Normal':'norm', 'Poison': 'norm',
	'Psychic':'norm', 'Rock':'norm', 'Water':'super'
}
fightingEffect={
	'Bug':'norm', 'Dragon':'norm', 'Electric':'norm',
	'Fighting':'norm', 'Fire':'norm', 'Flying':'nve',
	'Ghost':'none', 'Grass':'norm', 'Ground':'norm',
	'Ice':'super', 'Normal':'super', 'Poison': 'norm',
	'Psychic':'nve', 'Rock':'super', 'Water':'norm'
}
fireEffect={
	'Bug':'super', 'Dragon':'norm', 'Electric':'norm',
	'Fighting':'norm', 'Fire':'norm', 'Flying':'norm',
	'Ghost':'norm', 'Grass':'super', 'Ground':'super',
	'Ice':'super', 'Normal':'norm', 'Poison': 'norm',
	'Psychic':'norm', 'Rock':'nve', 'Water':'nve'
}
flyingEffect={
	'Bug':'super', 'Dragon':'norm', 'Electric':'nve',
	'Fighting':'super', 'Fire':'norm', 'Flying':'norm',
	'Ghost':'norm', 'Grass':'super', 'Ground':'norm',
	'Ice':'norm', 'Normal':'norm', 'Poison': 'norm',
	'Psychic':'norm', 'Rock':'nve', 'Water':'norm'
}
ghostEffect={
	'Bug':'norm', 'Dragon':'norm', 'Electric':'norm',
	'Fighting':'norm', 'Fire':'norm', 'Flying':'norm',
	'Ghost':'norm', 'Grass':'norm', 'Ground':'norm',
	'Ice':'norm', 'Normal':'none', 'Poison': 'norm',
	'Psychic':'none', 'Rock':'norm', 'Water':'norm'
}
grassEffect={
	'Bug':'nve', 'Dragon':'norm', 'Electric':'norm',
	'Fighting':'norm', 'Fire':'nve', 'Flying':'nve',
	'Ghost':'norm', 'Grass':'nve', 'Ground':'super',
	'Ice':'norm', 'Normal':'norm', 'Poison': 'nve',
	'Psychic':'norm', 'Rock':'super', 'Water':'super'
}
groundEffect={
	'Bug':'norm', 'Dragon':'norm', 'Electric':'super',
	'Fighting':'norm', 'Fire':'super', 'Flying':'none',
	'Ghost':'norm', 'Grass':'nve', 'Ground':'norm',
	'Ice':'norm', 'Normal':'norm', 'Poison': 'super',
	'Psychic':'norm', 'Rock':'super', 'Water':'norm'
}
iceEffect={
	'Bug':'norm', 'Dragon':'super', 'Electric':'norm',
	'Fighting':'norm', 'Fire':'norm', 'Flying':'super',
	'Ghost':'norm', 'Grass':'super', 'Ground':'super',
	'Ice':'nve', 'Normal':'norm', 'Poison': 'norm',
	'Psychic':'norm', 'Rock':'norm', 'Water':'nve'
}
normalEffect={
	'Bug':'norm', 'Dragon':'norm', 'Electric':'norm',
	'Fighting':'norm', 'Fire':'norm', 'Flying':'norm',
	'Ghost':'none', 'Grass':'norm', 'Ground':'norm',
	'Ice':'norm', 'Normal':'norm', 'Poison': 'norm',
	'Psychic':'norm', 'Rock':'norm', 'Water':'norm'
}
poisonEffect={
	'Bug':'super', 'Dragon':'norm', 'Electric':'norm',
	'Fighting':'norm', 'Fire':'norm', 'Flying':'norm',
	'Ghost':'norm', 'Grass':'super', 'Ground':'nve',
	'Ice':'norm', 'Normal':'norm', 'Poison': 'nve',
	'Psychic':'norm', 'Rock':'nve', 'Water':'norm'
}
psychicEffect={
	'Bug':'norm', 'Dragon':'norm', 'Electric':'norm',
	'Fighting':'super', 'Fire':'norm', 'Flying':'norm',
	'Ghost':'norm', 'Grass':'norm', 'Ground':'norm',
	'Ice':'norm', 'Normal':'norm', 'Poison': 'super',
	'Psychic':'nve', 'Rock':'norm', 'Water':'norm'
}
rockEffect={
	'Bug':'super', 'Dragon':'norm', 'Electric':'norm',
	'Fighting':'nve', 'Fire':'super', 'Flying':'super',
	'Ghost':'norm', 'Grass':'norm', 'Ground':'norm',
	'Ice':'super', 'Normal':'norm', 'Poison': 'norm',
	'Psychic':'norm', 'Rock':'nve', 'Water':'norm'
}
waterEffect={
	'Bug':'norm', 'Dragon':'norm', 'Electric':'norm',
	'Fighting':'norm', 'Fire':'super', 'Flying':'norm',
	'Ghost':'norm', 'Grass':'nve', 'Ground':'super',
	'Ice':'nve', 'Normal':'norm', 'Poison': 'norm',
	'Psychic':'norm', 'Rock':'super', 'Water':'norm'
}
noneEffect={
	'Bug':'norm', 'Dragon':'norm', 'Electric':'norm',
	'Fighting':'norm', 'Fire':'norm', 'Flying':'norm',
	'Ghost':'norm', 'Grass':'norm', 'Ground':'norm',
	'Ice':'norm', 'Normal':'norm', 'Poison': 'norm',
	'Psychic':'norm', 'Rock':'normr', 'Water':'norm'
}
effectiveness={
	'Bug':bugEffect, 'Dragon':dragonEffect, 'Electric':electricEffect,
	'Fighting':fightingEffect, 'Fire':fireEffect, 'Flying':flyingEffect,
	'Ghost':ghostEffect, 'Grass':grassEffect, 'Ground':groundEffect,
	'Ice':iceEffect, 'Normal':normalEffect, 'Poison':poisonEffect,
	'Psychic':psychicEffect, 'Rock':rockEffect, 'Water':waterEffect,
	'None':noneEffect
}

class attack:
	def __init__(self):
		self.type=[]
		self.accuracy=80
		self.maxUsagePoints=10 #power points on serebii
		self.baseDamage=20  #base power on serebii
		self.specFlag=0 #special attack flag (kenetic=0, special=1, calculated=2)
		self.speedPriority=0
	
	def calcDamage(self, user, target):
		#calc critFlag
		if rrang(0,255)<user.stats.base['speed']/2:
			lvlWithCritMod=user.level*2
		else:
			lvlWithCritMod=user.level
		#calc sameTypeMod
		if user.types.count(self.type):
			sameTypeMod=1.5
		else:
			sameTypeMod=1
		#calc typeMod
		eMap=effectiveness[self.type]
		effectList=[]
		for ptype in target.types:
			effectList.append(eMap[ptype])
		if len(effectList) == 1:
			if effectList[0] == 'none':
				typeMod = 0
			if effectList[0] == 'nve':
				typeMod = 5
			if effectList[0] == 'norm':
				typeMod = 10
			if effectList[0] == 'super':
				typeMod = 20
		else:
			score=0
			for effect in effectList:
				if effect == 'none':
					score -=5
				if effect == 'nve':
					score -=1
				if effect == 'norm':
					pass
				if effect == 'super':
					score +=1
			if score < -2:
				typeMod = 0
			if score == -2:
				typeMod = 2.5
			if score == -1:
				typeMod = 5
			if score == 0:
				typeMod = 10
			if score == 1:
				typeMod = 20
			if score == 2:
				typeMod = 40
		if self.specflag==0:
			dmg=0.0
			dmg=int(2*lvlWithCritMod)
			dmg=int(dmg/5.0+2)
			dmg=int((dmg+0.0)*user.stats.stats['atk']*user.statStageCoefficient(user.stats.combatStages['atk']))
			dmg=int((dmg+0.0)*self.baseDamage)
			dmg=int((dmg+0.0)/(target.stats.stats['def']*target.statStageCoefficient(target.stats.combatStages['def'])))
			dmg=int(dmg/50.0)
			dmg=int(dmg+2.0)
			dmg=int((dmg+0.0)*sameTypeMod)
			dmg=int(((dmg+0.0)*typeMod)/10)
			dmg=int((dmg+0.0)*(rrang(217,255)/255.0))		
		elif self.specFlag==1:
			dmg=0.0
			dmg=int(2*lvlWithCritMod)
			dmg=int(dmg/5.0+2)
			dmg=int((dmg+0.0)*user.stats.stats['spAtk']*user.statStageCoefficient(user.stats.combatStages['spAtk']))
			dmg=int((dmg+0.0)*self.baseDamage)
			dmg=int((dmg+0.0)/(target.stats.stats['spDef']*target.statStageCoefficient(target.stats.combatStages['spDef'])))
			dmg=int(dmg/50.0)
			dmg=int(dmg+2.0)
			dmg=int((dmg+0.0)*sameTypeMod)
			dmg=int(((dmg+0.0)*typeMod)/10)
			dmg=int((dmg+0.0)*(rrang(217,255)/255.0))
		return dmg

class absorb(attack):
	def __init__(self):
	#	super(self.__class__, self).__init__()
		self.atkid=0
		self.type='Grass'
		self.name='Absorb'
		self.remainingUsagePoints=20
		self.maxUsagePoints=20
		self.baseDamage=20
		self.specFlag=0
		self.accuracy=100
		self.speedPriority=0
	def cast(self, user, target):
		dmg = self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			user.hp+=(dmg/2)
			return 1
		else:
			return 0
			
class Acid(attack):
	def __init__(self):
		self.atkId=1
		self.type='Normal'
		self.name='Acid'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
	def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class AcidArmor(attack):
    def __init__(self):
		self.atkId=2
		self.type='Normal'
		self.name='AcidArmor'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Agility(attack):
    def __init__(self):
		self.atkId=3
		self.type='Normal'
		self.name='Agility'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Amnesia(attack):
    def __init__(self):
		self.atkId=4
		self.type='Normal'
		self.name='Amnesia'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Aurrorabeam(attack):
    def __init__(self):
		self.atkId=5
		self.type='Normal'
		self.name='Aurrorabeam'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Barrage(attack):
    def __init__(self):
		self.atkId=6
		self.type='Normal'
		self.name='Barrage'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Barrier(attack):
    def __init__(self):
		self.atkId=7
		self.type='Normal'
		self.name='Barrier'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Bide(attack):
    def __init__(self):
		self.atkId=8
		self.type='Normal'
		self.name='Bide'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Bind(attack):
    def __init__(self):
		self.atkId=9
		self.type='Normal'
		self.name='Bind'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Bite(attack):
    def __init__(self):
		self.atkId=10
		self.type='Normal'
		self.name='Bite'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Blizzard(attack):
    def __init__(self):
		self.atkId=11
		self.type='Normal'
		self.name='Blizzard'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Bodyslam(attack):
    def __init__(self):
		self.atkId=12
		self.type='Normal'
		self.name='Bodyslam'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class BoneClub(attack):
    def __init__(self):
		self.atkId=13
		self.type='Normal'
		self.name='BoneClub'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Bonemerang(attack):
    def __init__(self):
		self.atkId=14
		self.type='Normal'
		self.name='Bonemerang'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Bubble(attack):
    def __init__(self):
		self.atkId=15
		self.type='Normal'
		self.name='Bubble'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Bubblebeam(attack):
    def __init__(self):
		self.atkId=16
		self.type='Normal'
		self.name='Bubblebeam'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Clamp(attack):
    def __init__(self):
		self.atkId=17
		self.type='Normal'
		self.name='Clamp'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Cometpunch(attack):
    def __init__(self):
		self.atkId=18
		self.type='Normal'
		self.name='Cometpunch'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Confuseray(attack):
    def __init__(self):
		self.atkId=19
		self.type='Normal'
		self.name='Confuseray'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Confusion(attack):
    def __init__(self):
		self.atkId=20
		self.type='Normal'
		self.name='Confusion'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Constrict(attack):
    def __init__(self):
		self.atkId=21
		self.type='Normal'
		self.name='Constrict'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Conversion(attack):
    def __init__(self):
		self.atkId=22
		self.type='Normal'
		self.name='Conversion'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Counter(attack):
    def __init__(self):
		self.atkId=23
		self.type='Normal'
		self.name='Counter'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.speedPriority=-1
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Crabhammer(attack):
    def __init__(self):
		self.atkId=24
		self.type='Normal'
		self.name='Crabhammer'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Cut(attack):
    def __init__(self):
		self.atkId=25
		self.type='Normal'
		self.name='Cut'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class DefenseCurl(attack):
    def __init__(self):
		self.atkId=26
		self.type='Normal'
		self.name='DefenseCurl'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Dig(attack):
    def __init__(self):
		self.atkId=27
		self.type='Normal'
		self.name='Dig'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Disable(attack):
    def __init__(self):
		self.atkId=28
		self.type='Normal'
		self.name='Disable'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class DizzyPunch(attack):
    def __init__(self):
		self.atkId=29
		self.type='Normal'
		self.name='DizzyPunch'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class DoubleEdge(attack):
    def __init__(self):
		self.atkId=30
		self.type='Normal'
		self.name='Double-edge'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Doublekick(attack):
    def __init__(self):
		self.atkId=31
		self.type='Normal'
		self.name='Doublekick'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Doubleslap(attack):
    def __init__(self):
		self.atkId=32
		self.type='Normal'
		self.name='Doubleslap'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Doubleteam(attack):
    def __init__(self):
		self.atkId=33
		self.type='Normal'
		self.name='Doubleteam'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class DragonRage(attack):
    def __init__(self):
		self.atkId=34
		self.type='Normal'
		self.name='Dragon Rage'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class DreamEater(attack):
    def __init__(self):
		self.atkId=35
		self.type='Normal'
		self.name='DreamEater'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class DrillPeck(attack):
    def __init__(self):
		self.atkId=36
		self.type='Normal'
		self.name='DrillPeck'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class EarthQuake(attack):
    def __init__(self):
		self.atkId=37
		self.type='Normal'
		self.name='EarthQuake'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class EggBomb(attack):
    def __init__(self):
		self.atkId=38
		self.type='Normal'
		self.name='EggBomb'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Ember(attack):
    def __init__(self):
		self.atkId=39
		self.type='Normal'
		self.name='Ember'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Explosion(attack):
    def __init__(self):
		self.atkId=40
		self.type='Normal'
		self.name='Explosion'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Fireblast(attack):
    def __init__(self):
		self.atkId=41
		self.type='Normal'
		self.name='Fireblast'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Firepunch(attack):
    def __init__(self):
		self.atkId=42
		self.type='Normal'
		self.name='Firepunch'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Firespin(attack):
    def __init__(self):
		self.atkId=43
		self.type='Normal'
		self.name='Firespin'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Fissure(attack):
    def __init__(self):
		self.atkId=44
		self.type='Normal'
		self.name='Fissure'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Flamethrower(attack):
    def __init__(self):
		self.atkId=45
		self.type='Normal'
		self.name='Flamethrower'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Flash(attack):
    def __init__(self):
		self.atkId=46
		self.type='Normal'
		self.name='Flash'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Fly(attack):
    def __init__(self):
		self.atkId=47
		self.type='Normal'
		self.name='Fly'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class FocusEnergy(attack):
    def __init__(self):
		self.atkId=48
		self.type='Normal'
		self.name='FocusEnergy'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class FuryAttack(attack):
    def __init__(self):
		self.atkId=49
		self.type='Normal'
		self.name='FuryAttack'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class FurySwipes(attack):
    def __init__(self):
		self.atkId=50
		self.type='Normal'
		self.name='FurySwipes'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Glare(attack):
    def __init__(self):
		self.atkId=51
		self.type='Normal'
		self.name='Glare'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Growl(attack):
    def __init__(self):
		self.atkId=52
		self.type='Normal'
		self.name='Growl'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			if user.stats.combatStages['atk'] < 6:
				user.stats.combatStages['atk'] += 1
				return 1
			else:
				return 0
		else:
			return 0
class Growth(attack):
    def __init__(self):
		self.atkId=53
		self.type='Normal'
		self.name='Growth'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Guillotine(attack):
    def __init__(self):
		self.atkId=54
		self.type='Normal'
		self.name='Guillotine'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Gust(attack):
    def __init__(self):
		self.atkId=55
		self.type='Flying'
		self.name='Gust'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=40
		self.accuracy=100
		self.specflag=0
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Harden(attack):
    def __init__(self):
		self.atkId=56
		self.type='Normal'
		self.name='Harden'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Haze(attack):
    def __init__(self):
		self.atkId=57
		self.type='Normal'
		self.name='Haze'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class HEadbutt(attack):
    def __init__(self):
		self.atkId=58
		self.type='Normal'
		self.name='HEadbutt'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class HiJumpKick(attack):
    def __init__(self):
		self.atkId=59
		self.type='Normal'
		self.name='HiJumpKick'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class HornAttack(attack):
    def __init__(self):
		self.atkId=60
		self.type='Normal'
		self.name='HornAttack'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class HornDrill(attack):
    def __init__(self):
		self.atkId=61
		self.type='Normal'
		self.name='HornDrill'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Hydropump(attack):
    def __init__(self):
		self.atkId=62
		self.type='Normal'
		self.name='Hydropump'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Hyperbeam(attack):
    def __init__(self):
		self.atkId=63
		self.type='Normal'
		self.name='Hyperbeam'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Hyperfang(attack):
    def __init__(self):
		self.atkId=64
		self.type='Normal'
		self.name='Hyper Fang'
		self.remainingUsagePoints=15
		self.maxUsagePoints=15
		self.baseDamage=80
		self.accuracy=90
		self.specflag=0
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Hypnosis(attack):
    def __init__(self):
		self.atkId=65
		self.type='Normal'
		self.name='Hypnosis'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Icebeam(attack):
    def __init__(self):
		self.atkId=66
		self.type='Normal'
		self.name='Icebeam'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Icepunch(attack):
    def __init__(self):
		self.atkId=67
		self.type='Normal'
		self.name='Icepunch'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Jumpkick(attack):
    def __init__(self):
		self.atkId=68
		self.type='Normal'
		self.name='Jumpkick'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Karatechop(attack):
    def __init__(self):
		self.atkId=69
		self.type='Normal'
		self.name='Karatechop'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Kinesis(attack):
    def __init__(self):
		self.atkId=70
		self.type='Normal'
		self.name='Kinesis'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Leechlife(attack):
    def __init__(self):
		self.atkId=71
		self.type='Normal'
		self.name='Leechlife'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Leechseed(attack):
    def __init__(self):
		self.atkId=72
		self.type='Normal'
		self.name='Leechseed'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class leer(attack):
    def __init__(self):
		self.atkId=73
		self.type='Normal'
		self.name='leer'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Lick(attack):
    def __init__(self):
		self.atkId=74
		self.type='Normal'
		self.name='Lick'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Lightscreen(attack):
    def __init__(self):
		self.atkId=75
		self.type='Normal'
		self.name='Lightscreen'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class LovelyKiss(attack):
    def __init__(self):
		self.atkId=76
		self.type='Normal'
		self.name='LovelyKiss'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class LowKick(attack):
    def __init__(self):
		self.atkId=77
		self.type='Normal'
		self.name='LowKick'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Meditate(attack):
    def __init__(self):
		self.atkId=78
		self.type='Normal'
		self.name='Meditate'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class MegaDrain(attack):
    def __init__(self):
		self.atkId=79
		self.type='Normal'
		self.name='MegaDrain'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Megakick(attack):
    def __init__(self):
		self.atkId=80
		self.type='Normal'
		self.name='Megakick'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class MegaPunch(attack):
    def __init__(self):
		self.atkId=81
		self.type='Normal'
		self.name='MegaPunch'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Metronome(attack):
    def __init__(self):
		self.atkId=82
		self.type='Normal'
		self.name='Metronome'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Mimic(attack):
    def __init__(self):
		self.atkId=83
		self.type='Normal'
		self.name='Mimic'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Minimize(attack):
    def __init__(self):
		self.atkId=84
		self.type='Normal'
		self.name='Minimize'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Mirrormove(attack):
    def __init__(self):
		self.atkId=85
		self.type='Normal'
		self.name='Mirrormove'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Mist(attack):
    def __init__(self):
		self.atkId=86
		self.type='Normal'
		self.name='Mist'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Nightshade(attack):
    def __init__(self):
		self.atkId=87
		self.type='Normal'
		self.name='Nightshade'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Payday(attack):
    def __init__(self):
		self.atkId=88
		self.type='Normal'
		self.name='Payday'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class PEck(attack):
    def __init__(self):
		self.atkId=89
		self.type='Normal'
		self.name='PEck'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class PEtaldance(attack):
    def __init__(self):
		self.atkId=90
		self.type='Normal'
		self.name='PEtaldance'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Pinmissile(attack):
    def __init__(self):
		self.atkId=91
		self.type='Normal'
		self.name='Pinmissile'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class PoisonGas(attack):
    def __init__(self):
		self.atkId=92
		self.type='Normal'
		self.name='PoisonGas'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Poisonpowder(attack):
    def __init__(self):
		self.atkId=93
		self.type='Normal'
		self.name='Poisonpowder'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class PoisonSting(attack):
    def __init__(self):
		self.atkId=94
		self.type='Normal'
		self.name='Posion Sitng'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Pound(attack):
    def __init__(self):
		self.atkId=95
		self.type='Normal'
		self.name='Pound'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Psybeam(attack):
    def __init__(self):
		self.atkId=96
		self.type='Normal'
		self.name='Psybeam'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Psychic(attack):
    def __init__(self):
		self.atkId=97
		self.type='Normal'
		self.name='Psychic'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Psywave(attack):
    def __init__(self):
		self.atkId=98
		self.type='Normal'
		self.name='Psywave'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Quickattack(attack):
    def __init__(self):
		self.atkId=99
		self.type='Normal'
		self.name='Quickattack'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
		self.speedPriority=1
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Rage(attack):
    def __init__(self):
		self.atkId=100
		self.type='Normal'
		self.name='Rae'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Razorleaf(attack):
    def __init__(self):
		self.atkId=101
		self.type='Normal'
		self.name='Razorleaf'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Razoewind(attack):
    def __init__(self):
		self.atkId=102
		self.type='Normal'
		self.name='Razoewind'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Recover(attack):
    def __init__(self):
		self.atkId=103
		self.type='Normal'
		self.name='Recover'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Reflect(attack):
    def __init__(self):
		self.atkId=104
		self.type='Normal'
		self.name='Reflect'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class rest(attack):
    def __init__(self):
		self.atkId=105
		self.type='Normal'
		self.name='rest'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Roar(attack):
    def __init__(self):
		self.atkId=106
		self.type='Normal'
		self.name='Roar'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Rockslide(attack):
    def __init__(self):
		self.atkId=107
		self.type='Normal'
		self.name='Rockslide'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Rockthrow(attack):
    def __init__(self):
		self.atkId=108
		self.type='Normal'
		self.name='Rockthrow'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class RollingKick(attack):
    def __init__(self):
		self.atkId=109
		self.type='Normal'
		self.name='RollingKick'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class SandAttack(attack):
    def __init__(self):
		self.atkId=110
		self.type='Normal'
		self.name='SandAttack'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Scratch(attack):
    def __init__(self):
		self.atkId=111
		self.type='Normal'
		self.name='Scratch'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Screech(attack):
    def __init__(self):
		self.atkId=112
		self.type='Normal'
		self.name='Screech'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class SeismicToss(attack):
    def __init__(self):
		self.atkId=113
		self.type='Normal'
		self.name='SeismicToss'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class SelfDestruct(attack):
    def __init__(self):
		self.atkId=114
		self.type='Normal'
		self.name='SelfDestruct'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Sharpen(attack):
    def __init__(self):
		self.atkId=115
		self.type='Normal'
		self.name='Sharpen'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Sing(attack):
    def __init__(self):
		self.atkId=116
		self.type='Normal'
		self.name='Sing'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Skllbash(attack):
    def __init__(self):
		self.atkId=117
		self.type='Normal'
		self.name='Skllbash'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class SkyAttack(attack):
    def __init__(self):
		self.atkId=118
		self.type='Normal'
		self.name='SkyAttack'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Slam(attack):
    def __init__(self):
		self.atkId=119
		self.type='Normal'
		self.name='Slam'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Slash(attack):
    def __init__(self):
		self.atkId=120
		self.type='Normal'
		self.name='Slash'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Sleeppowder(attack):
    def __init__(self):
		self.atkId=121
		self.type='Normal'
		self.name='Sleeppowder'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Sludge(attack):
    def __init__(self):
		self.atkId=122
		self.type='Normal'
		self.name='Sludge'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Smog(attack):
    def __init__(self):
		self.atkId=123
		self.type='Normal'
		self.name='Smog'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class SmokeScreen(attack):
    def __init__(self):
		self.atkId=124
		self.type='Normal'
		self.name='SmokeScreen'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class SoftBoiled(attack):
    def __init__(self):
		self.atkId=125
		self.type='Normal'
		self.name='SoftBoiled'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class SolarBeam(attack):
    def __init__(self):
		self.atkId=126
		self.type='Normal'
		self.name='SolarBeam'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class SonicBoom(attack):
    def __init__(self):
		self.atkId=127
		self.type='Normal'
		self.name='SonicBoom'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class SpikeCannon(attack):
    def __init__(self):
		self.atkId=128
		self.type='Normal'
		self.name='SpikeCannon'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Splash(attack):
    def __init__(self):
		self.atkId=129
		self.type='Normal'
		self.name='Splash'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Spore(attack):
    def __init__(self):
		self.atkId=130
		self.type='Normal'
		self.name='Spore'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Stomp(attack):
    def __init__(self):
		self.atkId=131
		self.type='Normal'
		self.name='Stomp'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Strength(attack):
    def __init__(self):
		self.atkId=132
		self.type='Normal'
		self.name='Strength'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Stringshot(attack):
    def __init__(self):
		self.atkId=133
		self.type='Normal'
		self.name='Stringshot'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Struggle(attack):
    def __init__(self):
		self.atkId=134
		self.type='Normal'
		self.name='Struggle'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class StunSpore(attack):
    def __init__(self):
		self.atkId=135
		self.type='Normal'
		self.name='StunSpore'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Submission(attack):
    def __init__(self):
		self.atkId=136
		self.type='Normal'
		self.name='Submission'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Substitute(attack):
    def __init__(self):
		self.atkId=137
		self.type='Normal'
		self.name='Substitute'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Superfang(attack):
    def __init__(self):
		self.atkId=138
		self.type='Normal'
		self.name='Super Fang'
		self.remainingUsagePoints=10
		self.maxUsagePoints=10
		self.baseDamage=1
		self.accuracy=90
		self.specflag=0
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp=target.hp/2
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Supersonic(attack):
    def __init__(self):
		self.atkId=139
		self.type='Normal'
		self.name='Supersonic'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Surf(attack):
    def __init__(self):
		self.atkId=140
		self.type='Normal'
		self.name='Surf'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Swift(attack):
    def __init__(self):
		self.atkId=141
		self.type='Normal'
		self.name='Swift'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class SwordsDancw(attack):
    def __init__(self):
		self.atkId=142
		self.type='Normal'
		self.name='SwordsDancw'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Tackle(attack):
    def __init__(self):
		self.atkId=143
		self.type='Normal'
		self.name='Tackle'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Tailwhip(attack):
    def __init__(self):
		self.atkId=144
		self.type='Normal'
		self.name='Tailwhip'
		self.remainingUsagePoints=30
		self.maxUsagePoints=30
		self.baseDamage=0
		self.accuracy=100
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			if target.stats.combatStages['def'] > -6:
				target.stats.combatStages['def'] -= 1
				return 1
			else:
				return 0
		else:
			return 0
class Takedown(attack):
    def __init__(self):
		self.atkId=145
		self.type='Normal'
		self.name='Takedown'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Teleport(attack):
    def __init__(self):
		self.atkId=146
		self.type='Normal'
		self.name='Teleport'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Thrash(attack):
    def __init__(self):
		self.atkId=147
		self.type='Normal'
		self.name='Thrash'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Thunder(attack):
    def __init__(self):
		self.atkId=148
		self.type='Electric'
		self.name='Thunder'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Thunderbolt(attack):
    def __init__(self):
		self.atkId=149
		self.type='Normal'
		self.name='Thunderbolt'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Thunderpunch(attack):
    def __init__(self):
		self.atkId=150
		self.type='Normal'
		self.name='Thunderpunch'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class ThunderShick(attack):
    def __init__(self):
		self.atkId=151
		self.type='Normal'
		self.name='ThunderShick'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class ThunderWave(attack):
    def __init__(self):
		self.atkId=152
		self.type='Normal'
		self.name='ThunderWave'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Toxic(attack):
    def __init__(self):
		self.atkId=153
		self.type='Normal'
		self.name='Toxic'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Transform(attack):
    def __init__(self):
		self.atkId=154
		self.type='Normal'
		self.name='Transform'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class TriAttack(attack):
    def __init__(self):
		self.atkId=155
		self.type='Normal'
		self.name='TriAttack'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Twineedle(attack):
    def __init__(self):
		self.atkId=156
		self.type='Normal'
		self.name='Twineedle'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Vicegrip(attack):
    def __init__(self):
		self.atkId=157
		self.type='Normal'
		self.name='Vicegrip'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class VineWhip(attack):
    def __init__(self):
		self.atkId=158
		self.type='Normal'
		self.name='VineWhip'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Waterfall(attack):
    def __init__(self):
		self.atkId=159
		self.type='Normal'
		self.name='Waterfall'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Watergun(attack):
    def __init__(self):
		self.atkId=160
		self.type='Normal'
		self.name='Watergun'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Whirlwind(attack):
    def __init__(self):
		self.atkId=161
		self.type='Normal'
		self.name='Whirlwind'
		self.remainingUsagePoints=20
		self.maxUsagePoints=20
		self.baseDamage=0
		self.accuracy=85
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class WingAttack(attack):
    def __init__(self):
		self.atkId=162
		self.type='Flying'
		self.name='WingAttack'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=100
		self.specflag=0
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class WithDraw(attack):
    def __init__(self):
		self.atkId=163
		self.type='Normal'
		self.name='WithDraw'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0
class Wrap(attack):
    def __init__(self):
		self.atkId=164
		self.type='Normal'
		self.name='Wrap'
		self.remainingUsagePoints=35
		self.maxUsagePoints=35
		self.baseDamage=35
		self.accuracy=95
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			self.remainingUsagePoints-=1
			return 1
		else:
			return 0

class Struggle(attack):
    def __init__(self):
		self.atkId=165
		self.type='None'
		self.name='Struggle'
		self.remainingUsagePoints=1
		self.maxUsagePoints=1
		self.baseDamage=50
		self.accuracy=100
		self.specflag=0
		self.incomplete=1 #finish
		self.speedPriority=0
    def cast(self, user, target):
		dmg=self.calcDamage(user, target)
		if roll(self.accuracy):
			target.hp-=dmg
			user.hp-=dmg/4
			return 1
		else:
			return 0



attackClasses=[
	absorb,Acid,AcidArmor,Agility,Amnesia,
	Aurrorabeam,Barrage,Barrier,Bide,Bind,
	Bite,Blizzard,Bodyslam,BoneClub,
	Bonemerang,Bubble,Bubblebeam,Clamp,
	Cometpunch,Confuseray,Confusion,
	Constrict,Conversion,Counter,
	Crabhammer,Cut,DefenseCurl,Dig,
	Disable,DizzyPunch,DoubleEdge,
	Doublekick,Doubleslap,Doubleteam,
	DragonRage,DreamEater,DrillPeck,
	EarthQuake,EggBomb,Ember,Explosion,
	Fireblast,Firepunch,Firespin,Fissure,
	Flamethrower,Flash,Fly,FocusEnergy,
	FuryAttack,FurySwipes,Glare,Growl,
	Growth,Guillotine,Gust,Harden,Haze,
	HEadbutt,HiJumpKick,HornAttack,HornDrill,
	Hydropump,Hyperbeam,Hyperfang,
	Hypnosis,Icebeam,Icepunch,Jumpkick,
	Karatechop,Kinesis,Leechlife,Leechseed,
	leer,Lick,Lightscreen,LovelyKiss,
	LowKick,Meditate,MegaDrain,Megakick,
	MegaPunch,Metronome,Mimic,Minimize,
	Mirrormove,Mist,Nightshade,Payday,
	PEck,PEtaldance,Pinmissile,PoisonGas,
	Poisonpowder,PoisonSting,Pound,
	Psybeam,Psychic,Psywave,Quickattack,
	Rage,Razorleaf,Razoewind,Recover,Reflect,
	rest,Roar,Rockslide,Rockthrow,RollingKick,
	SandAttack,Scratch,Screech,SeismicToss,
	SelfDestruct,Sharpen,Sing,Skllbash,SkyAttack,
	Slam,Slash,Sleeppowder,Sludge,Smog,
	SmokeScreen,SoftBoiled,SolarBeam,
	SonicBoom,SpikeCannon,Splash,Spore,
	Stomp,Strength,Stringshot,Struggle,
	StunSpore,Submission,Substitute,Superfang,
	Supersonic,Surf,Swift,SwordsDancw,
	Tackle,Tailwhip,Takedown,Teleport,
	Thrash,Thunder,Thunderbolt,Thunderpunch,
	ThunderShick,ThunderWave,Toxic,Transform,
	TriAttack,Twineedle,Vicegrip,VineWhip,
	Waterfall,Watergun,Whirlwind,WingAttack,
	WithDraw,Wrap,

]

