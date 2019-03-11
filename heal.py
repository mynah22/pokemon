from clear import clear
#from playsound import playsound
def heal(pl):
    for poke in pl.team:
        poke.hp = int(poke.stats.stats['hp'])
   # playsound('heal.mp3')
    xxx=raw_input('Pokemon healed!')