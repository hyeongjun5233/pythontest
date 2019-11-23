def attack():
    select=int(input(''))

    if(select==1):
        print('KICK')
    elif(select==2):
        print('FIST')
    elif(select==3):
        print('AVOID')
    elif(select==4):
        print('FAKE')
    elif(select==5):
        print('HI')
    else:
        print('Wrong INPUT. Try again.')
    print('')

power=5
print('Attack Game')
print('1. KICK')
print('2. FIST')
print('3. AVOID')
print('4. FAKE')
print('5. HI')
print('0. EXIT\n')

while(1):
    attack()
    

print('Exit the game. Thanks for playing.')
