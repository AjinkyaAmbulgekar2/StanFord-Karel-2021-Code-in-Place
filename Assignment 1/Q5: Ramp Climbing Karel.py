Q5: Ramp Climbing Karel

from karel.stanfordkarel import *
def main():
  put_beeper()
  while front_is_clear():
    move_to_next()
    put_beeper()
 def move_to_next():
    turn_left()
    move()
    turn_right()
    move()
    move()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
if __name__ == "__main__":
    run_karel_program("RampKarel1.w")
