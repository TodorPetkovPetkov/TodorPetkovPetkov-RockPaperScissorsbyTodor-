import random
import time

c = 0
n = 0


def wait(wait_time):
    time.sleep(wait_time)


while 0 < 1:
    action = input("\nRock, paper, or scissors? (r/p/s) -  ")
    print('')
    actions = ["r", "p", "s"]
    if (action in actions):
        i = random.choice(actions)
        if i == action:
            wait(0.5)
            print("You both chose " + action + ".")
            wait(0.5)
        if not i == action:
            if i == "r":
                if action == "p":
                    wait(0.5)
                    print("You covered the rock with paper!")
                    wait(0.5)
                if action == "s":
                    wait(0.5)
                    print("You lost to the rock! You scissors are smashed!")
                    wait(0.5)
            if i == "p":
                if action == "r":
                    wait(0.5)
                    print("Your rock was covered by paper!")
                    wait(0.5)
                if action == "s":
                    wait(0.5)
                    print("You cut the paper!")
                    wait(0.5)
            if i == "s":
                if action == "r":
                    wait(0.5)
                    print("Your smashed the scissors!")
                    wait(0.51)
                if action == "p":
                    wait(0.5)
                    print("Your paper was cut!")
                    wait(0.5)
    else:
        print("\nThis is not an option.")
        c += 1
        wait(0.5)
        if (c % 5 == 0):
            n += 1
            x = 0

            while x < n:
                print("\nYou need to choose r or p or s ")
                print("")
                x += 1

            wait(1)