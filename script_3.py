std=input("Enter name:")
rl=int(input("Enter Enroll no."))
if std=="A":
    print("Room 1")
elif std=="B":
    print("Room 2")
    if rl==98:
        print("Room 2 and 98")
elif std=="C":
    print("Room 3")
elif std=="D":
    print("Room 4")
else:
    print("Invalid")
