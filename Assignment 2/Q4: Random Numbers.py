Q4: Random Numbers

import random

NUM_RANDOM = 10
MIN_RANDOM = 0
MAX_RANDOM = 100

def main():
    for i in range(NUM_RANDOM):
        n = random.randint(MIN_RANDOM, MAX_RANDOM)
        print(str(n))

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
