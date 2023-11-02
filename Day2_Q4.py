def distance():
    n = int(input("Enter distance:"))
    if n>=1 and n<=50:
        fare = n * 8
    elif n>=51 and n<=100:
        fare = n * 10
    elif n>100:
        fare = n * 12
    else:
        print("Invalid fare")
    print("The total fare is:",fare)
distance()

#input=60
#Output=600