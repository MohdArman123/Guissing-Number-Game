import random

secret_number = int(random.randint(1,100))

guissing_number = 0

tries = 0

while guissing_number != secret_number:

    guissing_number = int(input("make a guess;"))
    tries = tries + 1

    if guissing_number > secret_number:

        print("Too High!")

    elif guissing_number < secret_number:

        print("Too Low!")

    else:

       print("you got the Rigt number!")
       


print("Number of tries:" ,tries)
    

 
