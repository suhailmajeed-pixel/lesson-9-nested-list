medical_cause=input("did u have medical cause y or n:")
atten = int(input("enter the attendence of student:"))
if medical_cause == "y" :
    print("u are allowed")
else:
    if atten>=75:
        print ("allowed")
    else:
        print("not allowed")

