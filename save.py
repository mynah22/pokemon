from clear import clear
import pickle
import os.path 
from os import listdir
from menus import pMenu

def save(pl):
    if os.path.exists('saves/'+pl.name):
        pass #add overwrite check
    fullp='saves/'+pl.name
    with open(fullp, 'w+') as f:
       f.write(pickle.dumps(pl))   
    print 'game saved.'
    xxx=raw_input()

def load():
	choice = pMenu(listdir('saves/'))
	with open('saves/'+choice, 'r') as f:
		return pickle.loads(f.read())
