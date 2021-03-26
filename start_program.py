from logic import chord_switch

choice = (input('What key would you like to practice in? ').upper())
length = int(input('How many minutes would you like to practice for? '))
interval = int(input('How many seconds between chord switches? '))

chord_switch(interval, length,choice)