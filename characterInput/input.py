import datetime
def main():
    print("Hello! This program will calculate in which year you will turn 100.")
    name = str(input("What is your name? "))
    age = int(input("What is your age? "))
    now = datetime.datetime.now()
    print(name + ", you will turn 100 on the year " + str(now.year - age + 100) + "!")
main()