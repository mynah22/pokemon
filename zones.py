class zone:
	def __init__(self):
		self.pokelist=[]
		self.minlvl=1
		self.maxlvl=12
PalletTown=zone()
#id 0
PalletTown.nullflag=1
PalletTown.name= 'Pallet Town'
PalletTown.borders=[1]

Route1=zone()
#id 1
#pokelist legend:[0]pokedex id [1]ecounter prob. [2] low lvl [3] high lvl
#
Route1.pokelist=[(16,55,2,5),(19,45,2,4)]
Route1.name= 'Route 1'
Route1.borders=[0,2]
Route1.nullflag=0

ViridianCity=zone()
#id 2
ViridianCity.nullflag=1
ViridianCity.name= 'Viridian City'
ViridianCity.borders=[1,3]

Route22=zone()
#id 3
Route22.pokelist=[(19,50,2,4),(21,10,2,6),(32,24,2,4),(29,15,2,4),(56,1,3,5)]
Route22.name= 'Route 22'
Route22.nullflag=0
Route22.borders=[2,4]

Route2=zone()
#id 4
Route2.pokelist=[(16,40,3,5),(19,45,2,5),(13,7,3,5),(10,8,3,5)]
Route2.name= 'Route 2'
Route2.nullflag=0
Route2.borders=[3,5]

ViridianForest=zone()
#id 5
ViridianForest.name= 'Viridian Forest'
ViridianForest.pokelist=[(10,5,3,3),(11,5,4,4),(13,50,3,3),(14,5,4,4),(25,5,3,5)]
ViridianForest.nullflag=0
ViridianForest.borders=[4,6]

PewterCity=zone()
#id 6
PewterCity.nullflag=1
PewterCity.name= 'Pewter City'
PewterCity.borders=[5,7]

Route3=zone()
#id 7
Route3.pokelist=[(16,50,6,8),(21,40,5,8),(39,10,3,7)]
Route3.name= 'Route 3'
Route3.nullflag=0
Route3.borders=[6,8]

MtMoon=zone()
#id 8
MtMoon.pokelist=[(41,79,6,11),(74,15,8,10),(46,5,8,8),(35,1,8,8)]
MtMoon.name='Mt.Moon'
MtMoon.nullflag=0
MtMoon.borders=[7,9]

MtMoonB1=zone()
#id 9
MtMoon1.pokelist=[(41,60,7,11),(74,26,7,9),(46,10,10,10),(35,4,9,9)]
MtMoonB1.name='Mt.Moon Basement 1'
MtMoonB1.nullflag=0
MtMoonB1.borders=[8,10]

MtMoonB2=zone()
#id 10
MtMoonB2.pokelist=[(41,54,9,12),(74,25,9,10),(46,15,10,12),(35,6,10,12)]
MtMoonB2.name='Mt.Moon Basement 2'
MtMoonB2.nullflag=0
MtMoonB2.borders=[9,11]

Route4=zone()
#id 11
Route4.pokelist=[(19,45,8,12),(21,30,8,12),(23,24,6,12),(27,1,6,12)]
Route4.name='Route 4'
Route4.nullflag=0
Route4.borders=[10]

CeruleanCity=zone()
#id 6
CeruleanCity.nullflag=1
CeruleanCity.name= 'Cerulean City'
PewterCity.borders=[5,7]


zonelist= [
	PalletTown,Route1,ViridianCity,
	Route22,Route2,ViridianForest,
	PewterCity,Route3,MtMoon,MtMoonB1,
	MtMoonB2,Route4,CeruleanCity
]

#PalletTown=[129,60,118,72]