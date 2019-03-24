from clear import clear
from menus import bankMenu, pMenu
def bank(pl):
    clear()
    done=False
    while not done:
        clear()
        mode=pMenu([
            'deposit', 'withdraw',
            'done'
            ])
        if mode=='deposit':
            clear()
            print 'Deposit Menu \n\n'
            choice=bankMenu(pl)
            pl.bank.append(choice)
            pl.team.remove(choice)
            clear()
            xxx=raw_input(choice.name+' deposited!')
        if mode=='withdraw':
            if len(pl.team)>5:
                print '\n\nyour party is full!'
                xxx=raw_input()
            else:
                clear()
                print 'Withdrawl Menu \n\n'
                choice=bankMenu(pl, 'w')
                pl.bank.remove(choice)
                pl.team.append(choice)
                clear()
                xxx=raw_input(choice.name+' withdrawn!')
        if mode=='done':
            done=True