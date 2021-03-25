import random
import time
from PIL import ImageTk, Image
from tkinter import *

# Most common chords in a Key, chord chart from https://www.harpkit.com/mm5/ukulele-chords.html
"""
random_chord = 'C'
root = Tk()
canvas = Canvas(root, width = 275, height = 275)
canvas.pack()
img = PhotoImage(file="Chord Pictures/"+random_chord+".PNG")
canvas.create_image(75,50, anchor=NW, image=img)
mainloop()
"""


#Sg.Window(title='Ukulele Trainer', layout=[[]], margins=(150, 100)).read()

chord_in_key = {
    'F': ['F', 'Bb', 'C', 'C7', 'Dm'],
    'C': ['C', 'F', 'G', 'G7', 'Am'],
    'G': ['G', 'C', 'D', 'D7', 'Em'],
    'D': ['D', 'G', 'A', 'A7', 'Bm'],
    'A': ['A', 'D', 'E', 'E7', 'F#m'],
    'E': ['E', 'A', 'B', 'B7', 'C#m']}

choice = (input('What key would you like to practice in? ').upper())
length = int(input('How many minutes would you like to practice for? '))
interval = int(input('How many seconds between chord switches? '))

chords_to_practice = [[chord for chord in chord_in_key[key]] for key in chord_in_key.keys() if key == choice][0]

# chord_pic = Image.open(r'C:\Users\colin\PycharmProjects\UkuleleTrainer\Chord Pictures\Bb.PNG')
# chord_pic.show()


def chord_switch(interval, length):
    # interval is how often to switch to a new chord
    # length is how many minutes you want to practice

    start_time = time.time()
    stop_time = start_time + (60.0 * length)
    practice = True

    while practice:  # every x(number of interval) seconds prints out a chord
        random_chord = random.choice(chords_to_practice)
        print(random_chord)

        time.sleep(interval - ((time.time() - start_time) % interval))
        if time.time() >= stop_time:
            practice = False
            print(f'You have completed {length} minute of practice in the key of {choice}. ')


chord_switch(interval, length)
