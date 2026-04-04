#Bible Quiz Game
# Welcome Message

print("\nWelcome To My Bible Quiz")

# Ask for the player's name
name = input ("\nWhat is your name? ")
print ("Hi", name)

# Ask if the player wants to start the quiz
suggestion = input("\nDo you want to test your Bible knowledge? Yes or No: ").lower()

# Score counters
count = 0
wrong = 0

# Start quiz only if user says yes
if suggestion == "yes":
    print("Let's begin")
    print("\n** Prepare yourself for 10 questions **")

# Question 1
    question1 = input("\nQ1: What is the First Book of the Bible?: ")

    if question1.strip() .lower() == "genesis":
        print("\033[92mCorrect\033[0m")
        count += 1
    else:
        print("\033[91mWrong \033[0m")
        wrong += 1

# Question 2
    question2 = input("\nQ2: Who was swallowed by a great Fish?: ")

    if question2.strip().lower() == "jonah":
        print("\033[92mCorrect\033[0m")
        count += 1
    else:
        print("\033[91mWrong \033[0m")
        wrong += 1

# Question 3       
    question3 = input("\nQ3: How many disciples did Jesus have?: ")

    if question3 == "12" or question3 == "twelve":
        print("\033[92mCorrect\033[0m")
        count += 1
    else:
        print("\033[91mWrong \033[0m")
        wrong += 1

# Question 4
    question4 = input("\nQ4: What did God tell Noah to build?: ")

    if question4.strip().lower() == "ark":
        print("\033[92mCorrect\033[0m")
        count += 1
    else:
        print("\033[91mWrong \033[0m")
        wrong += 1

# Question 5
    question5 = input("\nQ5: Who defeated Goliath?: ")

    if question5.strip().lower() == "david":
        print("\033[92mCorrect\033[0m")
        count += 1
    else:
        print("\033[91mWrong \033[0m")
        wrong += 1

# Question 6
    question6 = input("\nQ6: Who was thrown into the lions'den?: ")

    if question6.strip().lower() == "daniel":
        print("\033[92mCorrect\033[0m")
        count += 1
    else:
        print("\033[91mWrong \033[0m")
        wrong += 1
        
# Question 7
    question7 = input("\nQ7: What did Jesus turn water into at the wedding in Cana?: ")

    if question7.strip().lower() == "wine":
        print("\033[92mCorrect\033[0m")
        count += 1
    else:
        print("\033[91mWrong \033[0m")
        wrong += 1

# Question 8
    question8 = input("\nQ8: Who was given a coat of many colors?: ")

    if question8.strip().lower() == "joseph":
        print("\033[92mCorrect\033[0m")
        count += 1
    else:
        print("\033[91mWrong \033[0m")
        wrong += 1

# Question 9
    question9 = input("\nQ9: Which apostle was a tax collector before following Jesus?: ")

    if question9.strip().lower() == "mathew":
        print("\033[92mCorrect\033[0m")
        count += 1
    else:
        print("\033[91mWrong \033[0m")
        wrong += 1

    question10 = input("\nQ10: Who was the strongest man in the Bible, known for his long hair?: ")

# Question 10
    if question10.strip().lower() == "samson":
        print("\033[92mCorrect\033[0m")
        count += 1
    else:
        print("\033[91mWrong \033[0m")
        wrong += 1

# Final result section
    if count in [10]:
        print(f"\nSUPERB {name.upper()}\nYour score is {count}\n")

    elif count in [9]:
        print(f"\nEXCELLENT {name.upper()}\nYour score is {count}")  

    elif count in [7,8]:
        print(f"\nWELL DONE {name.upper()}\nYour score is {count}")

    elif count in [5,6]:
        print(f"\nGOOD EFFORT {name.upper()}\nYour score is {count}")

    elif count in [4]:
        print(f"\nKEEP PRACTISING {name.upper()}\nYour score is {count}\n")

    elif count in [2,3]:
        print(f"\nDON'T GIVE UP {name.upper()} - TRY AGAIN\nYour score is {count}\n")

    elif count in [0,1]:
        print(f"\nGOODBYE, YOU NO GET BRAIN\nYour score is {count}\n")
else:
    quit()