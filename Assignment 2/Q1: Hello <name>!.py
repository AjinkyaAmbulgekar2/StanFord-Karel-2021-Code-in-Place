Q1: Hello <name>!

"""
Prompts the user for their name and then says hello!
"""

def main():

    inp = input("What is your name? ") # input() function takes input from user and save in variable inp
    print('Hello', inp +'!') # using string concatenation you can print given output



if __name__ == '__main__':
    main()
