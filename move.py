from clear import clear
from zones import zonelist
from menus import pMenu
def move(pl):
	#generate borders
	borderlist=[]
	for borderZone in zonelist[pl.zone].borders:
		borderlist.append(zonelist[borderZone].name)
	clear()
	print pl.name+' is in '+zonelist[pl.zone].name+'.'
	print 'move?'
 	inp=pMenu(['yes', 'no'])
 	if inp == 'no':
 		return
 	elif inp == 'yes':
 		clear()

 		inp=pMenu(borderlist)
 		if inp == 'Pallet Town':
 			pl.zone=0
 		if inp =='Route 1':
 			pl.zone=1 		
 		if inp =='Viridian City':
 			pl.zone=2
 		if inp =='Route 22':
 			pl.zone=3
 		if inp =='Route 2':
 			pl.zone=4
 		if inp =='Viridian Forest':
 			pl.zone=5
 		if inp =='Pewter City':
 			pl.zone=6
 		if inp =='Route 3':
 			pl.zone=7
		if inp =='Mt.Moon':
 			pl.zone=8
 		if inp =='Mt.Moon Basement 1':
 			pl.zone=9
 		if inp =='Mt.Moon Basement 2':
 			pl.zone=10
 		if inp =='Route 4':
 			pl.zone=11


 		elif inp == 'Cancel':
 			return

