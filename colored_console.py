from termcolor import colored, cprint
import random

colors = ['white', 'blue', 'red', 'green', 'yellow', 'grey', 'magenta', 'cyan']
choice = random.choice(colors)
text = colored('H', choice,)
choice = random.choice(colors)
text += colored('E', choice,)
choice = random.choice(colors)
text += colored('L', choice,)
choice = random.choice(colors)
text += colored('L', choice,)
choice = random.choice(colors)
text += colored('O', choice,)


print(text)