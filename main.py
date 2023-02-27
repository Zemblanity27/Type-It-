import time as tm
from pyfiglet import Figlet
from colored import fg
import random
import csv

def main():
    f = Figlet(font='big')
    print(f.renderText("Welcome to TYPE IT!"))
    countdown_test()
    test = get_test()
    print(test, "\n")

    #Starting the test
    time, user_input = start_test()
    results(time, user_input)

    #For accuracy percentage
    percent = accuracy_checker(test, user_input)
    print(f"Accuracy: {fg(47)}{round(percent, 2)}%")
    print(fg('white'), end="")


def get_test():
    with open("test.csv") as test:
        choice = csv.reader(test)
        chosen_test = random.choice(list(choice))
        chosen_test = str(chosen_test).replace("['", "").replace("']", "")
        return chosen_test


def countdown_test():
    print("The Test will begin in 5 seconds. Please get Ready!")
    print("5!")
    for i in range(4):
        tm.sleep(1)
        print(4 - i, "!", sep="")
    print()
    print("START! Press Enter After Typing!", "\n")
    tm.sleep(1)

def start_test():
    start = tm.time()
    user_input = input("Type: ")
    end = tm.time()
    result_time = end - start
    result_time = round(result_time, 2)
    return result_time, user_input

def results(time, user):
    f = Figlet(font='big')
    print(f.renderText("Here's Your Results :"))
    print(f"Time: {fg(47)}{time} seconds")
    print(fg('white'), end="")
    print(f"User: {fg(47)}{user}")
    print(fg('white'), end="")
    return time, user

def accuracy_checker(test, user):
    correct = 0
    length = len(test)
    for i in range(length):
        if i >= len(user):
            break
        if user[i] == test[i]:
            correct = correct + 1
    percent_accuracy = (correct / len(test)) * 100
    return percent_accuracy




if __name__ == "__main__":
    main()
