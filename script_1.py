#nuber is Positive or Negative and if Positive then odd or even

num=int(input("Enetr number:"))

if num>=0:# can check num>=0 and num%2==0
    if num%2==0:
        print("Positive and Even")
    else:
        print("Positive and Odd")
else:
    if num%2==0:
        print("Negative and Even")
    else:
        print("Negative and Odd")
    
