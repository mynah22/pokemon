from clear import clear
from zones import zonelist
from menus import pMenu
def move(pl):
	#generate borders
	borderlist=[]
	idlist=[]
	for borderZone in zonelist[pl.zone].borders:
		borderlist.append(zonelist[borderZone].name)
		#map borders to IDs
		idlist.append(borderZone)	
	clear()

	print pl.name+' is in '+zonelist[pl.zone].name+'.'
	print 'move?'
 	inp=pMenu(['yes', 'no'])
 	if inp == 'no':
 		return
 	elif inp == 'yes':
 		clear()
 		pl.zone=idlist[borderlist.index(pMenu(borderlist))]
 	elif inp == 'Cancel':
 		return

