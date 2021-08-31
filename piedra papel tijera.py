from time import sleep
import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

game_choice = ['piedra', 'papel', 'tijera']
print (f"{bcolors.WARNING} \n La piedra aplasta las tijeras. Las tijeras cortan el papel. El papel cubre la piedra. \n {bcolors.ENDC}")

victoria = f"{bcolors.OKGREEN}Has ganado!{bcolors.ENDC}"
derrota = f"{bcolors.FAIL}Has perdido!{bcolors.ENDC}"
x = 1
while x<5:

    human_player = input ('¿Que eliges, piedra, papel o tijera? ')
    print('\n')
    human_player = human_player.lower ()
    AI_player = random.choice (game_choice)
    print ('Tú elegiste ' +human_player+ ', y la IA eligió ' +AI_player)
    sleep (1)
    print('*')
    sleep (1)
    print('*')
    sleep (1)
    print('*')    
    #empate
    if human_player == AI_player:
        print ('¡Es un empate!')
    #piedra tijera
    elif human_player == 'piedra':
        if AI_player == 'tijera':
            print (victoria)
        elif AI_player == 'papel':
            print (derrota)
    elif human_player == 'tijera':
        if AI_player == 'piedra':
            print (derrota)
        elif AI_player == 'papel':
            print (victoria)
    elif human_player == 'papel':
        if AI_player == 'tijera':
            print (derrota)
        elif AI_player  == 'piedra':
            print (victoria)
    else:
        print('Has escrito ', human_player)
        print('Por favor, introduce una opcion entre piedra, papel o tijera')
    sleep (1)
    print('*')
    print('*') 

    if input('Escribe salir si quieres abandonar el juego, pulsa Enter si quieres seguir jugando').lower() == 'salir':
        break
    sleep (1)
    print('\n')