import keyboard

#whenever these letters are typed within (timout seconds) followed by a space, the second parameter will replace the text before the space was typed
keyboard.add_abbreviation('tt', 'think ', timeout = 2)
keyboard.add_abbreviation('ts', 'this ')
keyboard.add_abbreviation('th', 'that ')
keyboard.add_abbreviation('wl', 'will ')

#The code will keep running in the background until the command in args is pressed
keyboard.wait('Ctrl+Esc')