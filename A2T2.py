from colorama import Fore, Style, init
sum=0
for i in range(1,51):
    sum=sum+i
print("The" +Fore.YELLOW+ " sum"+ Style.RESET_ALL+" of numbers\033[34m from\033[35m 1\033[0m to\033[35m 50\033[34m is\033[35m:\033[35m",sum)