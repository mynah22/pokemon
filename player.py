class headedList(list):
    def head(self, pos=0):
        tmplis=[]
        tmplis.append(self.pop(pos))
        while self:
            tmplis.append(self.pop(0))
        for item in tmplis:
            self.append(item)

class player:
    def __init__(self, name='NAME'):
        self.name=name
        self.money=0
        self.team=headedList()
        self.balls={
            'pb':0,'gb':0, 
            'ub':0, 'mb':0
        }
        self.bank=[]
        self.zone=0
    def awakeList(self):
        awakePokes=[]
        for poke in self.team:
            if poke.hp>0:
                awakePokes.append(poke)
        return awakePokes

    def countawake(self):
    	return len(self.awakeList())