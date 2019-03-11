from clear import clear

def load():
	choice = pMenu(os.listdir('/saves'))
	with open('saves/'+choice, 'r') as f:
		return pickle.loads(f.read())
