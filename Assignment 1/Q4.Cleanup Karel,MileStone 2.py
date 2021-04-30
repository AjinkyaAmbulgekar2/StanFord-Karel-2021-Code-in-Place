Q4: Cleanup Karel, Milestone 2

from karel.stanfordkarel import *
# program starts at main
def main():
    while front_is_clear():
        move()
        if  beepers_present():
             pick_beeper()
if __name__ == '__main__':
    run_karel_program('Cleanup1.w')
