print("\nWelcome To my Bible Quiz")

name = input ("\nWhat is your name? ")
print ("Hi", name)

suggestion = input("\nDo you want to test your Bible knowledge? ").lower()
count = 0
wrong = 0

if suggestion == "yes":
    print("Let's begin")
    print("\n*** I'll ask 5 Questions ***")
    
    question1 = input("\nQ1: What is the First Book of the Bible?: ")

    if question1.strip() .lower() == "genesis":
        print("\033[92mCorrect\033[0m")
        count += 1
    else:
        print("\033[91mWrong \033[0m")
        wrong += 1

    question2 = input("\nQ2: Who was swallowed by a great Fish?: ")

    if question2.strip().lower() == "jonah":
        print("\033[92mCorrect\033[0m")
        count += 1
    else:
        print("\033[91mWrong \033[0m")
        wrong += 1

    question3 = input("\nQ3: How many disciples did Jesus have?: ")

    if question3 == "12" or question3 == "twelve":
        print("\033[92mCorrect\033[0m")
        count += 1
    else:
        print("\033[91mWrong \033[0m")
        wrong += 1

    question4 = input("\nQ4: What did God tell Noah to build?: ")

    if question4.strip().lower() == "ark":
        print("\033[92mCorrect\033[0m")
        count += 1
    else:
        print("\033[91mWrong \033[0m")
        wrong += 1

    question5 = input("\nQ5: Who defeated Goliath?: ")

    if question5.strip().lower() == "david":
        print("\033[92mCorrect\033[0m")
        count += 1
    else:
        print("\033[91mWrong \033[0m")
        wrong += 1

    if count >= 4:
        print(f"\nCONGRATULATIONS\nYour score is: {count}\n")
    else:
        print(f"\nBetter Luck Next Time !!\nYour score is {count}")

else:
    quit()
