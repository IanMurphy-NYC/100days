print('Welcome to Treasure Island. Your mission is to find the treasure.')

choice1 = input('left or right? ')

if choice1 != 'left':
    print('Fall into a hole. Game Over.')
else:
    choice2 = input('swim or wait? ')

    if choice2 != 'wait':
        print('Attacked by trout. Game Over.')

    else:
        choice3 = input('Which door? ')

        if choice3 == 'Blue':
            print('Eaten by beasts. Game Over.')

        elif choice3 == 'Yellow':
            print('You Win!')

        elif choice3 == 'Red':
            print('Burned by fire. Game Over.')

        else:
            print('Game Over.')
