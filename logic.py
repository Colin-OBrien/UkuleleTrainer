import random
import time

def chord_switch(interval, length, choice):
    # interval is how often to switch to a new chord
    # length is how many minutes you want to practice

    chord_in_key = {
        'F': ['F', 'Bb', 'C', 'C7', 'Dm'],
        'C': ['C', 'F', 'G', 'G7', 'Am'],
        'G': ['G', 'C', 'D', 'D7', 'Em'],
        'D': ['D', 'G', 'A', 'A7', 'Bm'],
        'A': ['A', 'D', 'E', 'E7', 'F#m'],
        'E': ['E', 'A', 'B', 'B7', 'C#m']}

    chords_to_practice = [[chord for chord in chord_in_key[key]] for key in chord_in_key.keys() if key == choice][0]

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

