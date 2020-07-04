import os
import shutil

import keyboard as kb
from pyfiglet import figlet_format

cols, rows = shutil.get_terminal_size()
font_name = '3x5'
custom_char_replace = {'#': '\u2588'}

##### Get pre-exising total. Create a new txt otherwise
total_txt = "total.txt"
if not os.path.isfile(total_txt):
    counter = 0
else:
    with open(total_txt, 'r') as total_file:
        counter = int(total_file.readline())

##### Display counter
inc = lambda x : x + 1
dec = lambda x : x - 1
while True:
    os.system('clear')

    # Format string
    total = figlet_format(f"{counter:04d}", font=font_name)
    for char in custom_char_replace:
        total = total.replace(char, custom_char_replace[char])

    # Top padding
    for i in range(int(len(total)/5)):
        print()

    # Right padding (useless until text alignment added)
    # Bottom padding (pretty much useless as well)
    # Left padding
    for i in range(5):
        total.replace('\n', f"{' '*cols}\n")

    # Display total
    print(total)

    # Get input
    inp = input("+/-/e: ")
    if inp == "-":
        counter = dec(counter)
        if counter < 0:
            counter = 0
    elif inp == "+":
        counter = inc(counter)
    
    # Save total
    with open(total_txt, 'w') as total_file:
        total_file.write(f"{counter}")
    if inp == 'e':
        exit()