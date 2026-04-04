#Geography Quiz Game

name = input ("\nEnter your name ")
print ("\nHello", name)
question = input ("\nDo you want to try a short Geography Quiz Game? ")
count = 0
wrong = 0
if question == "yes":
    print ("\n**Let's Gooooo**")

#Question 1
question1 = input ("\nWhat is the largest ocean in the world? ")
if question1 .lower() == "pacific ocean":
    print ("correct")
    count += 1
else:
    print ("incorrect")
    wrong += 1

#Question 2
question2 = input ("\nWhich continent is the largest in terms of area? ")
if question2 .lower() == "asia":
    print ("correct")
    count += 1
else:
    print ("incorrect")
    wrong += 1

#Question 3
question3 = input ("\nWhat is the official currency of Japan? ")
if question3 .lower() == "yen":
    print ("correct")
    count += 1
else:
    print ("incorrect")
    wrong += 1

#Question 4
question4 = input ("\nWhich African country is home to the most pyramids in the world? ")
if question4 .lower() == "sudan":
    print ("correct")
    count += 1
else:
    print ("incorrect")
    wrong += 1

#Question 5
question5 = input ("\nIn which country are the Spanish steps located? ")
if question5 .lower() == "italy":
    print ("correct")
    count += 1
else:
    print ("incorrect")
    wrong += 1

#Final Result
if count == 5:
    print(f"\nSUPERB {name.upper ()} Your score is {count}")

elif count == 4:
    print(f"\nEXCELLENT {name.upper ()} Your score is {count}")

elif count == 3:
    print(f"\nGOOD JOB {name.upper ()} Your score is {count}")

elif count == 2:
    print(f"\nNOT BAD, KEEP PRACTISING {name.upper ()} Your score is {count}")

elif count == 1:
    print(f"\nDON'T GIVE UP, TRY AGAIN {name.upper ()} Your score is {count}")

else:
    print (f"{name.upper ()}, YOU NO GET BRAIN OOOOO")
    print (f"\nYour score is {count}\n")

