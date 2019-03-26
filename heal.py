from clear import clear
#from playsound import playsound
def heal(pl):
    for poke in pl.team:
        poke.hp = int(poke.stats.stats['hp'])
        #reset PP
        for move in poke.moveset:
            if poke.moveset[move]:
                poke.moveset[move].remainingUsagePoints = poke.moveset[move].maxUsagePoints
        #clear status ailments
        for status in poke.status:
            poke.status[status]=False
   # playsound('heal.mp3')
    xxx=raw_input('Pokemon healed!')