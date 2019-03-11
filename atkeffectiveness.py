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

effectiveness={
	'Bug':bugEffect, 'Dragon':dragonEffect, 'Electric':electricEffect,
	'Fighting':fightingEffect, 'Fire':fireEffect, 'Flying':flyingEffect,
	'Ghost':ghostEffect, 'Grass':grassEffect, 'Ground':groundEffect,
	'Ice':iceEffect, 'Normal':normalEffect, 'Poison':poisonEffect,
	'Psychic':psychicEffect, 'Rock':rockEffect, 'Water':waterEffect
	}

def calcEffect(self, skill, target):
	map=effectiveness[skill.type]
	effectList=[]
	for ptype in target.types:
		effectList.append(map[ptype])
	if len(effectList) == 1:
		if effectList[0] == 'none':
			return 0
		if effectList[0] == 'nve':
			return 5
		if effectList[0] == 'norm':
			return 10
		if effectList[0] == 'super':
			return 20
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
			return 0
		if score == -2:
			return 2.5
		if score == -1:
			return 5
		if score == 0:
			return 10
		if score == 1:
			return 20
		if score == 2:
			return 40
			