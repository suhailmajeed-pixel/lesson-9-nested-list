units = int(input("please enter te number of units u consumed :"))
if(units < 50):
    amount = units * 2.60
    surcharge = 25

elif(units <= 100 ):
    amount = 130 + ((units - 100)*5.26)
    surcharge = 45

total = amount + surcharge
print("\neliricty bill = %.2f"% total)