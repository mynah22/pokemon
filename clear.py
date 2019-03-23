import os

if os.name=='posix':
    def clear():
        os.system('clear')
else:
    def clear():
        os.system('cls')


