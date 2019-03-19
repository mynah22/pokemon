from math import sqrt
class statholder(object):
	def __init__(self):
		self.statNames=[
			'hp','speed','atk',
			'spAtk', 'def', 'spDef'
			]	
		self.ev={
			'hp':0,'speed':0 
			'atk':0,'def':0,
			'spAtk':0,'spDef':0,}
		self.iv={
			'hp':0,'speed':0 
			'atk':0,'def':0,
			'spAtk':0,'spDef':0,	
			}
		self.base={
			'hp':0,'speed':0 
			'atk':0,'def':0,
			'spAtk':0,'spDef':0,
			}
		self.stats={
			'hp':0,'speed':0 
			'atk':0,'def':0,
			'spAtk':0,'spDef':0,
			}
		self.atkstats={
			'hp':0,'speed':0 
			'atk':0,'def':0,
			'spAtk':0,'spDef':0,}
		self.combatStages={
			'hp':0,'speed':0 
			'atk':0,'def':0,
			'spAtk':0,'spDef':0,}
		self.faintxp=0	
		

	def calcstat(self, st, lvl):
		stat = self.base[st]
		stat += self.iv[st]
		stat = stat * 2
		stat += sqrt(self.ev[st])/4
		stat = stat * lvl
		stat = stat / 100.0
		stat += 5
		self.stats[st]= int(stat)
	def rj(self, x):
		for s in self.stats.statNames:
			self.stats.iv[s]=x
			if s=='hp':
				self.stats.calchp(a.self)
			else:
				self.stats.calcstat(s,a.self)
		print self.stats.stats
#		return ((((self.base[st]+self.iv[st])*2+(sqrt(self.ev[st])/4))*lvl)/100)+5

#	def calciv(self, level, stat, base, ev=0, p=1.0):
#		iv=math.ceil(stat/p)
#		iv= iv-5
#		iv= iv * (100.0/level)
#		iv = iv - (2*base)
#		iv = iv - (ev/4)
#		return iv

	def calchp(self,lvl):
		health = self.base['hp']
		health += self.iv['hp']
		health = health*2
		health += (sqrt(self.ev['hp']))/4
		health = health * lvl
		health = health / 100.0
		health = health + lvl +10
		self.stats['hp'] = int(health)

#	def calchpiv(level, stat, base, ev=0):
#		iv=stat
#		iv= iv-10
#		iv= iv * (100.0/level)
#		iv = iv - (2*base)
#		iv = iv - (ev/4)
#		return iv


	def reportcard(stats, bases):
		pass
		