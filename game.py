import random 
secret=random.randint(1,100)

while True:
    guess=int(input("enter number between 1-100: "))
    if guess<secret:
        print("very low")
    elif guess>secret:
        print("too high")
    else:
        print("you won budddy")
        break
 
