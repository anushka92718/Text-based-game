name=input('Enter Your Name: ')
print(f'Greeting {name}! Welcome to the tutorial!')
start=input('Would you rather play the game or die?')
if start == 'play':
    print("Great! Let's play the game!")
    setting = input('Want to go to the jungle or the desert? ')
else:
    print("Okay you are dead, good work....")
    quit()

if setting == 'jungle':
    print('Welcome to the mighty Amazon rainforest! Your tour guide told you to wait here.....')
    response=input('But he has been gone a long time..... Follow him or wait here? ')
    if response == 'follow':
        print('You follow him into the trees ......')
    elif response == 'wait':
        print('You wait another ten minutes, and he still isn\'t here!')
    else:
        print('invalid response! you lose! ')
        quit()

elif setting == 'desert':
    print("Welcome to the mighty Sahara Desert! Your tour guide told you to wait here.....")
    response=input("But he has been gone a long time .... Follow him or wait here?")
    if response == 'follow':
        print('You follow him into the dunes.... ')
    elif response == 'wait':
        print('You wait another ten minutes, and he still isn\'t here! ')
    else:
        print('invalid response! you lose!')
        quit()
    
else:
    print('invalid response! you lose!')
    quit()






