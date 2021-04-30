Q3: Cleanup Karel, Milestone 1

 from karel.stanfordkarel import *
# program starts at main
def main():
 for i in range(1):
  if beepers_present():
   pick_beeper()
if __name__ == '__main__':
    run_karel_program('SafePickup2.w')
