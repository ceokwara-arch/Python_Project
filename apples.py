#Apple Stock Level
#Maximum Apple Number = 1000

print ("\nApple Stock Level ")
apples = int(input("\nEnter Stock Number: "))

#Enter Number OF Apples

if apples >= 750:
    print("Status: OVER STOCK")
    print("Action: Pause ordering and consider promotions to reduce stock.\n")

elif apples >= 500:
    print("Status: OPTIMAL")
    print("Action: Maintain current stock levels.\n")

elif apples >= 250:
    print("\Status: LOW")
    print("Action: Place a re-stock order soon.\n")
else:
    print("Status: CRITICAL")
    print("Action: Urgently order more stock immediately\n")