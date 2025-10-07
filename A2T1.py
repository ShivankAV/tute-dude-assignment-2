from colorama import Fore, Style, init
init(autoreset=True)
number=int(input( "Enter a number:" ))
if(number%2==0):
    print(f"\033[35m{number}\033[34m is\033[0m an even number")
else:
    print(f"\033[35m{number}\033[34m is\033[0m an odd number")