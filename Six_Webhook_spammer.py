from colorama import Fore
import random
import time
from dhooks import Webhook, File



print(Fore.GREEN +  '''
┌─┐┬─┐ ┬
└─┐│┌┴┬┘
└─┘┴┴ └─
''')

user_hook = input(Fore.CYAN + 'Enter a webhook: ')
hook = Webhook(user_hook)
user_time = float(input(Fore.RED + 'Enter a time: '))
user_loop = int(input(Fore.LIGHTGREEN_EX + 'Enter number of times: '))
user_message = input(Fore.YELLOW + 'Enter a message: ')

for i in range(int(user_loop)):
  time.sleep(float(user_time))
  hook.send(user_message)

